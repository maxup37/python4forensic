import json

"""
STEP5 Pattern search (DFS)
"""
class Node(object):
           def __init__(self, id_=0, data_="", isMatch_=False, objMatchInfo_={}):
                      self.id = id_
                      self.data = data_
                      self.child = {}
                      self.isMatch = isMatch_
                      self.dicMatchInfo = objMatchInfo_

           def __repr__(self):
                      return ("Object Node(%s, %d)" % (self.data, self.isMatch))

                      
           def get_child(self):
                      return self.child

           def get_data(self):
                      return self.data

with open("sample_sig2.json") as data_file:
    lst_sigdata = json.loads(data_file.read())

SigTreeRoot = Node()


def DFS_trace(curNode):
    if curNode.get_data() == "":
        print("ROOT")
    else:
        print(curNode.get_data())

    for k,v in curNode.get_child().items():
        DFS_trace(v)


def DFS_search(curNode, target, index):
    print("***********STEP1: %d, %s" % (curNode.id, curNode.data))
    if target[index] in curNode.get_child():
        if curNode.get_child()[target[index]].isMatch == True:
            print("Match!!!!! STEP1 %d:%d"% (curNode.id,curNode.get_child()[target[index]].id) )
            return True
        else:
            print("ST1:%d"%curNode.id)
            if DFS_search(curNode.get_child()[target[index]], target, index+1) == True:
                return True

    print("***********STEP2: %d, %s" % (curNode.id, curNode.data))
    if "xx" in curNode.get_child():
        if curNode.get_child()["xx"].isMatch == True:
             print("Match!!!!! STEP2  %d:%d"% (curNode.id,curNode.get_child()["xx"].id) )
             return True
        else:
            print("ST2:%d"%curNode.id)
            if DFS_search(curNode.get_child()["xx"], target, index+1) == True:
                return True
    print("ST4:%d"%curNode.id)
    return False
            
Uid = 1

for dic_Asigdata in lst_sigdata:
           lst_2bytetoken = dic_Asigdata["signature"].split()

           lstsize = len(lst_2bytetoken)

           # curNode는 reference로서 SigTreeRoot 객체의 reference이다.
           # c언어와 같이 curNode가 어떤 데이터(값, 구조체 등)를 저장하는 변수가 아니다.
           # -> Call by Object Reference를 이해해야 한다.: https://yes90.tistory.com/47
           curNode = SigTreeRoot        

           offset = dic_Asigdata["offset"]

           for i in range(offset):
               curNode.child["xx"] = Node(Uid, "xx")
               Uid += 1
               print("ADD: xx to %s" % curNode.get_data())
               curNode = curNode.child["xx"]
               

               
           cnt = 0
          
           
           for _2bytetoken in lst_2bytetoken:
                cnt += 1
                if not _2bytetoken in curNode.child:
                    if cnt == lstsize:
                       print("Last ADD: %s to %s" % (_2bytetoken, curNode.get_data()))
                       curNode.child[_2bytetoken] = Node(Uid, _2bytetoken, True, {"type":dic_Asigdata["type"], "ext":dic_Asigdata["extension"]})
                       Uid += 1
                    else:
                       curNode.child[_2bytetoken] = Node(Uid, _2bytetoken)
                       Uid += 1
                       print("ADD: %s to %s" % (_2bytetoken, curNode.get_data()))

                curNode = curNode.child[_2bytetoken]

print("Test")

DFS_trace(SigTreeRoot)

DFS_search(SigTreeRoot, ["01", "FF", "F8", "FF", "F6", "88"], 0)
                       
                                  
                                  
