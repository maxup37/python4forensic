# Making File Signature Detector for Study

마지막 업데이트 : 2020-08-03 (WORKING)

| 작성자 | 날짜 | 내용 |
|:--------:|:--------:|:--------:|
| j4254698 | 2020-07-30 | File Magic Number.md 최초 작성 |
| j4254698 | 2020-08-03 | test_siganal_step8.py 작성 |
| j4254698 | 2020-08-03 | Yara_MSCDF.yara 작성 |
| j4254698 | 2020-08-03 | rule.json 작성 |

## 요구 사항 정의
* Header detection: python으로 구현
* Body, footer detection: yara 사용
* Header 탐지 후 Body와 Footer를 탐지하도록 구현한다.
* Signature rule은 json 형식으로 작성
* Signature rule을 메모리로 읽어들일 때 Tree 구조를 형성하도록 한다.

## JSON file specification
'''
  [
    {
      ""type": /* file type:string, ex) "jpeg/jfif" */,
      "extension": /* file extention:string, ex) "jpg" */,
      "offset": /* start position:integer, ex) 0 */,
      "signature": /* signature: hexadecimal string, ex) "FF D8 FF E0 xx xx 4A 46 49 46" */
     },
     ...
  ]
'''

## Troubleshooting

2019.04.19
* Yara python이 windows python 3.7 install 버전이 없음
* 따라서 3.6 버전의 python 사용
