num = 1
#num = int(input('enter number'))
print(num % 10)
print(num//10)
for i in range(1000):
    num = i
    i += 1
    n = len(str(i))
    result = 0
    print(result)
    while i != 0:
        print(i)
        i = i % 10
        result = result+i**n
        i = num//10

    if num == result:
        print(result)
