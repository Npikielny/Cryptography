"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

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
    if op == "e":
        m = str(input("Message: "))
        k = str(input("Key: "))
        i = 0
        while len(m) > len(k):
            k += k[i]
            i += 1
    for u in range(0,len(m)):
        if numbChar[m[u]] + numbChar[k[u]] <= len(associations) - 1:
            ouput += charNumb[numbChar[m[u]] + numbChar[k[u]]]
        else:
            ouput += charNumb[(numbChar[m[u]] + numbChar[k[u]]) - (len(associations) - 1)]
    
    else:
        print("meh")
    print(output)
    op = "q"
    """
    op = str(input("Enter e to encrypt, d to decrypt, or q to quit: ")
    while op != "e" and op != "d" and op != "q":
        print("Did not understand command, try again.")
        op = str(input("Enter e to encrypt, d to decrypt, or q to quit: ")
    """