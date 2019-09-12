"""
Author: Andrew Brodhead
Class: Computer Security CPSC448-01
Date: Sept 19, 2019
Description:
Usage: python3 rsa_cracker.py

"""
import math

# main loop for running program
def main():
    e = 7
    n = 33
    d = 3
    P = 5
    C = 14
    print(rsa_encrypt(P,e,n))
    print(rsa_decrypt(C,d,n))

#uses a public key 'e' to encrypt plaintext into ciphertext
def rsa_encrypt(plaintext, e, n):
    #C = P^e mod n
    return (math.pow(plaintext, e))%n

#uses a private key 'd' to decrypt ciphertext into plaintext
def rsa_decrypt(ciphertext, d, n):
    #P = C^d mod n
    return (math.pow(ciphertext, d))%n

#cracks the rsa encryption and returns private key d
def crack_rsa(e, n):
    pass

#returns false if n is divisible by any number x| 2<x<sqrt(n)
def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)): #sqrt(n)+1 because of rounding
        if n%i is 0:
            return False
    return True

#gets the private key using e and phi(n)
def getPrivateKey(e, phiN):
    pass

main()