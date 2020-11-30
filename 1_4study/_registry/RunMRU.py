import pyregf
import sys


reg = sys.argv[1]
clsRegf = pyregf.file()

clsRegf.open(reg)


Rkey_RunMRU = clsRegf.get_key_by_path(r"Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU")

NumVal = Rkey_RunMRU.get_number_of_values()
Lwt = str(Rkey_RunMRU.get_last_written_time())

print "Registry Key Name : " + Rkey_RunMRU.get_name()
print "Number of Values : " + str(NumVal)
print "Last Written Time : " + Lwt
print "-------------------------------------------------"

for i in xrange(NumVal):
	v0 = Rkey_RunMRU.get_value(i)

	Data_Type = str(v0.get_type())

	print "Value Name : " + v0.get_name()

	if Data_Type =="0":
		print "Data_Type : REG_NONE"
	elif Data_Type == "1":
		print "Data_Type : REG_SZ"
	elif Data_Type =="2":
		print "Data_Type : REG_EXPAND_SZ"
	elif Data_Type =="3":
		print "Data_Type : REG_BINARY"
	elif Data_Type =="4":
		print "Data_Type : REG_DWORD/REG_DWORD_LITTLE_ENDIAN"
	elif Data_Type =="5":
		print "Data_Type : REG_DWORD_BIG_ENDIAN"
	elif Data_Type =="6":
		print "Data_Type : REG_LINK"
	elif Data_Type =="7":
		print "Data_Type : REG_MULTI_SZ"
	elif Data_Type =="8":
		print "Data_Type : REG_RESOURCE_LIST"
	elif Data_Type =="9":
		print "Data_Type : REG_FULL_RESOURCE_DESCRIPTOR"
	elif Data_Type =="10":
		print "Data_Type : REG_RESOURCE_REQUIREMENT_LIST"
	elif Data_Type =="11":
		print "Data_Type : REG_QWORD"

	print "Data : " + v0.get_data_as_string()
	print "-------------------------------------------------"
clsRegf.close()
