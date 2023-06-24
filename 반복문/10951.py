# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 A+B를 출력한다.
import sys
res = []

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        res.append([a, b])
    except:
        break

for i in range(len(res)):
    print(res[i][0]+res[i][1])