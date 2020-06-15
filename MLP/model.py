import os
import random
import xml.etree.ElementTree as ET

person = {"2480":"person 1", "2844":"person 2", "2944":"person 3", "2848":"person 4", "3008":"person 5", "1036":"person 6"}
person2 = {"{9e1903ff-2cdb-0000-0b05-199edb2cd601}":"person 1", "{3591cc69-2cda-0001-b1cc-9135da2cd601}":"person 2",
            "{46ce64eb-2cda-0001-3665-ce46da2cd601}":"person 3", "{a21559d7-2cda-0001-275a-15a2da2cd601}":"person 4",
            "{e0e75f9b-2cda-0001-ec5f-e7e0da2cd601}":"person 5", "{7eccaef9-2cd8-0000-01b0-cc7ed82cd601}":"person 6"}
def user_classify(Data_dir):
    test_sets = os.listdir(Data_dir)
    for test_set in test_sets:
        sysmon = Data_dir+"/"+test_set+"/Sysmon.xml"
        xmltree = ET.parse(sysmon)
        flag = 0
        for elem in xmltree.iter("{http://schemas.microsoft.com/win/2004/08/events/event}Execution"):
            try:
                print(test_set, ": ", person[elem.attrib["ProcessID"]])
                flag = 1
            except:
                pass
            break
        if flag == 0:
            security = Data_dir+"/"+test_set+"/Security.xml"
            xmltree = ET.parse(security)
            for elem in xmltree.iter("{http://schemas.microsoft.com/win/2004/08/events/event}Correlation"):
                try:
                    print(test_set, ": ", person[elem.attrib["ActivityID"]])
                except:
                    print(test_set, ":  person", random.randint(1,7))
                break
        
