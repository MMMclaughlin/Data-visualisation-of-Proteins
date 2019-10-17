

def average_len(record):#function to find average protein length
    totallength = 0#set total length
    for i in enumerate(record):#loop through the list
        totallength=totallength+len(i[1])#add the length of selected protein
    average=totallength/len(record)#creates average of total/quantity
    return average

def average_len_taxa(records):
    #calculates the average length for the top level taxa
    record_by_taxa = {}
    for r in records:
        taxa = r.annotations["taxonomy"][0]
        record_by_taxa.setdefault(taxa, []).append(r)

    return {taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}
