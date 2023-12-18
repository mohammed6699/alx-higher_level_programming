#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    devide_list =[]

    for x in range(list_length):
        try:
            devide_list.append(my_list_1[x] / my_list_2[x])
        except TypeError:
            devide_list.append(0)
            print("wrong type")
            continue
        except ZeroDivisionError:
            devide_list.append(0)
            print("division by 0")
            continue
        except IndexError:
            devide_list.append(0)
            print("out of range")
            continue
        finally:
            pass
    return devide_list
