def ExtractNumber(ID):
    num = ""
    for i in range(len(ID)-1, -1, -1):
        if ID[i].isdigit():
            num += ID[i]

    if num == "":
        return 0
def SumDigits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
    return int(num)
def PromotionCode(ID):
    n = ExtractNumber(ID)

    if n == 0:
        return 0

    code = 0
    temp = n

    while temp > 0:
        code += SumDigits(temp)
        temp //= 10

    return code
def Winner(customers):
    max_code = -1
    winner = ""

    for ID in customers:
        code = PromotionCode(ID)

        if code > max_code:
            max_code = code
            winner = ID

    return winner, max_code
N = int(input("Enter number of customers: "))

customers = []
for i in range(N):
    ID = input("Enter ID: ")
    customers.append(ID)

winner, code = Winner(customers)

print("Winner ID:", winner)
print("Promotion Code:", code)