with open("naw.txt","r") as file:
    datas=[]
    for line in file:
        datas.append(line.split())
    for data in datas:
        try:
            if int(data[0])>m:
                m=data[0]
            if int(data[1])>m:
                m=data[1]
        except:
            pass
    file.close()
    
maxmin_combinations=lambda brackets: sum([2**i for i in range(1,len(brackets)+1)])
    
def check_corecting(brackets):
    no_par=[]
    depth=0
    #print(brackets,"sansss")
    dic={"(":0,")":0}
    
    for bracket in brackets:
        
        if bracket=="(":
            no_par.append("(")
            dic["("]+=1
        else:
            try:
                no_par.remove("(") 
                dic[")"]+=1
            except:
                return False,None
        if depth<len(no_par):
            depth=len(no_par)
    if dic["("]!=dic[")"]:
        return False,None
    return True,depth

def maxmin(brackets,expected_depth):
    if brackets[0][0]!=(len(brackets[1][0])/2):
        brackets[0][0]=(len(brackets[1][0])/2)
        
    expected_depth=expected_depth%(len(brackets[1][0])/2)
    
    expected_depths=["",float("inf")]
    #binary = f'{int(0, 2):0{len(brackets)}b}'
    numer=0
    for i in range(1,maxmin_combinations(brackets[1][0])+1):
        numer+=1
        test_brackets=""
        for i in str(bin(numer)[2:].zfill(len(brackets[1][0]))):
            if int(i)==0:
                test_brackets+="("
            elif int(i)==1:
                test_brackets+=")"
        #print(bin(numer)[2:].zfill(len(brackets[1][0])))
        #print(test_brackets,"str!")
        #print(check_corecting(test_brackets),test_brackets,brackets[0][1])
        if check_corecting(test_brackets)==(True,int(brackets[0][1])):
            points=0
            #print(len(brackets[1][0]))
            #print(test_brackets,"hmm")
            for j in range(len(brackets[1][0])):
                if brackets[1][0][j]!=test_brackets[j]:
                    points+=1
            if points<expected_depths[1]:
                expected_depths[1]=points
                expected_depths[0]=test_brackets
    return expected_depths
    
print(maxmin(datas,2))