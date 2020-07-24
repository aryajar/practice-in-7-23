while True:
    n = int(input("Enter a number: "))
    if n <0:
        continue
    elif n == 0:
        break
    else:
        print("Square is ", n ** 2)
print("Goodbye")
