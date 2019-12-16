#!/usr/bin/env python3
#coding:utf-8

from pystat.basicStats import *

def average():
    user_list = ask_list()
    print(f"The average of the list {user_list} is {compute_average(user_list)}")

def median():
    print("Please input the values in increasing order.\n")
    user_dict = ask_list()
    median = compute_median(user_dict)
    print(f"The median of the 2D list {user_dict} is {median}")

if __name__ == "__main__":
    median()