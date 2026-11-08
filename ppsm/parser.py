# mcParser
import json
import xml.etree.ElementTree as ET

TEST_PATH = "test_files/my_scan.xml"

ATTR_PREFIX = "#"   # attributes become "#addr", "#state", ...
TEXT_KEY = "#text"  # text content, only added if non-empty


def parse_scan(file_path, ip, inputName):
    root = ET.parse(file_path).getroot()
    records = []

    # this is purely looking through the XML tree, and combining it nicely for the current format of export.py 
    for host in root.findall("host"):
        ip = host.find("address[@addrtype='ipv4']")
        name = host.find("hostnames/hostname")

        for port in host.findall("ports/port"):
            if port.find("state").get("state") != "open":
                #not open, skip it.
                continue
            service = port.find("service")

            # Get all the relevant data export needs. If it doesn't exists, we can just put a blank string.
            records.append({
                "ports": port.get("portid"),
                "protocol": port.get("protocol"),
                "service": service.get("name") if service is not None else "",
                "source_ip": ip.get("addr") if ip is not None else "",
                "source_name": inputName if inputName is not None else "",
                "destination_ip": ip.get("addr") if ip is not None else "",
                "destination_name": name.get("name") if name is not None else "",
            })
    return records

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