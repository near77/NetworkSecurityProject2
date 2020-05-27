import os
import xml.etree.ElementTree as ET

person = {"2480":"person 1", "2844":"person 2", "2944":"person 3", "2848":"person 4", "3008":"person 5", "1036":"person 6"}

def user_classify(Data_dir):
    test_sets = os.listdir(Data_dir)
    for test_set in test_sets:
        sysmon = Data_dir+"/"+test_set+"/Sysmon.xml"
        xmltree = ET.parse(sysmon)
        for elem in xmltree.iter("{http://schemas.microsoft.com/win/2004/08/events/event}Execution"):
            print(test_set, ": ", person[elem.attrib["ProcessID"]])
            break
        
