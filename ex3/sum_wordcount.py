import sys


def print_words(file_name):
    input_file = open(file_name,'r',encoding='utf-8')
    DOfWords = {}
    lines = input_file.readlines()
    for line in lines:
        for word in (line).split():
            if (word in DOfWords):
                DOfWords[word] +=1
            else:
                DOfWords[word] = 1
    for words in DOfWords:
        print (words, ' ', DOfWords[words])



def print_top(file_name):
    input_file = open(file_name, 'r', encoding='utf-8')
    DOfWords = {}
    lines = input_file.readlines()
    for line in lines:
        for word in (line).split():
            if (word in DOfWords):
                DOfWords[word] += 1
            else:
                DOfWords[word] = 1
    for i in range(20):
        maxkey = ""
        maxvalue = 0
        for words in DOfWords:
            if (DOfWords[words]>maxvalue):
                maxvalue = DOfWords[words]
                maxkey = words
        print (maxkey, ' ' ,maxvalue)
        DOfWords.pop(maxkey)




def main():
    print ("enter option:")
    sys.argv.append(input())
    print ("enter file name:")
    sys.argv.append(input())
    if (len(sys.argv) != 3):
        print ("eror")
        sys.exit(1)
    option = sys.argv[1]
    file_name = sys.argv[2]
    if (option == "count"):
        print_words(file_name)
    elif (option == "topcount"):
        print_top(file_name)
    else:
        print ("unknown option {}".format(option))
        sys.exit(1)

if (__name__ == '__main__'):
    main()