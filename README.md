# Cyber_Final
Stuyvesant Cybersecurity 2022: Final Project

Deven Maheshwari & Jerry Liang

## Description
We will be tackling the RC4 (Rivest Cipher) stream cipher. The RC4 Cipher is known for its speed and security. We will be writing an encoder and decoder. It functions by using random a key scheduling algorithm and a random generation algorithm as well as the XOR function to produce cipher-text.

## Directions
This project contains files to encode, decode, and find the insecurities associated with the RC4 cipher.
Insecurities, in this case, refer to the drawbacks of this cipher which can be learned about in the presentation linked below.

#### Steps to Success:
1. cd into the /source subdirectory
2. Download any dependencies with 
```$pip3 install -r code/requirements.txt```
3. Configure your plaintext and keyfile
    To encode: 
    ```$make encode ARGS="plaintextfile keyfile outputfile"```  
    To decode: 
    ```$make decode ARGS="ciphertextfile keyfile outputfile"``  
    To analyze the issues with RC4: 
    ```$make insecurities"```  


## Links
[Presentation](https://github.com/devenmaheshwari/Cyber_Final/blob/main/PRESENTATION.md)  
[Homework](https://github.com/devenmaheshwari/Cyber_Final/blob/main/HOMEWORK.md)
