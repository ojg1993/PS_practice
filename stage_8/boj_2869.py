# 2869
import math

a,b,v = map(int, input().split())

d = (v-b) / (a-b)
print(math.ceil(d))

# v-b: 올라가야 하는 거리 
# a-b: 하루에 올라갈 수 있는 거리