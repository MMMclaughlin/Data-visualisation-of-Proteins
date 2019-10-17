

def average_len(record):#function to find average protein length
    print(record)
    totallength = 0#set total length
    for i in range(0,len(record)):#loop through the list
        totallength=totallength+len(record[i])#add the length of selected protein
    average=totallength/len(record)#creates average of total/quantity
    return average

