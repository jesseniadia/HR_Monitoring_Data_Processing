"""
The main Python module that combines cleaner and metrics functions in order to perform comprehensive analysis.
"""
from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits
import matplotlib.pyplot as plt

def run(filename: str) -> tuple:
    """
    Process heart rate data from the specified file, clean it, calculate metrics and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, max, and standard deviation
    """ 
    data = []

    #open file using file I/O and read it into the `data` list
#f = open('data\phase0.txt, r')
#print(f.read())
#f.close()
    
    with open(filename,"r") as f:
        data = f.readlines()
    #print(data)

#Use `filter_nondigits` to clean the data and remove invalid entries, convert to intergers and remove non-numeric values from the list save the output to a new variable
    
    filtered_data = filter_nondigits(data) 

#plot this data to explore changes in heart rate for this file, save this visualization to the "images" folder
    fig, ax = plt.subplots()
    ax.plot(filtered_data)
    ax.set_title("Heart Rate Analysis")
    ax.set_xlabel("Time x-axis")
    ax.set_ylabel("Heartbeat y-axis")
    fig.savefig(f"images/{filename.split("/")[1].replace("txt", "png")}")

#calculate the average, maximum, and standard deviation of this file using the functions you've written
    avg_hr = average(filtered_data)
    max_hr = maximum(filtered_data)
    std_dev_hr = standard_deviation(filtered_data)

#return all 3 values
    print(avg_hr, max_hr, std_dev_hr)
    return avg_hr, max_hr, std_dev_hr
    
if __name__ == "__main__":
    print(run("data/phase0.txt"))

#for phase in phases:
    #result = run(phase)
#print(f"Result for {phase}: {result}")