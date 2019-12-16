#!/usr/bin/env python3
#coding:utf-8

from math import ceil, floor

def ask_list():
    returned_list = []
    while True:
        user_input = input("Enter a value to append to the list or type 'stop' : ")
        if user_input in ['stop', '\n', '', None]:
            return returned_list
        else:
            returned_list.append(float(user_input))
            print(f"The list currently contains the following elements : {returned_list}\n")

def ask_dict():
    returned_dict = {}
    while True:
        user_input = input("Enter an entry to append to this 2D list or type 'stop' : ")
        user_input = user_input.replace(',', '.')
        if user_input in ['stop', '\n', '', None]:
            return returned_dict
        else:
            user_value = input(f"What is the effective for the following entry : {user_input} ? ")
            user_value = user_value.replace(',', '.')
            returned_dict[float(user_input)] = float(user_value)
            print(f"The 2D list currently contains the following elements : {returned_dict}\n")


def compute_average(number_list):  # Compute the average of a list
    top = float()
    for number in number_list:
        top += number
    return float(top / float(len(number_list)))

def compute_median(number_dict):
    dict_len = int(len(number_dict))
    if dict_len % 2 == 0:
        return compute_average( [ number_dict[ceil(dict_len/2)] , number_dict[floor(dict_len/2)] ])
    else:
        return number_dict[dict_len / 2]