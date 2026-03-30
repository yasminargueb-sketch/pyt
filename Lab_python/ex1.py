def InputString():
    while True:
        ch = input("Give a string CH: ")
        valid = True
        for c in ch:
            if not (c.isupper() or c == " "):
                valid = False
                break
        if valid:
            return ch
def Different(ch):
    T = ()
    for c in ch:
        if c != " " and c not in T:
            T = T + (c,)
    return T
def GoldLetter(ch, T):
    words = ch.split()
    Lgold = []

    for letter in T:
        ok = True
        for w in words:
            if letter not in w:
                ok = False
                break
        if ok:
            Lgold.append(letter)

    return Lgold
ch = InputString()
T = Different(ch)
Lgold = GoldLetter(ch, T)

if len(Lgold) == 0:
    print("No gold letter in CH")
else:
    print("The gold letters are:", ", ".join(Lgold))

