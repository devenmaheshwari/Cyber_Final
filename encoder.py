# Deven Maheshwari & Jerry Liang
# Cybersecurity
# Final Project - RC4
# May 31, 2022

import numpy as np

def swap(one, two): 
    temp = one
    one = two
    two = temp

def KSA(key):
    """
    KSA 
        Arguments:
        Algorithm: 
        Return:
    """

    S = [i for i in range(256)]
    key_array = bytearray(key, 'utf-8')
    j = 0
    for i in range(256): 
        j = (j + S[i] + key_array[i % len(key_array)]) % 256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
    return S

def RGA(iterate, arr):
    """
    RGA
        Arguments:
        Algorithm: 
        Return:
    """

    i = 0
    j = 0
    index = 0
    while index <= iterate:
        i = (i + 1) % 256
        j = (j + arr[i]) % 256
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        k = arr[(arr[i] + arr[j]) % 256]
        index += 1
        return k

def main():
    test = (KSA("test1"))
    print(test)
    print('-----------------------------------')
    print(RGA(5, test))

if __name__ == "__main__":
    main()