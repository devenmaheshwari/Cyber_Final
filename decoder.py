# Deven Maheshwari & Jerry Liang
# Cybersecurity
# Final Project - RC4
# May 31, 2022

import numpy as np

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
        Dependencies:
            KSA(key) to get the permutation array of byte encoding of the key
        Arguments:
        Algorithm:
        Return:
    """

    i = 0
    j = 0
    index = 0
    answer = []
    while index < iterate:
        i = (i + 1) % 256
        j = (j + arr[i]) % 256
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        k = arr[(arr[i] + arr[j]) % 256]
        answer.append(k)
        index += 1
    return answer

def decoder(plaintext, key):
    plaintext_array = bytearray(plaintext.encode())
    keystream = RGA(len(plaintext_array), KSA(key))
    ciphertext = []
    for i in range(len(plaintext_array)):
        ciphertext.append(plaintext_array[i] ^ keystream[i])
    return ciphertext

def main():
    test = (KSA("Key"))
    print(test)
    print('-----------------------------------')

    test1 = RGA(5, test)
    print(test1)
    print('-----------------------------------')

    print(encoder("Plaintext", "Key"))

if __name__ == "__main__":
    main()
