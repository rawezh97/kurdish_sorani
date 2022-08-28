file = open("kurdword.txt" , "r")
gg = file.read()
word = gg.split(" ")
print (word)

f = open("test.txt" , "w+")
for i in word:
    if len(i) == 1 :
        pass
    else:
        f.write(i+"\n")
