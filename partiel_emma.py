def sommult(limit):
    i = 0
    j = 0
    result = 0
    while i < limit:

        i += 3
        result += i
    while j < limit:

        j += 5
        result += j
    return result


def friends(n1, n2):
    sommef1 = 0
    sommef2 = 0
    for i in range(1, n1 + 1):
        if n1 % i == 0:
            sommef1 += i
    for i in range(1, n2 + 1):
        if n2 % i == 0:
            sommef2 += i
    print(sommef1, sommef2)
    if sommef1 == sommef2:
        return 1
    else:
        return 0


dict = {"a": "win"}
score = 0
for key in dict:
    if dict[key] == "nul":
        score += 1
    if key == "win":
        score += 3
return score