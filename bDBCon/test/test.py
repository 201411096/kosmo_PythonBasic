import re
# def pwd_check(pwd):
#     reg=re.compile('[A-Z]+[a-zA-Z0-9]{6,10}$')
#     result=reg.search(pwd)
#     if result==None:
#         print('아님')
#         return
#     else:
#         print('맞음')
#         return
#
# pwd_check('abcdE') # 길이오류
# pwd_check('abcdef') # 대문자 포함하지 않아 오류
# pwd_check('aBcdef2') # 성공
# pwd_check('bBcdef_2') # 특수문자 포함



def pwd_check(pwd):
    p = re.search('^(?=.*[A-Z]).[A-Za-z0-9]{6,10}$',pwd)
    if p:
        return print(True)
    else:
        return print(False)


pwd_check('abcdE') # 길이오류
pwd_check('abcdef') # 대문자 포함하지 않아 오류
pwd_check('abCdef2') # 성공
pwd_check('Abcdef_2') # 특수문자 포함