

def average_len(record):#function to find average protein length
    totallength = 0#set total length
    for i in enumerate(record):#loop through the list
        totallength=totallength+len(i[1])#add the length of selected protein
    average=totallength/len(record)#creates average of total/quantity
    return average

