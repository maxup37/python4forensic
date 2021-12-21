# 시그니처 분석 툴 0.2v

마지막 업데이트 : 2020-08-03

| 작성자 | 날짜 | 내용 |
|:--------:|:--------:|:--------:|
| j4254698 | 2020-07-30 | File Magic Number.md 최초 작성 |
| j4254698 | 2020-08-03 | test_siganal_step8.py 작성 |
| j4254698 | 2020-08-03 | Yara_MSCDF.yara 작성 |
| j4254698 | 2020-08-03 | rule.json 작성 |

* 요약

  **Python**을 이용한 시그니처 분류 목적의 툴입니다.

* 변동내역
  
  File Magic Number.md에서 File Signature 정보를 정리했습니다. [issue #1](https://github.com/maxup37/fparsers_collection/issues/1#issue-668619283)
  
  **2020-08-03** STEP 8 에서 YARA rule 비교 , argument 추가

* 사용방법

  CMD>python **{.py 경로} {Target}**
  
  ex) >python test_siganal_step8.py hwp.hwp
