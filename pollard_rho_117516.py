#!/usr/bin/env python3

import sys

y = 1018
p = 2
g = 5
Y = y + 1


def zero(x, a, b):
    global x_g
    global a_g
    global b_g
    x_g = x * x % Y
    a_g = a * 2 % y
    b_g = b * 2 % y


def one(x, a):
    global x_g
    global a_g
    x_g = x * p % Y
    a_g = (a + 1) % y


def two(x, b):
    global x_g
    global b_g
    x_g = x * g % Y
    b_g = (b + 1) % y


def caseSwitch(x, a, b):
    if(x % 3 == 0):
        return zero(x, a, b)
    if(x % 3 == 1):
        return one(x, a)
    if(x % 3 == 2):
        return two(x, b)


def zeroU(X, A, B):
    global X_g
    global A_g
    global B_g
    X_g = X * X % Y
    A_g = A * 2 % y
    B_g = B * 2 % y


def oneU(X, A):
    global X_g
    global A_g
    X_g = X * p % Y
    A_g = (A + 1) % y


def twoU(X, B):
    global X_g
    global B_g
    X_g = X * g % Y
    B_g = (B + 1) % y


def caseSwitchU(X, A, B):
    if(X % 3 == 0):
        return zeroU(X, A, B)
    if(X % 3 == 1):
        return oneU(X, A)
    if(X % 3 == 2):
        return twoU(X, B)


def main():
    global p
    global g
    global y
    global Y
    for i in range(1, len(sys.argv)):
        if(sys.argv[i] == "-p"):
            p = int(sys.argv[i + 1])
        if(sys.argv[i] == "-g"):
            g = int(sys.argv[i + 1])
        if(sys.argv[i] == "-y"):
            y = int(sys.argv[i + 1])
    if (p % g == 0):
        print ("Error: g divides p.")
    Y = y + 1

    global x_g
    x_g = 1
    global a_g
    a_g = 0
    global b_g
    b_g = 0
    global X_g
    X_g = x_g
    global A_g
    A_g = a_g
    global B_g
    B_g = b_g
    print("i x a b X A B")
    for i in range(1, y):
        caseSwitch(x_g, a_g, b_g)
        caseSwitchU(X_g, A_g, B_g)
        caseSwitchU(X_g, A_g, B_g)
        print(i, x_g, a_g, b_g, X_g, A_g, B_g)
        if(x_g == X_g):
            print("\n")
            print("\n")
            print("Found equival value at: p^" + str(a_g) + " g^" + str(b_g) +
                  " = " + "p^" + str(A_g) + " g^" + str(B_g) + " = " +
                  str(x_g))
            print("\n")
            break

if __name__ == "__main__":
        main()
