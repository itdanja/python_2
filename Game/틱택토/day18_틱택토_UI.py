
from tkinter import *   #tkinter : 파이썬 UI
from tkinter import messagebox   #메시지 창 제공
import random as r          #난수 생성 함수 제공

# 2. 버튼 함수 만들기
def 버튼( 화면 ) :
    b = Button( 화면 , padx = 1 , bg="papaya whip" , width=3 , text="   " , font=("arial",60,'bold') , relief="sunken" , bd = 10 )
    return b

def 리셋():                #Resets the game
    global 알
    for i in range(3):
        for j in range(3):
                게임판[i][j]["text"]=" "
                게임판[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])

# 5. 이기는수 함수 만들기
def 이기는수() :
    for i in range(3) : # i는 0부터 2까지 1씩 증가 반복
        ################### 가로 이기는 수 ##########################
        if 게임판[i][0]["text"] == 게임판[i][1]["text"] == 게임판[i][2]["text"] == 알 :
            messagebox.showinfo( "게임종료" , 알 + " 플레이어 승리")
            리셋()
        ################### 세로 이기는 수 ##########################
        if 게임판[0][i]["text"] == 게임판[1][i]["text"] == 게임판[2][i]["text"] == 알 :
            messagebox.showinfo("게임종료", 알 + " 플레이어 승리")
            리셋()
    #################### 대각선 이기는수 #########################
    # 0 4 8
    if 게임판[0][0]["text"] == 게임판[1][1]["text"] == 게임판[2][2]["text"] == 알 :
        messagebox.showinfo("게임종료", 알 + " 플레이어 승리")
        리셋()
    # 2 4 6
    if 게임판[0][2]["text"] == 게임판[1][1]["text"] == 게임판[2][0]["text"] == 알:
        messagebox.showinfo("게임종료", 알 + " 플레이어 승리")
        리셋()

# 4. 알 교체 함수 만들기
def 알교체() :
    global 알
    for i in ['O' ,"X"] :  #  O 혹은 X 를 i 에 대입
        if not( i == 알 ) : # 현재 알이  i 와 같지 않으면
            알 = i           # 교체
            break           # 반복문 종료

# 3. 클릭 함수 만들기
def 클릭( 가로 , 세로 ) : # 클릭한 위치를 가져오기
    게임판[가로][세로].config( text =알 , state=DISABLED , disabledforeground = colour[알])
    이기는수() # 이기는수 함수 불러내기 # 승리 판단
    알교체() # 알교체 함수 불러내기 # 알교체
    레이블.config(text = 알 + "님 플레이어 순서입니다 ")

# 화면 화면 설정
화면 = Tk() # window 화면 만들기
화면.title(" 틱택토 게임기 ") # 화면 이름

# 알 만들기
알 = r.choice( [ 'O' , 'X'] )
colour = { 'O':"deep sky blue" , 'X' : "lawn green"} # tkinter Colour 색상 검색

게임판 = [  [  ]  ,  [  ]  ,  [  ]  ] # 2차원 배열
# 2. 2차원 배열에 버튼 넣기
for i in range(3) :   # 가로 단위
    for j in range( 3 ) : # 세로 단위
        게임판[i].append( 버튼(화면))
        게임판[i][j].config( command=lambda row=i , col=j:클릭(row,col) )
        게임판[i][j].grid( row = i , column = j )

# 텍스트[레이블] 만들기
레이블 = Label( text= 알 + "님 플레이어 순서입니다" , font=("arial",15,"bold"))
            # text=" 내용입력 "             , font=("글꼴명",글자크기 , 굵기 )
# 텍스트[레이블] 배치하기  [ 4번쨰 행[가로]에   1번째 열[세로] , 세로 3칸을 병합[합치기]
레이블.grid( row = 3 , column=0 , columnspan=3 )

화면.mainloop() # 화면 반복 실행하기

