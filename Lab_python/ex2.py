def InputString():
    while True:
        ch = input("Give a string CH: ")
        valid = True
        for c in ch:
            if not (c.islower() or c == " "):
                valid = False
                break
        if valid:
            return ch
def InputKey():
    while True:
        key = input("Give the key: ")
        if key.islower():
            return key
def CreateLM(ch, key):
    N = len(key)

    # add spaces
    while len(ch) % N != 0:
        ch += " "

    LM = []
    for i in range(0, len(ch), N):
        LM.append(list(ch[i:i+N]))

    return LM
def Encrypt(ch, key):
    LM = CreateLM(ch, key)
    Ch1 = ""

    for sub in LM:
        for i in range(len(key)):
            Ch1 += sub[i] + key[i]

    return Ch1
def Decrypt(Ch1):
    Ch2 = ""

    # take only characters at even positions
    for i in range(0, len(Ch1), 2):
        Ch2 += Ch1[i]

    return Ch2.rstrip()
ch = InputString()
key = InputKey()

Ch1 = Encrypt(ch, key)
Ch2 = Decrypt(Ch1)

print("Encrypted string:", Ch1)
print("Decrypted string:", Ch2)