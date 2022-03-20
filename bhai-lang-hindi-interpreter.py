import codecs
import os


Syntax = {"अंक":"int","दशमलव":"float","हां_या_नहीं":"bool","वाक्य":"str","सच_है_भाई":"True","गलत_है_भाई":"False","खाली":"None","अगर_भाई":"if","वर्ना":"else","और_अगर":"elif","जारी_रखें":"continue","रोक_दे":"break","लौटाये":"return","बदमे_देखेंगे":"pass","जबतक_भाई":"for","जबकि_भाई":"while","और":"and","अथवा":"or","नहीं":"not","अंदर_है_भाई":"in","एब्सॉ":"abs","दीखा_भाई":"print","श्रेणी":"range","_बताओ_भाई":"def","शुरू_करे_भाई":"init","कक्षा":"class","खुद":"self"}

fileLocation = input()

print("क्या बोलती पब्लिक")
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
print("ठीक है बाई पब्लिक")