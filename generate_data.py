'''this file is for testing and calcuating the waste of each algorithm. it will generate the increasing
on sizes of n random uniform permutations from 0.0-0.6 and call each bin-packing algorithm.
it will then store the data in csv files to be called by the plotting file, which will then plot them on
graphs.
'''
from next_fit import next_fit
from first_fit import first_fit
from first_fit import first_fit_decreasing
from best_fit import best_fit, merge_sort
from best_fit import best_fit_decreasing
import random, csv

def generate_permutation(n:int) -> list[float]:
    """Given an input size n, generate a random uniform permutation from 0.0-0.6"""
    permutation = [random.uniform(0.0, 0.6) for _ in range(n)]
    random.shuffle(permutation)
    return permutation

def calculate_waste(lst: list[float]):
    # waste is the sum of the free_space list
    return sum(lst)

def waste(algorithm, n: int, file):
    """Takes a function pointer as an argument and an input size. Takes the input size as an argument, generates
    the permutation list, runs and times the function. Creates output and prints to a csv file"""
    # format: 
    # "size,waste"
    # n,waste
    # five times total on each permutation size (average of waste).
    writer = csv.writer(file)
    waste = 0
    for i in range(5):
        permutation = generate_permutation(n)
        space = algorithm(permutation, [0]*n, [])
        waste += calculate_waste(space)

    waste /= 5
    writer.writerow([n, waste])

def test_func(algorithm, filename: str):
    sizes = [15, 67, 150, 675, 1500, 6750, 15000]       # sizes to test on. 5-10 tests on each size to get an average
    # open the file and add the headers, then do a double for loop to pass to the function
    # and run 5-10 times for each size, add to csv file
    with open(filename, mode = 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["size", "waste"])
        for s in sizes:
            # calculate waste of algorithm 5 times and append to csv
            waste(algorithm, s, file)



if __name__ == "__main__":
    test_func(best_fit, "best_fit.csv")
    test_func(best_fit_decreasing, "best_fit_decreasing.csv")
    test_func(next_fit, "next_fit.csv")
    test_func(first_fit, "first_fit.csv")
    test_func(first_fit_decreasing, "first_fit_decreasing.csv")