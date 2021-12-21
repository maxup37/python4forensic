import json
import yara
import sys

"""
Forensic: Signature Analyzer
"""

'''
[USAGE]
*CMD>mxsigtool {Target}

ex) > mxsigtool.py hwp.hwp
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

        self.matchInfo = {}

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

    def search(self, target):
        if isinstance(target, list):
            return self.__search(target, None)
        elif isinstance(target, str):  # path
            return self.__search_file(target)
        return None

    def __search_file(self, target_path):

        with open(target_path, "rb") as fo:
            data = fo.read(1024)

        target = ["%02X" % i for i in data]

        return self.__search(target, target_path)

    def __search(self, target, target_path):
        self.matchInfo = {}
        if self.__dfs_search(self.RootNode, target, 0) == True:
            if target_path and self.matchInfo["Yara_rule"]:
                dic_result = self.__yara(target_path, self.matchInfo["Yara_rule"])
                if dic_result == None:
                    return None
                else:
                    self.matchInfo['type'] = dic_result['type']
                    self.matchInfo['ext'] = dic_result['extension']

            return self.matchInfo

        else:
            return None

    def __dfs_search(self, curNode, target, index):
        if target[index] in curNode.child:
            if curNode.child[target[index]].isMatch == True:
                self.matchInfo = curNode.child[target[index]].dicMatchInfo
                return True
            else:
                if self.__dfs_search(curNode.child[target[index]], target, index + 1) == True:
                    return True

        if "xx" in curNode.child:
            if curNode.child["xx"].isMatch == True:
                self.matchInfo = curNode.child[target[index]].dicMatchInfo
                return True
            else:
                return self.__dfs_search(curNode.child["xx"], target, index + 1)

        return False

    def __yara(self, search_yara, cmp_rule_name):

        try:
            rules = yara.compile(filepath="yararules\\{}".format(cmp_rule_name))
        except yara.Error as e:
            print(e)
            return None

        matches = rules.match(search_yara)

        if len(matches) == 0:
            return None

        result = {}
    
        if 'type' in matches[0].meta:
            result['type'] = matches[0].meta['type']
        else:
            result['type'] = matches[0].rule

        if 'extension' in matches[0].meta:
            result['extension'] = matches[0].meta['extension']        
        else:
            result['extension'] = matches[0].rule
        return result


if __name__ == "__main__":

    get_target = sys.argv[1]
    
    sigpattern = SigTree("jsonrule\\rule.json")

    sigpattern.trace()

    #matchInfo = sigpattern.search(["D0", "CF", "11", "E0", "A1", "B1", "1A", "E1", "CC"])
    matchInfo = sigpattern.search(get_target)

    if matchInfo:
        print("Match (TYPE:%s, EXT:%s)" % (matchInfo['type'], matchInfo['ext']))
    else:
        print("Not Match")
