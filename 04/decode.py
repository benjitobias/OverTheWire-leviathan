thingy = "01010100 01101001 01110100 01101000 00110100 01100011 01101111 01101011 01100101 01101001 00001010 "

password = ""

# weird exception when run as script to random handling :p

try:

    for i in thingy.split(" "):
        password += chr(int(i, 2))
except:
    pass
print password
