import sys
programsFunction = "a series of numbers that will be rearranged in increasing order"
usersName        = input('What is your name?\n')
playProgram      = input("\nHello "+usersName+",\nWould you be so kind as to provide me with\n"+programsFunction+"?\n")
if 'y' not in playProgram:
    print("Okay then, Bye")
    sys.exit()
else:
    print("Alright then, just give me numbers and stop by giving me\na non numerical character\n")
    A = []
while True:
    try:
        data = int(input("Enter a number: "), 10)
    except ValueError:
        break
    A.append(data)

    ### Algorithm Starts Here ###

for x in range(1,len(A)):
    key = A[x]
    y = x-1
    while(y>=0 and A[y]>key):
        A[y+1] = A[y]
        y = y-1
    A[y+1] = key

    ### Algorithm Ends Here ###

print("Here is the list of numbers you gave me, ordered increasingly\n")
print(A)
end = input("\nOK?")