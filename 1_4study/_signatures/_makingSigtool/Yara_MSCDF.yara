rule PPT
{
	meta:
		type = "MS Compound Document Format"
		extension = "PPT"
	strings:
		$a = "Microsoft Office PowerPoint"
	condition:
		$a
}

rule DOC
{
	meta:
		type = "MS Compound Document Format"
		extension = "DOC"
	strings:
		$a = "MSWordDoc"
		$b = "Word.Document"
	condition:
		$a and $b
}

rule XLS
{
	meta:
		type = "MS Compound Document Format"
		extension = "XLS"
	strings:
		$a = "Microsoft Excel"
	condition:
		$a
}

rule HWP
{
	meta:
		type = "MS Compound Document Format"
		extension = "HWP"
	strings:
		$a = "HWP Document File"
	condition:
		$a
}
