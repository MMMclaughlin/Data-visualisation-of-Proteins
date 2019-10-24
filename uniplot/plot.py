import matplotlib.pyplot as plt

def plot_bar_show(d):
    """takes the dictionary to get the values of each unique protean and plot the barchart."""
    ## A list of numbers as long as the elements in d
    r = range(0, len(d))#this loops the amount of bars we will need to make
    ## Prepare a figure
    plt.figure()
    ## Add bars, one at each x position, with the values of d
    plt.bar(r, d.values())
    ## Add labels to the x-axis, with the keys of d
    plt.xticks(r, d.keys(),rotation=90)
    plt.tight_layout(w_pad=0.5)
    plt.xlim(xmax=20)
    ## Show the graph
    plt.show()

def plot_piechart_show(d):
    """takes the dictionary to get the values of each unique protean and plot the piechart."""
    sum=0
    newlist=[]
    for value in d.values():#finds the total amount
        sum=sum+value
    for value in d.values():#gives a percentage of total amount to each value
        newlist.append(value/sum)
    #creates pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(newlist, labels=(list(d.keys())),
            shadow=False, startangle=90, autopct='%1.1f%%')
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()
    plt.show()
