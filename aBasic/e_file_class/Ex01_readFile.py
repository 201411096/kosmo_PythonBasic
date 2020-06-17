"""
@ 파일 읽고 쓰기
    - 파일을 읽고 쓰기 전에 파일을 열어야 한다
    - fileObj = open ( filename, mode )
            mode 첫번째 글자 - 작업 표시
            r(read)  : 파일 읽기
            w(write) : 파일 쓰기 ( 파일이 없으면 생성하고 파일이 있으면 덮어쓴다 )
            x(write) : 파일 쓰기 ( 파일이 없을 때만 생성하고 쓴다 )
            a(append) : 파일 추가 ( 파일이 있으면 파일의 끝에서부터 추가하여 쓴다 )

            mode 두번째 글자 - 파일 타입
            t : 텍스트(text) 타입 ( 기본값 )
            b : 이진(binary) 타입
            두번째 글자가 없으면 텍스트 타입이다.

            encoding='utf-8' : 한글

    - 파일을 열고 사용 후에는 반드시 닫아야 한다
"""
#예시_01
# try:
#     f = open('./data/data.txt', 'r', encoding='utf-8')
# except Exception as e:
#     print('예외발생:', e)
# else:               # 예외가 발생되지 않았을 경우
#     while True:
#         line = f.readline()
#         if not line:    #line에 아무값도 없을 경우
#             break
#         print(line, end='')
#     f.close()
# finally:
#     print('파일처리 종료')
#예시_02
try:
    with open('./data/data.txt', 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:    #line에 아무값도 없을 경우
                break
            print(line, end='')
#except Exception as e:
except FileNotFoundError as e:
    print('예외발생:', e)
finally:
    print('\n종료')
#예시_03
try:
    with open('./data/data.txt', 'r', encoding='utf-8') as f:
        contents = f.read()     #파일 전체를 읽음
        words = contents.split()
        num = len(words)
#except Exception as e:
except FileNotFoundError as e:
    print('예외발생:', e)
else:
    print('총 단어 수 :', num)
finally:
    print('파일 입출력 종료')