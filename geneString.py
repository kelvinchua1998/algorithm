with open('Human.txt', 'r') as file:
    data = file.read().replace('\n', '')

subset = input("please enter a string:")


subsetIndex = []

count = 0

def recursiveFunction(data, subset):
    global count
    if(subset == ""):
        count += 1
        return True
    elif (data[0] == subset[0]):
        count += 1
        return recursiveFunction(data[1:], subset[1:])
         
    else:
        count += 1
        return False
    
for i in range(0,len(data)-len(subset)+1,1):

    if recursiveFunction(data[i:], subset):
        subsetIndex.append(i)

print(subsetIndex)
print(count)

