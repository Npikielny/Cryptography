"""
cryptography.py
Author: Noah Pikielny
Credit: None

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
charNumb = {}
numbChar = {}
for i in range(0, len(associations)):
    charNumb[associations[i]] = i
    numbChar[i] = associations[i]

op = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
while op != "e" and op != "d" and op != "q":
    print("Did not understand command, try again.")
    op = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))

while op != "q":
    output = ""
    m = str(input("Message: "))
    k = str(input("Key: "))
    i = 0
    while len(m) > len(k):
            k += k[i]
            i += 1
    if op == "e":
        for u in range(0,len(m)):
            if charNumb[m[u]] + charNumb[k[u]] <= len(associations):
                output += numbChar[charNumb[m[u]] + charNumb[k[u]]]
            else:
                output += numbChar[(charNumb[m[u]] + charNumb[k[u]]) - (len(associations))]
        print(output)
    
    else:
        for u in range(0,len(m)):
            if charNumb[m[u]] - charNumb[k[u]] >= 0:
                output += numbChar[charNumb[m[u]] - charNumb[k[u]]]
            else:
                output += numbChar[charNumb[m[u]] - charNumb[k[u]] + len(associations)]
        print(output)
    op = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    while op != "e" and op != "d" and op != "q":
        print("Did not understand command, try again.")
        op = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))

print("Goodbye!")