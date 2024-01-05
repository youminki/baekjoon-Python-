def permute(data, i, length, result):
    if i == length:
        print(result)
    else:
        for j in range(len(data)):
            result[i]=data[j]
            permute(data, i+1, length, result)

n = 4
k = 2
data = list(range(1, n+1))
result = [0]*k
permute(data, 0, k, result)
