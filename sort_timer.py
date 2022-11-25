# Author: Patrick Duane
# GitHub username: patrickduane94
# Date: 07/30/2022

import time
import random
import matplotlib.pyplot as graph


def bubble_sort(a_list):
  for pass_num in range(len(a_list) - 1):
    for index in range(len(a_list) - 1 - pass_num):
      if a_list[index] > a_list[index + 1]:
        temp = a_list[index]
        a_list[index] = a_list[index + 1]
        a_list[index + 1] = temp


def insertion_sort(a_list):
  for index in range(1, len(a_list)):
    value = a_list[index]
    pos = index - 1
    while pos >= 0 and a_list[pos] > value:
        a_list[pos + 1] = a_list[pos]
        pos -= 1
    a_list[pos + 1] = value


def sort_timer(function):  #decorator for calculating bubble sort and insertion sort times
    def get_times(sequence):
        begin = time.perf_counter()
        function(sequence)  #calling functions
        end = time.perf_counter()
        elapsed_time = end - begin  #subtract to get elapsed time
        return elapsed_time
    return get_times


def compare_sorts(bubble_sort_time, insertion_sort_time):
    y_axis_ins = []  #setting y axis data to empty lists
    y_axis_bub = []
    x_axis = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]  #x-axis values set to list sizes
    num_list = []  #empty random number list
    i = 1000
    while i <= 10000:  #exit while loop when i hits max list size of 10000
        num_list.append(random.randint(1, 10000) in range(i))  #append i random numbers between 1 and 10000
        new_list = list(num_list) #copy of num_list
        bub = bubble_sort_time(num_list)  #using decorator and passing to it the num_list
        ins = insertion_sort_time(new_list)
        y_axis_bub.append(bub)  #append elapsed time to y-axis data for bubble sort
        y_axis_ins.append(ins)  #append elapsed time to y-axis data for insertion sort
        i += 1000  #increment i by 1000 - lists should be in increments of 1000 in (1000, 10000)
    graph.plot(x_axis, y_axis_bub, 'ro--', linewidth=2, label='bubble sort')  #modified code for graph
    graph.plot(x_axis, y_axis_ins, 'go--', linewidth=2, label='insertion sort')
    graph.xlabel("size of list")
    graph.ylabel("elapsed time")
    graph.legend(loc='upper left')
    graph.show()


compare_sorts(sort_timer(bubble_sort), sort_timer(insertion_sort))
