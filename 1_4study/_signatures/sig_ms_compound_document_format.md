# File Magic Number

### 목차

* [MS Compound Document Format](#ms-compound-document-format)
   + [DOC](#DOC)
   + [PPT](#PPT)
   + [XLS](#XLS)
   + [HWP (v. 5.0)](#hwp-v50)


## [MS Compound Document Format](#목차)

   Ref. <https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-cfb/53989ce4-7b05-4f8d-829b-d08d6148375b>
   
   여러 파일과 디렉토리를 하나의 파일에 저장하는 마이크로소프트의 파일형식이다.

   + **Magic Number**
   
      | Start Position | Other Position | 비고 |
      |:--------:|:--------:|:--------:|
      |  D0 CF 11 E0 A1 B1 1A E1 |  |  Microsoft Office Compound Document File |

   + **관련 파일**

      | Extention | 설명 |
      |:--------:|:--------:|
      | DOC,PPT,XLS 등 | MS Office 97-2003 문서 |
      | HWP | hwp document file v5.00 |
   

## [DOC](#목차)

   Ref. <https://www.inuitor.com/73?category=777967>
   
   + **Magic Number**
   
      | Start Position | Other Position | 비고 |
      |:--------:|:--------:|:--------:|
      |  D0 CF 11 E0 A1 B1 1A E1 | 아래참조 |  Microsoft Office Compound Document File |
   
   + **Other Position**
   
      파일의 임의 위치에 다음과 같은 값이 존재
      
      `4D 53 57 6F 72 64 44 6F 63 00 10 00 00 00 57 6F 72 64 2E 44 6F 63 75 6D 65 6E 74`
   
      위 값은 아래 그림과 같이 존재한다. (정확한 위치는 아직 확인 못함)
      (사진)
      
      
      > [MS-DOC]
      >-	The WordDocument stream MUST be present in the file
      >-	Either the 1Table stream or the 0Table stream MUST be present in the file
      >-	Each storage within the ObjectPool storage contains a stream whose name is "\003ObjInfo" where \003 is the character with value 0x0003
      >-	The Summary Information stream is an optional stream whose name MUST be "\005SummaryInformation", where \005 is the character with value 0x0005, and not the string literal "\005".
      >-	The Document Summary Information stream is an optional stream whose name MUST be "\005DocumentSummaryInformation"
      >-	The Encryption stream is an optional stream whose name MUST be "encryption".
      >-	The Macros storage is an optional storage that contains the macros for the file.
      >-	The XML signatures storage is an optional storage whose name MUST be "_xmlsignatures".
      >-	The signatures stream is an optional stream whose name MUST be "_signatures".
      >-	The Protected Content Stream is an optional stream whose name MUST be "\009DRMContent",


## [PPT](#목차)

   Ref. <https://www.inuitor.com/73?category=777967>
   
   + **Magic Number**
   
     | Start Position | Other Position | 비고 |
     |:--------:|:--------:|:--------:|
     |  D0 CF 11 E0 A1 B1 1A E1 | 아래참조 |  Microsoft Office Compound Document File |
   
   + **Other Position**
   
     파일의 임의 위치에 다음과 같은 값이 존재
     
     `4D 69 63 72 6F 73 6F 66 74 20 4F 66 66 69 63 65 20 50 6F 77 65 72 50 6F 69 6E 74`
     
     (사진)
     
      > [MS-PPT]
      >-	A required stream whose name MUST be "Current User".
      >-	A required stream whose name MUST be "PowerPoint Document".
      >-	An optional stream whose name MUST be "Pictures".
      >-	An optional stream whose name MUST be "\005SummaryInformation"
      >-	An optional stream whose name MUST be "\005DocumentSummaryInformation"
      >-	An optional stream whose name MUST be "EncryptedSummary".
      >-	An optional storage whose name MUST be "_xmlsignatures".
      >-	An optional stream whose name MUST be "\005DocumentSummaryInformation"
      >-	An optional stream whose name MUST be "EncryptedSummary".
      >-	An optional storage whose name MUST be "_xmlsignatures".
      >-	An optional storage whose name MUST be "MsoDataStore".
      >-	An optional stream whose name MUST be "_signatures".


## [XLS](#목차)

   Ref. <https://www.inuitor.com/73?category=777967>

   + **Magic Number**
   
     | Start Position | Other Position | 비고 |
     |:--------:|:--------:|:--------:|
     |  D0 CF 11 E0 A1 B1 1A E1 | 아래참조 |  Microsoft Office Compound Document File |
   
   + **Other Position**

     파일의 임의 위치에 다음과 같은 값이 존재
     
     `4D 69 63 72 6F 73 6F 66 74 20 45 78 63 65 6C`
     
     (사진)
     
      > [MS-XLS]
      >-	Component Object Stream (\001CompObj: \001 = (little endian) 0x01 0x00), The name of this stream MUST be "\001CompObj", A file MUST contain at most one Component Object Stream
      >-	Control Stream (Ctls), The name of this stream MUST be "Ctls". A file MUST contain at most one Control Stream.
      >-	Data Spaces Storage (\006DataSpaces), A file MUST contain at most one Data Spaces Storage.
      >-	Document Summary Information Stream (\005DocumentSummaryInformation), A file MUST contain at most one Document Summary Information Stream.
      >-	Embedding Storage (MBD...), The name of this storage MUST be "MBD" followed by eight hexadecimal digits uniquely identifying the embedded object.
      >-	Encryption Stream (encryption), A file MUST contain at most one Encryption Stream.
      >-	List Data Stream (List Data), A file MUST contain at most one List Data Stream.
      >-	Office Data Store Storage (MsoDataStore), A file MUST contain at most one Office Data Store Storage. 
      >-	…
      >-	Workbook Stream (Workbook), A file MUST contain exactly one Workbook Stream


## [HWP (v.5.0)](#목차)

   Ref. <https://cdn.hancom.com/link/docs/%ED%95%9C%EA%B8%80%EB%AC%B8%EC%84%9C%ED%8C%8C%EC%9D%BC%ED%98%95%EC%8B%9D_5.0_revision1.3.pdf?_ga=2.151887289.1432197376.1595929481-443197701.1595817726>

   + **Magic Number**
   
     | Start Position | Other Position | 비고 |
     |:--------:|:--------:|:--------:|
     |  D0 CF 11 E0 A1 B1 1A E1 | 아래참조 |  Microsoft Office Compound Document File |
   
   + **Other Position**
   
     파일의 임의 위치에 다음과 같은 값이 존재
     
     `48 57 50 20 44 6F 63 75 6D 65 6E 74 20 46 69 6C 65`
     
     
.
