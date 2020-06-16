print('first 모듈 시작')
print('first.py __name__:', __name__)    # __name__ 변수 출력
print('first 모듈 끝')

#파일(first.py)을 직접 실행 시 __name__ 변수의 값은 __main__

#다른 파일에 의해 실행을 하면 __name__ 변수의 값은 파일명으로 나옴