# import xml.dom.minidom as xmllib

# def read_xml(file_path):
#     doc = xmllib.parse(file_path)
#     print(doc.nodeName)
    

# read_xml("Logs/Train/Person_1/Sysmon.xml")
import xml.etree.ElementTree as ET

xmltree = ET.parse("Logs/Train/Person_1/Sysmon.xml")
elemList = []
for elem in xmltree.iter("{http://schemas.microsoft.com/win/2004/08/events/event}Execution"):
    # elemList.append(elem.tag)
    print(elem.attrib)
# elemList = list(set(elemList))
# for tag in elemList:
#     print(tag)
# root = xmltree.getroot()
# for child in root:
#     print(child.tag, ": ", child.attrib)