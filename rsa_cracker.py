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
    runTest(1,e,n,P,d,C)

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
    p, q = getPrimeFactors(n)
    phiN = (p-1)*(q-1)
    d = getPrivateKey(e, phiN)
    return d

#returns false if n is divisible by any number x| 2<x<sqrt(n)
def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)): #sqrt(n)+1 because of rounding
        if n%i is 0:
            return False
    return True

#gets the private key using e and phi(n)
def getPrivateKey(e, phiN):
    for i in range(2, phiN):
        if (e*i)%phiN is 1:
            return i
    return (-1)

#runs a single test of the cracking with set e,n,P,d,and C.
def runTest(testNum, e, n, P, d, C):
    #get test values for d, C, and P
    d_prime = crack_rsa(e,n)
    C_prime = rsa_encrypt(P, e, n)
    P_prime = rsa_decrypt(C_prime, d_prime, n)

    print("**************** Test case " + str(testNum) + " ****************")


#returns a tuple of prime factors of a number n
def getPrimeFactors(n):
    p = 1
    for i in range(2, int(math.sqrt(n)+1)):
        if isPrime(i) and n%i is 0: #i is a prime divisor of n
            p = i
            break
    q = n/p
    return (p,int(q))

main()