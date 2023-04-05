import csv
import numpy as np
import matplotlib.pyplot as plt

def plot_data(csv_file_path: str):
    # load data
    results = []
    with open(csv_file_path) as result_csv:
        csv_reader = csv.reader(result_csv, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if row != []:
                results.append([float(el) for el in row])
        results = np.stack(results,axis=1)
    nx, ny = results[0,:], results[1,:]

    # plot precision-recall curve
    plt.scatter(nx,ny)
    plt.ylim([-0.05, 1.05])
    plt.xlim([-0.05, 1.05])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.show()

"""
    | 1 - For some reason the plot is not showing correctly, can you find out what is going wrong?
    | Ans: The problems are that the plot is stacking the data in the csv file in a row-size 1-D dimensional array, hence why showing it with a shape of a regression line,
    | the other problem is that the numbers of the rows in the data are being saved as strings instead of floats, making not plt not recognizing the points depicted and since
    | we are slicing the array through the it's second index, the x and y coordinates end up being switched instead of the correct ones.
    | 2 -  How could this be fixed?
    | Ans: In order to fix this, we must add a loop to convert the elements of the row of the data to a float so that they can be recognized in the plot, define the axis as 1
    | in the np.stack in order to get a column size 2-D array and slice the array through it's first index axis in order to get the correct plot, we desire
"""

f = open("data_file.csv", "w")
w = csv.writer(f)
_ = w.writerow(["precision", "recall"])
w.writerows([[0.013,0.951],
            [0.376,0.851],
            [0.441,0.839],
            [0.570,0.758],
            [0.635,0.674],
            [0.721,0.604],
            [0.837,0.531],
            [0.860,0.453],
            [0.962,0.348],
            [0.982,0.273],
            [1.0,0.0]])
f.close()
plot_data('data_file.csv')