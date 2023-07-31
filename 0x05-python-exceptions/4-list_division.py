#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for i in range(0, list_length):
        try:
            dv = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            dv = 0
        except ZeroDivisionError:
            print("division by 0")
            dv = 0
        except IndexError:
            print("out of range")
            dv = 0
        finally:
            n_list.append(dv)
    return (n_list)

