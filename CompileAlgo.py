with open('Human.txt', 'r') as file:
    data = file.read().replace('\n', '')

foundindex = []
foundtrueindex = []

def compile(data): 
    newString = ""
    counter = 1
    prevChar=''
    for index in range(0,len(data),1):
        if(data[index] != prevChar):
            if(index != 0):
                newString = newString+ prevChar+ str(counter)
                counter = 1
        else:
            counter += 1

        if(index == len(data)-1):
            newString = newString+ data[index]+ str(counter)
        
        prevChar = data[index]

    return newString

subsetStr = ""
subsetStr = str(input("Enter a Sequence: ")).upper()

compiledData = compile(data)
compiledSubsetStr = compile(subsetStr) 

def search(compiledData,compiledSubsetStr):
    mainindex=0
    substrindex=0
    trueindex = 0

    for mainindex in range(0,(len(compiledData)-len(compiledSubsetStr)+1)):
        if(mainindex % 2 == 1):
            trueindex+=int(compiledData[mainindex])
        for substrindex in range(0, len(compiledSubsetStr)):

            if(substrindex == 1 or substrindex == len(compiledSubsetStr)-1):
                if(int(compiledData[mainindex+substrindex]) < int(compiledSubsetStr[substrindex])):
                    break
            else:
                if(compiledData[mainindex+substrindex] != compiledSubsetStr[substrindex]):
                    break
            if(substrindex == len(compiledSubsetStr)-1):
                if(int(compiledData[mainindex+1]) > int(compiledSubsetStr[1])):
                    tempIndex = trueindex
                    tempIndex += (int(compiledData[mainindex+1]) - int(compiledSubsetStr[1]))
                    foundtrueindex.append(tempIndex)
                else:
                    foundindex.append(mainindex+1)
                    foundtrueindex.append(trueindex)


search(compiledData,compiledSubsetStr)


print(foundtrueindex)