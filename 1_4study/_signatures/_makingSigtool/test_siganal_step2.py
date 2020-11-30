import json

"""
STEP2 Just making node class
"""
class Node(object):
           def __init__(self, id_, chvalue_, starflag_, objMatchInfo_):
                      self.id = id_
                      self.child = []
                      self.chvalue = chvalue_
                      self.starflag = starflag_
                      self.dicMatchInfo = objMatchInfo_

           def __repr__(self):
                      return "Node: [%s]" % self.id
           
           def add_child(self, node):
                      self.child.append(node)
                      
           def get_child(self):
                      return self.child   

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
