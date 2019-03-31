menpref={"V":["A","B","C"],"W":["B","C","A"],"X":["A","B","C"]}
womenpref={"A":["W","X","V"],"B":["X","V","W"],"C":["V","W","X"]}

freemen=list(menpref.keys())
takenwomen=[]

marriage={}

while freemen:
    for man in freemen:
        for woman in menpref[man]:
            if woman not in takenwomen:
                marriage[woman]=man
                freemen.remove(man)
                takenwomen.append(woman)
                break
            else:
                current=marriage.get(woman)
                womanpref=womenpref.get(woman)
                currenti=womanpref.index(current)
                mani=womanpref.index(man)
                if mani<currenti:
                    marriage[woman]=man
                    freemen.remove(man)
                    freemen.append(current)
                    break


print(marriage)
