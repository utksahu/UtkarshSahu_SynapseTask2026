import sys
import math
from collections import defaultdict, Counter, deque
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product
from bisect import bisect_left, bisect_right, insort_left, insort_right
from heapq import heapify, heappush, heappop, nlargest, nsmallest
from functools import cache, lru_cache
from math import gcd, lcm, ceil, floor, sqrt, isqrt, factorial, comb, perm, hypot, prod
from string import ascii_lowercase, ascii_uppercase
#sys.setrecursionlimit(300000)
sys.set_int_max_str_digits(0)
input = sys.stdin.readline

s=input().split()
c={'I':0,'T':0,'H':0,'A':0,'C':0}
ans=-1
for i in range(len(s)):
    x=s[i].upper()
    if x in c:
        c[x]+=1
    if c['I']>=1 and c['T']>=1 and c['H']>=1 and c['A']>=2 and c['C']>=1:
        ans=i+1
        break
print(ans)