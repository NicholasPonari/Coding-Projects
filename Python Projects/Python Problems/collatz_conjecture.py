def steps(number, count = 0):
    if number > 1:
        if number % 2 == 0:
            number = number/2
            count += 1
            return steps(number, count)
        else:
            number = (number * 3) + 1
            count += 1
            return steps(number, count)
    elif number == 1:
        return count
    else:
        raise ValueError("Only positive integers are allowed")