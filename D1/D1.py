#wordstring ="\"hello\" is the first word written by a programmer in \"hello world\" program. by by"

def remove_punc(wordstring):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in wordstring:
        if ele in punc:
            wordstring = wordstring.replace(ele, "")
    return wordstring

def freq(str): 
    str = str.split()         
    str2 = []
    worddict = {}
  
    for i in str:             
        if i not in str2:
            str2.append(i) 
              
    for i in range(0, len(str2)):
        worddict[str2[i]] = str.count(str2[i])
        #print(str2[i], ":", str.count(str2[i]))
    
    #print(worddict(sorted(worddict.items(), key=lambda t: t[1])))
    worddict_sorted = sorted(worddict.items(), key=lambda t: t[1])

    print("\nWord Frequency in ascending order")
    for i in range(0, len(worddict_sorted)):
        print(worddict_sorted[i][0], ":", worddict_sorted[i][1])


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        wordstring = file.read().replace('\n', '')
    wordstring = remove_punc(wordstring)
    print('Formatted input\n',wordstring)
    freq(wordstring)
    