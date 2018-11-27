

def hash():
    sarray = ["q", "u", "o", "i", "n", "e"] #sample remove
    h = 7
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"] #hide


    i = 0

    while i < len(sarray):
            h = (h * 37 + letters.index(sarray[i]))
            i += 1
    return h


def reverse_hash(): #general function
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z", " "] #dont need String enough

    hash1 = long(1309011123477288991) #64 type long()
    result = ""

    while hash1 > 10:
        difference = hash1 % 37
        result = result + letters[difference] #just index
        hash1 = (hash1 - difference)/37
    #result = result[0:11]
    return result[::-1]


#print(hash())
print(reverse_hash())

#1,0 commit to git internwork
#1.make a importable python module
#2.makeot generic
#3. unit test





