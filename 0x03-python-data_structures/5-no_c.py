def no_c(my_string):
    remove_c = my_string.translate({ord(i): None for i in 'cC'})
    return remove_c
