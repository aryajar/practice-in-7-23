x = float(input("Enter a number: "))
n = fenmu = 1
result = 1.0
while n <= 100:
    fenmu *= n
    result += float(pow(x, n)/fenmu)
    n += 1
    if (pow(x, n)/fenmu)<0.0001:
        break
print("No of Times= {}, Sum= {}".format(n, result))
