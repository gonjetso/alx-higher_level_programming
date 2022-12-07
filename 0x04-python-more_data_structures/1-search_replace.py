#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = [item if item != 2 else 89
            for item in my_list]

    return new_list
