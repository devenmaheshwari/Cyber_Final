# Deven Maheshwari & Jerry Liang
# Cybersecurity
# Final Project - RC4
# May 31, 2022

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

    S = []
    for i in range(255):
        S[i] = i
    j = 0
    for i in range(255): 
        j = (j + S[i] + key[i & len(key)]) % 256
        swap(S[i], S[j])

def RGA(iterate):
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
        j = (j + S[i]) % 256
        swap(S[i], S[j])
        K = S[(S[i] + S[j]) % 256]
        return K
        index += 1

