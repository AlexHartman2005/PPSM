# mcParser
import json
import xml.etree.ElementTree as ET

TEST_PATH = "test_files/my_scan.xml"

ATTR_PREFIX = "#"   # attributes become "#addr", "#state", ...
TEXT_KEY = "#text"  # text content, only added if non-empty


def element_to_dict(el):
    """Recursively convert an Element into a dict."""
    node = {}

    # attributes
    for k, v in el.attrib.items():
        node[ATTR_PREFIX + k] = v

    # text (ignore whitespace between tags)
    text = (el.text or "").strip()
    if text:
        node[TEXT_KEY] = text

    # children (recursive step)
    for child in el:
        child_dict = element_to_dict(child)
        if child.tag not in node:
            node[child.tag] = child_dict
        else:
            # repeated tag -> promote to list
            if not isinstance(node[child.tag], list):
                node[child.tag] = [node[child.tag]]
            node[child.tag].append(child_dict)

    return node


def parse_xml_file(file_path):
    root = ET.parse(file_path).getroot()
    return {root.tag: element_to_dict(root)}


if __name__ == "__main__":
    with open("test_files/test.json", "w") as f:
        json.dump(parse_xml_file(TEST_PATH), f, indent=4)