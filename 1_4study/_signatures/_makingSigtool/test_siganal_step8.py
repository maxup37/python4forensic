import json
import yara
import sys

"""
STEP 8 ADD YARA , get argument
"""

'''
How to use
*CMD>python {.py path} {Target}

ex) >python test_siganal_step8.py hwp.hwp
'''

class Node(object):
    def __init__(self, id_=0, isMatch_=False, objMatchInfo_={}):
        self.id = id_
        self.child = {}
        self.isMatch = isMatch_
        self.dicMatchInfo = objMatchInfo_

    def __repr__(self):
        return ("[%d] Object Node(isLast? %r)" % (self.id, self.isMatch))


class SigTree(object):

    def __init__(self, fpath):
        with open(fpath) as data_file:
            lst_sigdata = json.loads(data_file.read())

        self.RootNode = Node()
        self.uid = 1

        self.matchinfo = {}

        for dic_Asigdata in lst_sigdata:
            lst_2bytetoken = dic_Asigdata["signature"].split()

            lstsize = len(lst_2bytetoken)

            curNode = self.RootNode

            offset = dic_Asigdata["offset"]

            for i in range(offset):
                curNode.child["xx"] = Node(self.uid, "xx")
                self.uid += 1
                curNode = curNode.child["xx"]

            cnt = 0

            for _2bytetoken in lst_2bytetoken:
                cnt += 1
                if not _2bytetoken in curNode.child:
                    if cnt == lstsize:
                        curNode.child[_2bytetoken] = Node(self.uid, True, {"type": dic_Asigdata["type"],
                                                                           "ext": dic_Asigdata["extension"],
                                                                           "Yara_rule": dic_Asigdata["Yara_rule"]})
                        self.uid += 1
                    else:
                        curNode.child[_2bytetoken] = Node(self.uid)
                        self.uid += 1

                curNode = curNode.child[_2bytetoken]

    def trace(self):
        self.__dfs_trace(self.RootNode)

    def __dfs_trace(self, curNode):

        for k, v in curNode.child.items():
            self.__dfs_trace(v)

    def search(self, target, index):
        if isinstance(target, list):
            return self.__search(target, index)
        elif isinstance(target, str):  # path
            return self.__search_file(target, index)
        return {}

    def __search_file(self, target_path, index):

        with open(target_path, "rb") as fo:
            data = fo.read(1024)

        target = ["%02X" % i for i in data]

        return self.__search(target, index)

    def __search(self, target, index):
        self.matchinfo = {}
        if self.__dfs_search(self.RootNode, target, index) == True:
            return self.matchinfo
        else:
            return {}

    def __dfs_search(self, curNode, target, index):
        if target[index] in curNode.child:
            if curNode.child[target[index]].isMatch == True:
                self.matchinfo = curNode.child[target[index]].dicMatchInfo
                return True
            else:
                if self.__dfs_search(curNode.child[target[index]], target, index + 1) == True:
                    return True

        if "xx" in curNode.child:
            if curNode.child["xx"].isMatch == True:
                self.matchinfo = curNode.child[target[index]].dicMatchInfo
                return True
            else:
                return self.__dfs_search(curNode.child["xx"], target, index + 1)

        return False


def Yara(search_yara,cmp_rule_name):

    rules = yara.compile(filepath=cmp_rule_name)

    matches = rules.match(search_yara)
    
    result = list(matches[0].meta.values())
    
    return result

if __name__ == "__main__":

    get_target = (sys.argv[1])
    
    sigpattern = SigTree("rule.json")

    sigpattern.trace()

    # matchInfo = sigpattern.search(["01", "FF", "F8", "FF", "F7", "88"], 0)
    matchInfo = sigpattern.search(get_target, 0)

    if matchInfo:
        if matchInfo["Yara_rule"]!=None:
            result_list = Yara(get_target,matchInfo["Yara_rule"])
            print("Match (TYPE:%s, EXT:%s)" % (result_list[0], result_list[1]))
        else:
            print("Match (TYPE:%s, EXT:%s)" % (matchInfo["type"], matchInfo["ext"]))
    else:
        print("Not Match")
