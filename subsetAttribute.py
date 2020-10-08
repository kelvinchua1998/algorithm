with open('Human.txt', 'r') as file:
    data = file.read().replace('\n', '')

substring = input("Input substring\n>>> ")

substringIndexes = []

def subsetAttribute(substring,data):
    for i in range(0, len(data) - len(substring)+1,1):
        if (data[i] == substring[0] and data[i+len(substring)-1] == substring[-1]):
            for j in range(i+1,i+len(substring)-1,1):
                if data[j] != substring[j-i]:
                    break
                elif (j-i) == (len(substring)-2):
                    substringIndexes.append(i)
                


bryan(substring,data)
print(substringIndexes)