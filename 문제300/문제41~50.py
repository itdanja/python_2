
# 문제 41 : upper() 함수 : 대문자로 변환 해주는 함수
ticker = "btc_krw"
print( ticker.upper() )

# 문제 42 : lower() 함수 : 소문자로 변환 해주는 함수
ticker = "btc_krw"
print( ticker.lower() )

# 문제 43 : capitalize() 함수 : 첫글자만 대문자로 변환 해주는 함수
ticker = "btn_krw"
print( ticker.capitalize() )

# 문제 44 : endswith() 함수 : 끝나는 문자가 맞는지 확인 함수
file_name = "보고서.xlsx"  # 엑셀 파일
print( file_name.endswith("xlsx") ) # 파일에서 "xlsx" 으로 끝나는지 확인
            # 맞으면 true  아니면 false

# 문제 45 : 문자열이 xlsx' 또는 'xls' 로 끝나는지 확인 함수
file_name = "보고서.xlsx"
print( file_name.endswith( ("xlsx" , "xls") ) )
                        # ("문자" , "문자2")
                        #xlsx 혹은 xls 로 끝나는지 확인

# 문제 46 : startswith() 함수 : 시작하는 문자가 맞는지 확인 함수


