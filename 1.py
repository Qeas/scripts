def primeProducts(numbers):
    res = []
    for i in range(len(numbers)):
        prev = 0
        res.append(numbers[i])
        for j in range(i + 1, len(numbers)):
            if prev:
                res.append(numbers[j] * prev)
            prev = numbers[i] * numbers[j]
            res.append(prev)
    return res

numbers = [2,3,5,7]
pn = primeProducts(numbers)
print(pn)
