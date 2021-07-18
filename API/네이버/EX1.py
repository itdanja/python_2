
# API : 미리 만들어진 코드[ 프로그램 ]
    # 네이버 API

# 1. 네이버 로그인 [ 회원가입 ]
# 2. 네이버에서 네이버 api 검색 => 네이버 개발자센터 [ https://developers.naver.com/main/ ]
# 3. 사이트 메뉴에서 => appilcation => 애플리케이션 등록
    # 1. 애플리케이션 이름 : 아무거나 넣기 [ 파이썬입시 ]
    # 2. 사용 api : 검색
    # 3. 서비스환경 : WEB  => RUL : http://python.com

# 4. 사이트 메뉴 => Documents
# 5. 검색결과는 딕셔너리 호출 된다 [  딕셔너리 데이터 가공 ]
    # 결과 : {  "item" : [검색결과리스트]     }
    # 검색 결과 리스트중 한개당 {  } 묶음


# Documents 파이썬 코드를 복사 해오기
import os
import sys
import urllib.request
import json
import re

# 발급받은 애플리케이션 정보를 변수에 저장
client_id = "2NhHqjjdzUXHBrl_BL33"
client_secret =  "ZRy9I7CWeC"

# 직접 입력해서 검색하기
검색어 = input(" 블로그 검색 : ")
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

# 책 검색
검색어 = input( " 책 검색 : ")
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/book.json?query=" + encText # json 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    검색결과 = response_body.decode('utf-8')  # utf-8 : 한글 지원

    # 검색결과 가공 하기
    json결과=json.loads(검색결과)

    for i in json결과['items'] :
        타이틀 = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
        print( 타이틀 )                        # 엔터 위에 원화기호 특수문자 :  shift+\
else:
    print("Error Code:" + rescode)

# 뉴스 검색
검색어 = input( " 뉴스 검색 : ")
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/news?query=" + encText # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)








