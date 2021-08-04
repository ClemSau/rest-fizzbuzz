def my_fizzbuzz(int1: int, int2: int, limit: int, string1: str, string2: str):
    response = []
    for i in range(1, limit + 1):
        if i % int1 == 0 and i % int2 == 0:
            response.append(string1 + string2)
            continue
        elif i % int1 == 0:
            response.append(string1)
            continue
        elif i % int2 == 0:
            response.append(string2)
            continue
        else:
            response.append(i)

    return response
