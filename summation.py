def summationOf(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum

print(summationOf(1,2,3))