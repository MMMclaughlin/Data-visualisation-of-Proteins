import matplotlib.pyplot as plt

def plot_bar_show(d):
    ## A list of numbers as long as the elements in d
    r = range(0, len(d))#this loops the amount of bars we will need to make
    ## Prepare a figure
    plt.figure()
    ## Add bars, one at each y position, with the values of d
    plt.barh(r, d.values(),align='edge')
    ## Add labels to the y-axis, with the keys of d
    plt.yticks(r, d.keys())
    ## Show the graph
    plt.show()

def plot_piechart_show(d):
    sum=0
    newlist=[]
    for value in d.values():
        sum=sum+value
    for value in d.values():
        newlist.append(value/sum)
    fig1, ax1 = plt.subplots()
    ax1.pie(newlist, labels=(list(d.keys())),
            shadow=False, startangle=90, autopct='%1.1f%%')
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
