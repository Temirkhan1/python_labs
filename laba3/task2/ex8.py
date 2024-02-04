#ex8
def figna(listik1) :
    emptyy = []
    for i in listik1 :
        if i == 0 or i == 7 :
            emptyy.append(i)


    for element in range(len(emptyy)) :
        if (emptyy[element] == 0 and emptyy[element+1] == 0 and emptyy[element+2] == 7) :
            print("True")
    return False

figna([1,2,3,0,1,2,1,0,7])
