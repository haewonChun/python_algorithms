# 0. arithmetic operator

## precedence
print(6*3/4 + (-3*+2//-2)**4)     # 85.5

## 문자열 뺄샘, 나눗셈은 허용되지 않음

## logical operator
### and, or, not 
print(2 and 0)                    # 0
print(2 and not(0))               # True
print(not 2)                      # False
print(not 0)                      # True

## ex.
print(2 * (3+4)//2)               # 7
print(2+3 > 5 == 2)               # False
print(2**2 < 4 or 2 != 1+1)       # False
a = 10
a**= 2+1
print(a)                          # 1000



# 1. input and output

## print 
### 1. str.format()
print("pi={0:7.4f}:\t name={1:10s}, age={2:2d}\n".format(3.14390340, "hyewon", 27))         # pi= 3.1439:      name=hyewon    , age=27

### 2. %
print("pi=%5.4f:\t name=%+10s, age=%2d\n" %(3.14390340, "hyewon", 27))                      # pi=3.1439:       name=    hyewon, age=27



# 2. conditional statement

## ax**2+bx+c = 0
import math

def quadratic_formula(a, b, c):
    if a == 0:
        anw = c/b
    else:
        X1 = (-b+math.sqrt(b**2-4*a*c))//2*a
        X2 = (-b-math.sqrt(b**2-4*a*c))//2*a
        anw = list(set((X1, X2)))

    return anw

ABC = input()
a, b, c = ABC.split()
anw = quadratic_formula(int(a), int(b), int(c))
print(anw)


# 3. loop and list

## while
x = 1
a = 0
while x <= 10:
    a = a + x
    x = x + 1
print(a)                                    # 55

## list
# 음수 인덱스의 좋은 점 : list의 끝을 기준으로 접근 가능

## repetition
b = [2, 3]*2
print(b)                                    # [2, 3, 2, 3]

## slicing
a = [0, 1, 2, 3, 4, 5, 6, 7]
a[1] = [10, 20, 30]
print(a)                                    # [0, [10, 20, 30], 2, 3, 4, 5, 6, 7]

a = [0, 1, 2, 3, 4, 5, 6, 7]
a[1:2] = [10, 20, 30]
print(a)                                    # [0, 10, 20, 30, 2, 3, 4, 5, 6, 7]


# ex.
## 1


