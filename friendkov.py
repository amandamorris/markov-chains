from markov import *
import re
import pprint


def open_and_clean_file(filename):
    script = open(filename)

    speech_only = []
    cleaned_speech = []
    for line in script:
        #print line
        line = line.strip()
        if line:
            if line[0] != "[" and line[0] != "(":
                speech_only.append(line)
    for line in speech_only:
        m = re.findall(r'\((.*?)\)', line)
        n = re.findall(r'\[(.*?)\]', line)
        print m
        if m != []:
            for i in range(len(m)):
                line = line.replace("(" + m[i] + ")", "")
        if n != []:
            for j in range(len(n)):
                line = line.replace("[" + n[j] + "]", "")
        cleaned_speech.append(line)
            #print line

    return cleaned_speech


def build_dictionary(clean_file):

    character_dic = {}
    for line in clean_file:
        #print line
        #print line.find(":")
        if line.find(":") != -1:
            character_name = line.split(":")[0]
            # print character_name
            script_line = line.split(":")[1]
            character_dic.setdefault(character_name, "")
            character_dic[character_name] += script_line
    return character_dic


clean_file= open_and_clean_file("friends.txt")
character_dic = build_dictionary(clean_file)
for character in character_dic.keys():
    character_dic[character] = make_chains(character_dic[character], 2)
pprint.pprint(character_dic)
# \((.*?)\)
