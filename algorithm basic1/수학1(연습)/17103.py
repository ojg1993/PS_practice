#17103

import sys
input= sys.stdin.readline
def main():
    t = int(input())
    nums = [int(input()) for _ in range(t)]
    m = max(nums)
    prime_check = [True] * (m+1)
    
    for i in range(2, int(m**0.5)+1):
        if prime_check[i]:
            for j in range(i*2, m+1, i):
                if prime_check[j]:
                    prime_check[j] = False
    for n in nums:
        ans = 0
        for i in range(2, n//2+1):
            if prime_check[i] and prime_check[n-i]:
                ans += 1
        print(ans)

if __name__ == '__main__':
    main()