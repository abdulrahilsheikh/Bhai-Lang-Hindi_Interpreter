import codecs
import os


Syntax = {"_बताओ_भाई":"def",
            "जबतक_भाई":"for","जबकि_भाई":"while","करो_भाई":"do","दीखा_भाई":"print","अगर_ऐसा_है_भाई":"if","और_अगर_ऐसा_है":"elif","वर्ना":"else","अंदर_है_भाई":"in","अधिकतम":"max","न्यूनतम":"min","नीच_चे":"floor","उपारी":"ceil","और":"and","नहीं":"not","या" :"or",
            "जारी_रखें":"continue","रोक_दे":"break","लौटाये":"return","बकरी":"lambda","कक्षा":"class","शुरू_करे_भाई":"__init__","स्वयं":"self","श्रेणी":"range","वाक्य":"str","अंक":"int","दशमलव":"float","हां_या_नहीं":"bool","सच_है_भाई":"true","गलत_है_भाई":"false"}

fileLocation = input()

print("सलाम  भाई")
print()

data = None

with codecs.open(fileLocation, encoding='utf-8') as K_file:
    data = K_file.read()
K_file.close()

for key,value in Syntax.items():
    data = data.replace(key,value)

new_file = fileLocation.replace(".bhai",".py")

P_file = open(new_file,"w")
P_file.close()

with codecs.open(new_file,"w", encoding='utf-8') as P_file:
    P_file.write(data)

P_file.close()

os.system('python {}'.format(new_file))
print()
print("ठीक  है  अलविदा  भाई")