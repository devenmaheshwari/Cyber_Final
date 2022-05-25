# Deven Maheshwari & Jerry Liang
# Cybersecurity
# Final Project - RC4
# May 31, 2022

import numpy as np
import sys

def KSA(key):
    """
    KSA - Key Scheduling Algorithm in order to create an array of byte values to be used in RGA for encoding.
        Arguments:
            key - string
        Algorithm:
            Initializes an array of length 256 to represent the number of bytes available for key encoding then
            switches values within the array using the key length and key length in bytes.
        Return:
            S - byte array
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

def KSA_byte(key):
    """
    KSA - Key Scheduling Algorithm in order to create an array of byte values to be used in RGA for encoding.
        Arguments:
            key - bytes
        Algorithm:
            Initializes an array of length 256 to represent the number of bytes available for key encoding then
            switches values within the array using the key length and key length in bytes.
        Return:
            S - byte array
    """

    S = [i for i in range(256)]
    key_array = bytearray(key)
    j = 0
    for i in range(256):
        j = (j + S[i] + key_array[i % len(key_array)]) % 256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
    return S

def RGA(iterate, arr):
    """
    RGA - Random Generation Algorithm in order to generate a bit array to be XOR'ed with the plaintext
        Dependencies:
            KSA(key) to get the permutation array of byte encoding of the key
        Arguments:
            iterate - number of values to be generated in the bit array
            arr - the identity permutation from the KSA
        Algorithm:
            For iternates number of times, adds S[i] to j and swaps S[i] with S[j] and uses a separate value
            from S fm the keystream.
        Return:
            answer - bit array to be XOR'ed
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


def encoder(plaintext, key):
    """
    Encoder
        Dependencies:
            KSA(key) to get the permutation array of byte encoding of the key
            RGA to generate XOR array
        Arguments:
            plaintext - string
            key - string
        Algorithm:
            Uses KSA and RGA and XOR's the plaintext with the generated array to produce the ciphertext.
        Return:
            ciphertext - bit array
    Does not function. Meant as organizational code since strings are innately ascii. 
    """

    plaintext_array = bytearray(plaintext.encode())
    keystream = RGA(len(plaintext_array), KSA(key))
    ciphertext = []
    for i in range(len(plaintext_array)):
        ciphertext.append(plaintext_array[i] ^ keystream[i])
    return bytearray(ciphertext)

def file_encoder(plaintext_file, key_file, output_name):
    """
    Encoder for files
        Dependencies:
            KSA(key) to get the permutation array of byte encoding of the key
            RGA to generate XOR array
        Arguments:
            plaintext_file - file
            key_file - file
            output_name - file to be written to with ciphertext
        Algorithm:
            Uses KSA and RGA and XOR's the plaintext with the generated array to produce the ciphertext.
    """

    plaintext = open(plaintext_file, "rb")
    key = open(key_file, "rb")
    output_file = open(output_name, "wb")

    plaintext_array = bytearray(plaintext.read())
    keystream = RGA(len(plaintext_array), KSA_byte(key.read()))

    for i in range(len(plaintext_array)):
        output_file.write((plaintext_array[i] ^ keystream[i]).to_bytes(1, "big"))
    plaintext.close()
    key.close()
    output_file.close()

def main():
    try:
        filename = file_encoder(sys.argv[1], sys.argv[2], sys.argv[2])
    except:
        print("Incorrect Arguments")

if __name__ == "__main__":
    main()
