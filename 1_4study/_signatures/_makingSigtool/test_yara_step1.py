import yara

rules = yara.compile(filepath='yara_msdoc.rule')

matches = rules.match('example.xls')
print(matches)
#print(matches[1].strings)
#help(matches[0].rule)
