def median(numbers):
    numbers.sort()
    Midindex = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[Midindex]
    else:
        return(numbers[Midindex] + numbers[Midindex - 1])/2

def mean(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

def mode(numbers):
    result = numbers[0]
    count = 0
    for num in numbers:
        if numbers.count(num) >= count:
            count = numbers.count(num)
            result = num
    return result

def main():
    UserList = [4, 6, 9, 3, 10, 8]
    print("List:", UserList)
    print("Mode:", mode(UserList))
    print("Median:", median(UserList))
    print("Mean:", mean(UserList))


main()
