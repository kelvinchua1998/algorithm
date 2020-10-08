with open('Human.txt', 'r') as file:
    data = file.read().replace('\n', '')

substring = input('Txt\n>>>')

substringindex = []

def KMPSearch(data, substring):
    dlen = len(data)
    sublen = len(substring)

    lps = [0] * sublen
    j = 0
    computeLPSArray(substring, sublen, lps)

    i = 0
    while i < dlen:
        if substring[j] == data[i]:
            i += 1
            j += 1

        if j == sublen:
            substringindex.append(i-j)
            print("Found pattern at index " + str(i - j))
            j = lps[j - 1]

        elif i < dlen and substring[j] != data[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def computeLPSArray(substring, sublen, lps):
    len = 0
    lps[0]
    i = 1

    while i < sublen:
        if substring[i] == substring[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


KMPSearch(data, substring)
print(substringindex)