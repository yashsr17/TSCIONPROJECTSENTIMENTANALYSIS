def exec(input):
    import re
    
    p = 0
    n = 0
    conv = list(input)
    for i in range(len(conv)) :
        if conv[i] == '.' :
            conv[i] = ' '
    
    
    inputchange = ''.join(conv)
    
    #print(inputchange)

    splits = inputchange.split()
    for t in splits:
        x = t
        x = '^'+x+'$'
        pos = open("C:\\Users\\YASH\\Desktop\\tcsion\\positive-words.txt","r")
        with pos as file:
            for line1 in file:
                for word in line1.split():
                    if re.search(x, word, re.I):
                        p = p + 1
                        #print(word)
        pos.close()
    
    for t in splits:
        x = t
        x = '^'+x+'$'
        neg = open("C:\\Users\\YASH\\Desktop\\tcsion\\negative-words.txt","r")
        with neg as file:
            for line2 in file:
                for word in line2.split():
                    if re.search(x, word, re.I):
                        n = n + 1
                        #print(word)
        neg.close()
    
    #print("Positive cases = "+str(p))
    #print("Negative cases = "+str(n))
    
    total = p + n
    
    chancep = p / total
    chancen = n / total
    
    if p > n:
        print ("It has More Positive Sentiments with chance of %.2f" % round(chancep, 2))
    
    elif n < p:
        print ("It has More Negative Sentiments with chance of %.2f" % chancen)
    
    else:
        print ("It has Neutral Sentiments")
     
    n = str(n)
    p = str(p)
    
    return 0
