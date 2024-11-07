change=1
print("Enter the text")
text = input()

for j in range(26):
    for str in text:
        for i in range(j):
            if str == " ":
                str = " "
            elif str == "Z":
                str = "A"
            elif str == "z":
                str = "a"
            else:
                str = chr(ord(str) + 1)
        print(str,end="")
    print("\n\n")