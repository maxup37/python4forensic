import json

"""
STEP1 Just loading JSON
"""

with open("sample_sig.json") as data_file:
    lst_sigdata = json.loads(data_file.read())


for dic_Asigdata in lst_sigdata:
           print(dic_Asigdata)
           print(dic_Asigdata["signature"])
           lst_2bytetoken = dic_Asigdata["signature"].split()
           print(lst_2bytetoken)
           for _2bytetoken in lst_2bytetoken:
                      if _2bytetoken == "xx":
                                 print("*")
                      else:
                                 print(_2bytetoken)
                                 int_ch = int(_2bytetoken, 16)
                                 print ("%x" % int_ch)
                                 ch = chr(int_ch)
                                 print (ch)
