import math

f = 100
t = float(input("Please enter the value of t to calculate y: "))
a = float(input("Please enter the value of a to calculate y: "))

pi = math.pi
pift = pi * f * t

apift = -a * pift
num1 = math.exp(apift)
s1 = 2 * 10 ** 6
s1pift = s1 * pift
num2 = math.sin(s1pift)
sum = num1 + num2
sqrt = math.sqrt(sum)

a2 = -a + 2
exp = math.exp(a2)
tot = exp * pift
den = math.fabs(tot)

y = sqrt / den

print(f"The value of y is {y:.5f}")

""" Sample output results:
The value of y is 0.22291
"""
