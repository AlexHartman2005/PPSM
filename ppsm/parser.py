# mcParser
# WIP
import xml.etree.ElementTree as ET

# Test command: sudo nmap -sP --no-stylesheet -oX my_scan.xml 172.16.7.204/24
TEST_PATH = "/Users/kennethzheng_/Downloads/PPSM/test_files/my_scan.xml"

def parse_xml_file(file_path):
    # Option A: Parse from a local file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Option B: Parse directly from a string
    # xml_string = """
    # <catalog>
    #     <product id="101">
    #         <name>Wireless Keyboard</name>
    #         <price currency="USD">29.99</price>
    #     </product>
    #     <product id="102">
    #         <name>Hydration Backpack</name>
    #         <price currency="USD">45.00</price>
    #     </product>
    # </catalog>
    # """
    # root = ET.fromstring(xml_string)

    # Basic metadata
    print(f"Root Tag: {root.tag}")  # Output: catalog
    # print(f"Root Attributes: {root.attrib}")  # Output: {}
    # print(len(root))  # Output: []
    for host in root.findall('host'):
        print(f"Host: {host.attrib}")
        for address in host.findall('address'):
            print(f"  Address: {address.attrib}")
        for port in host.findall('ports/port'):
            print(f"  Port: {port.attrib}")
            for service in port.findall('service'):
                print(f"    Service: {service.attrib}")

if __name__ == "__main__":
    parse_xml_file(TEST_PATH)

