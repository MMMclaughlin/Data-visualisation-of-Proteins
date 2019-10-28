def average_len(record):#function to find average protein length
    "takes the list of proteans and then finds the average length of them all returning "
    totallength = 0#set total length
    for i in enumerate(record):#loop through the list
        totallength=totallength+record[i[0]]#add the length of selected protein
    average=totallength/len(record)#creates average of total/quantity
    return average

def average_len_taxa(records,depth):
    """takes a list of records and a integer to loop up till-> returns a dictionary of each taxa as a key at the given
    depth with a value pair of the average length for that taxa.
    """
    record_by_taxa={}
    print(records)
    for i in enumerate(records):#records calls the generator and generates the next value each call
        #i is the info of each protean
        string = ""
        for x in range(0,int(depth)):  #this makes the strings of all the connected depth levels eg:
            try:  #this deals with the given depth possibly being longer than a protean is and instead skips that protean
#this selects the list within the tuple returned by the generator within the tuple returned enumerate
                string=(string+i[1].annotations["taxonomy"][x]+"-")
            except IndexError:
                pass
        record_by_taxa.setdefault(string, []).append(len(i[1]))#append the new made string to the list of strings
    return {taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}#return the dictionary key value pairs
