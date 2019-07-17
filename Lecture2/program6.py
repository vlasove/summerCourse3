import re


top_words = {}
summary = []
hand = open("example.txt")
for line in hand:
    line = line.rstrip()
    #COMMENT : MAGIC CODE!! DONT TOUCH!
    y = re.findall("[0-9]+", line)
    #print(y)
    if len(y) != 0:
        for i in y:
            summary.append(int(i))
    continue

    words = line.split()
    for word in words:
        if word in top_words.keys():
            top_words[word] +=1

        else:
            top_words[word] = 1

#for k,v in top_words.items():
    #print("Key:  %s ------ Value:  %s"%(k,v))
print(sum(summary))