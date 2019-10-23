def average_len(record):#function to find average protein length
    totallength = 0#set total length
    for i in enumerate(record):#loop through the list
        totallength=totallength+len(i[1])#add the length of selected protein
    average=totallength/len(record)#creates average of total/quantity
    return average

def average_len_taxa(records,depth):
    #calculates the average length for the top level taxa
    record_by_taxa = {}
    depth=int(depth)-1
    for r in records:
        taxa = r.annotations["taxonomy"]
        string=""
        for x in range(0,depth+1):
            try:
                string=(string+taxa[x]+"-")
            except:
                pass
        record_by_taxa.setdefault(string, []).append(r)
        print(string)

    return {taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}
