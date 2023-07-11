# syntax error /bugs
# tuna = int(input("what's your fav number?\n"))
# print (tuna)

while True:
    try:
        number = int(input("what's your favorite number\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number")

