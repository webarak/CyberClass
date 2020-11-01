print ("enter a number with 5 digits")
num = input()
sum = 0
print ("the number that tou enter is {}".format(num))
print("the digits of this number are:", end='')
for digit in num:
    print(digit, end=',')
    sum = sum+int(digit)
print(" ")
print("the sum of the digits is {}".format(sum))
