def isnum(num):
    isnumber = False
    for digit in num:
        if (not digit.isalpha()):
            isnumber = True
        else:
            return False
    return isnumber

print ("enter a number with 5 digits")
num = input()
stop = 0
while (stop==0):
    if (len(num)==5 and isnum(num)):
        sum = 0
        print ("the number that tou enter is {}".format(num))
        print("the digits of this number are:", end='')
        for digit in num:
            print(digit, end=',')
            sum = sum+int(digit)
        print(" ")
        print("the sum of the digits is {}".format(sum))
        stop=stop+1
    else:
        print("enter a number with 5 digits")
        num = input()