import pyregf
import sys
import pyfwsi
import datetime
import construct
from datetime import datetime

#######################################
######### References
# - https://github.com/libyal/winreg-kb/blob/master/documentation/MRU%20keys.asciidoc
#   > LastVisitedPidlMRU data format
#     . String + Shell Item List
# - https://github.com/libyal/winreg-kb/blob/master/winregrc/mru.py
#   > find _STRING_AND_SHELL_ITEM_LIST_MRU_KEY_PATHS and _ProcessMRUEntryStringAndShellItemList


#######################################
######### dependencies
# - construct (pip install construct)
# - pyfwsi (external module, must be copied to site-packages)

clsRegf = pyregf.file()

clsRegf.open(r"NTUSER.DAT")
#NTUSER.DAT file open(Must be in the same path)

key_open = clsRegf.get_key_by_path(r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU")
#path

for i in range(1,key_open.get_number_of_values()):
#Repeat the number of registry
	print "-----------------------------------------"
	print "            Registry Values              "
	print "-----------------------------------------"
	ab = key_open.get_value(i)
	print "Value Name         : " + ab.get_name()
	print "Number of Sub keys : " + str(key_open.get_number_of_sub_keys())
	print "Value Data         : " + str(ab.get_data_size())
	num = str(ab.get_type())
	#Registry type according to get_type() function value
	if num == '0' :
		print "Registry type      : REG_NONE"
	elif num == '1' :
		print "Registry type      : REG_SZ"
	elif num == '2' :
		print "Registry type      : EXPAND_SZ"
	elif num == '3' :
		print "Registry type      : REG_BINARY"
	elif num == '4' :
		print "Registry type      : REG_DWORD"
	elif num == '5' :
		print "Registry type      : REG_DWORD_BIG_ENDIAN"
	elif num == '6' :
		print "Registry type      : REG_LINK"
	elif num == '7' :
		print "Registry type      : REG_MULTI_SZ"
	elif num == '8' :
		print "Registry type      : REG_RESOURCE_LIST"
	elif num == '9' :
		print "Registry type      : REG_FULL_RESOURCE_DESCRIPTOR"
	elif num == '10' :
		print "Registry type      : REG_RESOURCE_REQUIREMENTS_LIST"
	elif num == '11' :
		print "Registry type      : REG_QWORD"
			
	########################################
	# Shell Item List parsing
	#    - TYPE: FileName(unicode, little endian) + ShellItemList
	#    - CASE: Windows 10, LastVisitedPidlMRU

	data = ab.get_data()
	
	_DATA_SHELLITEMMRU_STRUCT = construct.Struct(
		'pname' / construct.RepeatUntil(lambda obj, lst, ctx: obj == 0, construct.Int16ul),
		#Rotate until lambda values = 0 ,little endian 16-bit integer
		'sitemlist' / construct.GreedyBytes,
	)

	stShellItemMRU_data = _DATA_SHELLITEMMRU_STRUCT.parse(data)

	print "-----------------------------------------"
	print "               Shell Item                "
	print "-----------------------------------------"
	print "decode name1            : "+u''.join(unichr(e) for e in stShellItemMRU_data.pname).decode('euc-kr')
	print "decode name2            : "+u''.join(unichr(e) for e in stShellItemMRU_data.pname).decode('cp949')
	print "decode name3            : "+u''.join(unichr(e) for e in stShellItemMRU_data.pname)
	print "decode name4            : "+''.join(unichr(e) for e in stShellItemMRU_data.pname)

	sil = pyfwsi.item_list()

	sil.copy_from_byte_stream(stShellItemMRU_data.sitemlist, ascii_codepage='cp949')

	print "Item Number             : " + str(sil.get_number_of_items())

	for shell_item in iter(sil.items):
		#shell_item : file_entry, root_folder, volume, ...
		#shell_item may include extension_block
		if isinstance(shell_item, pyfwsi.file_entry):
			print "File Entry ITEM(Name)   : " + shell_item.get_name()
			print "  - size: " + str(shell_item.get_file_size())
			print "  - mtime: " + str(shell_item.get_modification_time())

			for extension_block in shell_item.extension_blocks:
				# file_entry_extension: base class - extension_block
				if isinstance(extension_block, pyfwsi.file_entry_extension):
					print"  > long name: " + extension_block.long_name
					print"  > atime: " + str(extension_block.get_access_time())
					print"  > ctime: " + str(extension_block.get_creation_time())

		elif isinstance(shell_item, pyfwsi.root_folder):
			print "Root Folder ITEM"
		elif isinstance(shell_item, pyfwsi.network_location):
			print "Network Location ITEM(Location): " + shell_item.get_location()
		elif isinstance(shell_item, pyfwsi.volume):
			print "volume ITEM(Volume Name): " + str(shell_item.get_name())
	
	print " "
	print " "


clsRegf.close()
