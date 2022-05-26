# Deven Maheshwari & Jerry Liang
# Cybersecurity
# Final Project - RC4
# May 31, 2022

import numpy as np
import matplotlib.pyplot as plt
import random

def KSA(key):
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
            answer - byte array to be XOR'ed
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

def main():
    tograph = {}
    for i in range(256):
        for j in range(256):
            help = RGA(2,KSA((256 * i+j).to_bytes(2, "big")))[1]
            if help in tograph: 
                tograph[help] += 1
            else:
                tograph[help] = 1
    fig, ax = plt.subplots()

    ax.bar(tograph.keys(), tograph.values(), width=1, edgecolor="white", linewidth=0.7)

    ax.set(xlim=(-1, 256), xticks=np.arange(1, 8),
    ylim=(0, 100), yticks=np.arange(1, 8))

    plt.show()
    #plt.plot(tograph.keys(), tograph.values())
    #plt.show()


if __name__ == "__main__":
    main()
