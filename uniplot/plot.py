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
