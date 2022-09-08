import math

message = int(input("Enter the message to be encrypted: ")) 

"""p = 11
q = 7
e = 3"""
p = int(input("Enter the p: ")) 
q = int(input("Enter the q: ")) 
e = int(input("Enter the e: ")) 

n = p*q

def encrypt(me):
    en = math.pow(me,e)
    c = en % n
    print("Encrypted Message is: ", c)
    return c

print("Original Message is: ", message)
c = encrypt(message)
