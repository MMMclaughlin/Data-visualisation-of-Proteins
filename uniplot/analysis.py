records=["adshlkfja","fah","faeopjia","grope"]
def average_len(records):
    totallength=0
    for i in enumerate(records):
        totallength=totallength+len(i[1])
    average=totallength/len(records)
    return average
average_len(records)
