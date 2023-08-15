#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list2 = my_list.copy()
    if my_list:
        if idx >= len(my_list):
            return my_list
        elif idx < 0:
            return my_list
        else:
            list2[idx] = element
            return list2
    else:
        return None
