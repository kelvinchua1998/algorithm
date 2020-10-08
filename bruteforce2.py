with open('Human.txt', 'r') as file:
    data = file.read().replace('\n', '')

subsetStr = ""
subsetStr = str(input("Enter a Sequence: ")).upper()

foundindex = []
mainindex = 0
substrindex = 0
for mainindex in range(0,(len(data)-len(subsetStr)+1)):
    for substrindex in range(0, len(subsetStr)):
        if(data[mainindex+substrindex] != subsetStr[substrindex]):
            break
        if(substrindex == len(subsetStr)-1):
            foundindex.append(mainindex)

print(str(foundindex))
print(len(foundindex))
        





