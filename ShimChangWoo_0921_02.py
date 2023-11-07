# 제목: 팩토리얼 계산 문제
# 작성자: 컴퓨터공학부 심창우
# 작성일: 2023.09.21

# 제목: 팩토리얼 계산 문제
# 작성자: 컴퓨터공학부 심창우
# 작성일: 2023.09.21
# 제목: 팩토리얼 계산 문제
# 작성자: 컴퓨터공학부 심창우
# 작성일: 2023.09.21


count_r = 0
count_i = 0

def factorial(n) :
    global count_r
    count_r += 1
    if n == 0 :
        return 1
    else :
        return n * factorial(n - 1)
    
def factorial_iter(n) :
    global count_i
    count_i += 1
    result = 1
    for k in range(n, 0, -1) :
        result = result * k
    return result

n = int(input("정수 n을 입력하세요:"))

print(f"순환 Factorial({n})={factorial(n)} 호출 횟수: {count_r}")
print(f"반복 Factorial({n})={factorial_iter(n)} 호출 횟수: {count_i}")
