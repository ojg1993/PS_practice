def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(lst, left, right):
    if left < right:
        pivot_index = pivot(lst, left, right)
        quick_sort_helper(lst, left, pivot_index)
        quick_sort_helper(lst, pivot_index + 1, right)
    # return lst


def quick_sort(my_list):
    quick_sort_helper(my_list, 0, len(my_list) - 1)


my_list = [4, 6, 1, 7, 3, 2, 5]

quick_sort(my_list)

print(my_list)


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7]
"""
