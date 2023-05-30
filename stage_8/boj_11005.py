# 11005

n, b = map(int, input().split())


convert = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ''

while n:
    ans += convert[n%b]
    n //= b

print(ans[::-1])

'''
이번 문제는 요구하는 사항이 이해되지 않아 고민했고, 예시를 찾아보고 정답을 도출했다.

해법은 생각보다 간단했으며 아래와 같다.

1. 진법은 최소 2부터 최대 36까지이니, 36진법 string을 convert 변수에 저장한다.
2. 진법 산술에 따라 저장할 정답을 ans 변수에 empty string으로 저장한다.
3. n이 True일때 작동하는 while 반복문을 만들어 n%b로 값을 covert에서 인덱싱하여 ans변수에 append한다.
4. n//b의 값을 n으로 저장한다.
5. 3~4를 반복한다.
6. ans를 역순으로 출력한다.
'''