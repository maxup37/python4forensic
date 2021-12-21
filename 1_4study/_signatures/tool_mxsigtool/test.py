import mxsigtool
import sys

get_target = sys.argv[1]
    
sigpattern = mxsigtool.SigTree("jsonrule\\rule.json")

sigpattern.trace()

# matchInfo = sigpattern.search(["01", "FF", "F8", "FF", "F7", "88"], 0)
matchInfo = sigpattern.search(get_target, 0)

if matchInfo:
    if matchInfo["Yara_rule"]!=None:
        dic_result = mxsigtool.Yara(get_target,matchInfo["Yara_rule"])
        if dic_result == None:
            print("Not Match")
        else:
            print("Match (TYPE:%s, EXT:%s)" % (dic_result['type'], dic_result['extension']))
    else:
            print("Match (TYPE:%s, EXT:%s)" % (dic_result['type'], dic_result['extension']))
else:
    print("Not Match")
