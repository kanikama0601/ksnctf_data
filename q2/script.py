input_word=input()
for n in range(26):
    for str in input_word:
        for _ in range(n):
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