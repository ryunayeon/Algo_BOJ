import math

A, I = map(int, input().split())
# 멜로디 수 / 곡 수 = 평균
# A = 곡 수, I = 평균
Real_I = I - 1 + 0.01
Melody = A * Real_I
print(math.ceil(Melody))