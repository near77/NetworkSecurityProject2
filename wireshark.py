import os
import json
import math

def count_dns_qry(file_path, person):
    command = "cat '" +  file_path + "' | grep "+ "'dns.qry.name\":'" +" > wireshark.txt"
    os.system(command)
    f = open("wireshark.txt")
    lines = f.readlines()
    qry_dic = {}
    for line in lines:
        try:
            qry_dic[str(line.split(":")[1][:-2]).replace(" ", "")] += 1
        except:
            qry_dic[str(line.split(":")[1][:-2]).replace(" ", "")] = 1
    qry_dic = {k: v for k, v in sorted(qry_dic.items(), key=lambda item: item[1], reverse=True)}
    weight_file = "./"+person+".json"
    with open(weight_file, "w") as f:
        content = json.dumps(qry_dic,indent=4)
        f.write(content)


def TF():
    files = os .listdir("./Logs/Train")
    for file_name in files:
        file_path = "./"+file_name+".json"
        with open(file_path) as f:
            # =============TF=================
            dns_qry = json.load(f)
            sum = 0
            for key in dns_qry:
                sum += int(dns_qry[key])
            for key in dns_qry:
                dns_qry[key] = dns_qry[key]/sum
            # ================================
            content = json.dumps(dns_qry, indent=4)
            with open(file_path, "w") as wf:
                wf.write(content)


def IDF():
    files = os .listdir("./Logs/Train")
    for file_name in files:
        file_path = "./"+file_name+".json"
        with open(file_path) as f:
            dns_qry = json.load(f)
            for key in dns_qry:
                IDF = 0
                for file_name2 in files:
                    file_path2 = "./" + file_name2 + ".json"
                    with open(file_path2) as f2:
                        dns_qry2 = json.load(f2)
                        try:
                            k = dns_qry2[key]
                            IDF += 1
                        except:
                            continue
                dns_qry[key] = dns_qry[key]*math.log(6/IDF)
            content = json.dumps(dns_qry, indent=4)
            with open(file_path, "w") as wf:
                wf.write(content)


def TFIDF(test_file):
    command = "cat '" +  test_file + "' | grep "+ "'dns.qry.name\":'" +" > wireshark.txt"
    os.system(command)
    f = open("wireshark.txt")
    lines = f.readlines()
    qry_dic = {}
    for line in lines:
        try:
            qry_dic[str(line.split(":")[1][:-2]).replace(" ", "")] += 1
        except:
            qry_dic[str(line.split(":")[1][:-2]).replace(" ", "")] = 1
    qry_dic = {k: v for k, v in sorted(qry_dic.items(), key=lambda item: item[1], reverse=True)}

    scores = []
    for i in range(1,7):
        score = 0
        weight_file = "./weights/Person_"+str(i)+".json"
        f = open(weight_file)
        weight = json.load(f)
        for key in qry_dic:
            try:
                score += qry_dic[key]*weight[key]
            except:
                continue
        scores.append(score)
    # print(scores)
    return scores.index(max(scores))+1

# files = os.listdir("./Logs/wireshark2")
# for tfile in files:
#     file_path = "./Logs/wireshark2/" + tfile + "/wireshark2.json"
#     count_dns_qry(file_path, tfile)

# TF()
# IDF()

# TFIDF("./Logs/Example Test/Test_2/Wireshark.json")