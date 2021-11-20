s = list(input())
count = 0
for i in range(len(s)):
    if s[i]=="=":
        if s[i-1]=="c" or s[i-1]=="s":
            continue
        if s[i-1]=="z":
            if s[i-2]=="d":
                count-=1
            else:
                continue
        else:
            count+=1

    elif s[i]=="-":
        if s[i-1]=="c" or s[i-1]=="d":
            continue
        else:
            count+=1
    
    elif s[i]=="j":
        if s[i-1]=="l" or s[i-1]=="n":
            continue
        else:
            count+=1
    else:
        count+=1
print(count)
