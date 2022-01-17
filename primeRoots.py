def isPrime(x):
    if x == 1:
        return False
    prime = True
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            prime = False
            break
    return prime

number = int(input())

answer = {}
counter = 2
while not number == 1:
    if isPrime(counter):
        if number % counter == 0:
            if counter not in answer:
                answer[counter] = 1
            else:
                answer[counter] += 1
            number /= counter
        else:
            counter += 1
    else:
        counter += 1

print(answer)
