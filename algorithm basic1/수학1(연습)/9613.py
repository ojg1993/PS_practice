# 9613

import math
from itertools import combinations
import sys
input = sys.stdin.readline

# combinations를 활용한 풀이(2중 반복문...?)

for i in range(int(input())):
    nums = list(map(int, input().split()))
    tot = 0
    for combi in combinations(nums[1:], 2):
        if math.gcd(combi[0], combi[1]):
            tot += math.gcd(combi[0], combi[1])
    print(tot)

# 브루트포스를 활용한 풀이(2중 반복문)

for i in range(int(input())):
    nums = list(map(int, input().split()))
    tot = 0
    for j in range(1, len(nums)):
        for k in range(j+1, len(nums)):
            tot += math.gcd(nums[j],nums[k])
    print(tot)

# 제출 결과 메모리와 시간[O(n^2)]이 두 방법 모두 같았다.
# 곰곰히 생각해보니 combinations 함수를 호출과 동시에 combination을 구하기 위한 for문이
# 함수에 내장되어 돌아가는것을 떠올릴 수 있었다.
