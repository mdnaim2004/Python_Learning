def sum(num1, num2, num3=0, num4=0, num5=0):
    res = num1+num2+num3+num4+num5
    return res


total = sum(99, 11, 7, 9)
print("The sum is = ", total)


# args

def all_sum(num1, num2, *numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum = sum+num
    return sum


total = all_sum(45, 56, 56, 34, 78, 12)
print("all_sum:", total)


# variable numbers of parameters
def do_a_lot(*args):
    print(args)



def a_lot(num1, num2):
    sum = num1+num2
    mult = num1 * num2
    sub = num1 - num2

    return sum, mult, sub
    # return [sum, mult, sub]
everything = a_lot(55, 21)
print(everything)