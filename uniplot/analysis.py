def average_len(record):#function to find average protein length
    "takes the list of proteans and then finds the average length of them all returning "
    totallength = 0#set total length
    for i in enumerate(record):#loop through the list
        totallength=totallength+len(i[1])#add the length of selected protein
    average=totallength/len(record)#creates average of total/quantity
    return average

def average_len_taxa(records,depth):
    """takes a list of records and a integer to loop up till-> returns a dictionary of each taxa as a key at the given
    depth with a value pair of the average length for that taxa.
    """
    #calculates the average length for the top level taxa
    record_by_taxa = {}
    depth=int(depth)-1#this allows the user to use depth 1 for the highest level which seems normal
    for r in records:#this itterates through all the information
        taxa = r.annotations["taxonomy"]
        string=""
        for x in range(0,depth+1):#this makes the strings of all the connected depth levels eg:
            #Eukaryota-Metazoa-Chordata-Craniata
            try:#this deals with the given depth possibly being longer than a protean is and instead skips that protean
                string=(string+taxa[x]+"-")
            except IndexError:
                pass
        record_by_taxa.setdefault(string, []).append(r)#append the new made string to the list of strings
    return {taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}#return all t
