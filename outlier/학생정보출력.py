# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # 학생정보출력_난이도 (중)
# #### input으로 학번을 받을 후 개인정보를 출력
# #### 학번을 잘못 입력할 경우 “잘못 입력하였습니다” 출력 후 다시 입력
#     - 학번을 잘못 입력하는 예시 : 21년도 이후 학번, 성별(1,2 제외 다른 숫자), 연생(18세 미만:미성년자), 숫자 7개 초과, s가 3개 이상 등
#
# * 앞에서부터 2번째까지 : 학번
# * 3번째 숫자 : 성별 (1이면 여성, 2이면 남성)
# * 4~5번째 숫자 : 연생 (1970-2003)
# * 6~7번째 숫자 : 학과(00-29 : 컴퓨터학과,30-89 : 정보통계학과,90-99 : 문헌정보학과)
# * 맨 끝에 s가 붙으면 휴학 1년
#     (없는 경우 휴학 경험X, s가 두개인 경우 휴학 2년이며 2년이 최대)
# * 예시 > 1819976, 1819735s

from datetime import datetime


def student():
    print('enter키를 입력하면 종료됩니다.')
    now_year = int(str(datetime.today().year)[2:]) # 현재 년도 저장
    while True:
        try:
            print('-----------------------------------------------------------------')
            sid = input('학번: ')
            
            #year_id
            birth = int(sid[3:5])
            if int(sid[:2]) <= int(now_year):
                year =int(sid[:2])
            else:
                raise ValueError
    
    
            #age
            age =now_year+1-birth if sid[3] == '0' else 100+now_year-1-birth 
        
        
            #sex
            if sid[2] =='1':
                sex = '여성'
            elif sid[2] =='2':
                sex = '남성'
                
                
            #department
            dep = int(sid[5:7])
            if dep >= 0 and dep <30:
                dep = '컴퓨터학과'
            elif dep <90:
                dep = '정보통계학과'
            elif dep <100:
                dep = '문헌정보학과'
            else:
                raise ValueError

                
            #grade & 숫자 개수check
            if sid[7:] == 'ss':   #무조건 9개
                grade = 21-year-1
            elif sid[7:] == 's':  # 무조건 8개
                grade = 21-year
            elif sid[-1] != 's' and len(sid) == 7:  #7개인지 check
                grade = 21-year+1
            else:
                raise ValueError     
                
            #잘못된 성별, 나이, 학년 입력 처리
            if sid[2] not in ['1','2'] or age<=18 or grade >7:
                raise ValueError

                
        except ValueError:
            if sid == '':
                print('종료 됩니다.')
                break      # 잘못된 학번이 입력될 경우 종료
            else : 
                print('잘못 입력하였습니다')
                break 

                
        print("학년 : {}학년\n성별 : {}\n나이 : {}살\n학과 : {}".format(grade, sex, age, dep))

# ## 올바른 학번 입력

student()

# ## 잘못된 학번 입력

student()  #성별 잘못 입력

student()  #학번 잘못 입력

student() #생년 잘못 입력

student() #학과 잘못입력

student() # 휴학 잘못입력

student() # 6학년 초과 예외처리


