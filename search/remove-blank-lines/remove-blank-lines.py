import sys
#OUT FILE

op = input("clear output file ? y/n  \n")

#remove last data evaluation
if op == "y":
    file_formated = open('AFTER-gas-used-last-evaluation.txt', 'w')
    file_formated.write("")
    file_formated.close()

    print("File clear !\n")



print("removing spaces ... !\n")
file_formated = open('AFTER-gas-used-last-evaluation.txt', 'a')

#INPUT FILE
with open("BEFORE-gas-used-last-evaluation.txt") as f:
    for line in f:
        if not line.isspace():
            sys.stdout.write(line)

            file_formated.write(line)     


    file_formated.close()
    print("spaces removed !\n")