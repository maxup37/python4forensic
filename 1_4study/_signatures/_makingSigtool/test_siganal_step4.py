import json

"""
STEP4 Offset 추가

  - 확인을 위해 tree 탐색 기능 구현 안됨
  - pattern search 구현 안됨 
"""
class Node(object):
           def __init__(self, data_="", isMatch_=False, objMatchInfo_={}):
                      self.data = data_
                      self.child = {}
                      self.isMatch = isMatch_
                      self.dicMatchInfo = objMatchInfo_

           def __repr__(self):
                      return ("Object Node(%s)" % self.data)

                      
           def get_child(self):
                      return self.child

           def get_data(self):
                      return self.data

with open("sample_sig2.json") as data_file:
    lst_sigdata = json.loads(data_file.read())

SigTreeRoot = Node()



for dic_Asigdata in lst_sigdata:
           lst_2bytetoken = dic_Asigdata["signature"].split()

           lstsize = len(lst_2bytetoken)

           # curNode는 reference로서 SigTreeRoot 객체의 reference이다.
           # c언어와 같이 curNode가 어떤 데이터(값, 구조체 등)를 저장하는 변수가 아니다.
           # -> Call by Object Reference를 이해해야 한다.: https://yes90.tistory.com/47
           curNode = SigTreeRoot        

           offset = dic_Asigdata["offset"]

           for i in range(offset):
               curNode.child["xx"] = Node("xx")
               print("ADD: xx to %s" % curNode.get_data())
               curNode = curNode.child["xx"]
               

               
           cnt = 0
          
           
           for _2bytetoken in lst_2bytetoken:
                cnt += 1
                if not _2bytetoken in curNode.child:
                    if cnt == lstsize:
                       print("Last ADD: %s to %s" % (_2bytetoken, curNode.get_data()))
                       curNode.child[_2bytetoken] = Node(_2bytetoken, True, {"type":dic_Asigdata["type"], "ext":dic_Asigdata["extension"]})
                    else:
                       curNode.child[_2bytetoken] = Node(_2bytetoken)
                       print("ADD: %s to %s" % (_2bytetoken, curNode.get_data()))

                curNode = curNode.child[_2bytetoken]


print(SigTreeRoot.get_child())
                       
                                  
                                  
