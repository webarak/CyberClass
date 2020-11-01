import sys
def ex1():
    sentence = input("enter a sentence")
    print ('.'.join(sentence.split(' ')))

def ex2():
    num = input("enter a number")
    sum = 0
    multiply = 1
    for i in range(len(num)):
        sum = sum + int(num[i])
        multiply = multiply*int(num[i])
    print("the sum of the digits in {summ} and the multiply is {multi}".format(summ=sum, multi=multiply))

def ex3():
    list = (input("enter a list of numbers")).split()
    sum = 0
    for i in range(len(list)):
        sum = sum + int(list[i])
    avg = sum/len(list)
    print(avg)

def ex4():
    list = (input("enter a list of words")).split()
    sentence = ""
    for i in range (len(list)):
        sentence = sentence + list[i]
    print(sentence)

def ex5():
    str = input("enter string")
    newstr = ('').join(('').join(('').join(('').join((('').join(str.split('e'))).split('a')).split('u')).split('i')).split('o'))
    print (newstr)

def ex6():
    list = (input("enter a list of words")).split()
    min = int(sys.maxsize)
    place = 0
    for word in range (len(list)):
        if (len(list[word])<min):
            min = len(list[word])
            place = word
    print (list[place])

def ex7():
    str = input("enter string")
    newstr = ""
    a = 1
    for i in range(len(str)):
        newstr = newstr + str[-a]
        a = a +1
    print(newstr)

ex1()
ex2()
ex3()
ex4()
ex5()
ex6()
ex7()
