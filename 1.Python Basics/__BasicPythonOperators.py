from random import randrange

# create list of 100 random numbers from 0 to 1000 each
list_of_randoms = [randrange(1001) for i in range(100)]
print(list_of_randoms)


# sort list from min to maxx
def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randrange(len(array))]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)


sorted_list = quicksort(list_of_randoms)
print(sorted_list)


# calculate average for even and odd numbers

def even_and_odd_averages(array):
    sum_even = 0
    sum_odd = 0
    num_even = 0
    num_odd = 0
    for n in array:
        if n % 2 == 0:
            sum_even += n
            num_even += 1
        else:
            sum_odd += n
            num_odd += 1

    if num_odd:
        avg_odd = sum_odd / num_odd
    else:
        avg_odd = None

    if num_even:
        avg_even = sum_even / num_even
    else:
        avg_even = None

    return avg_even, avg_odd

avg_even, avg_odd = even_and_odd_averages(list_of_randoms)
avg_even_sorted, avg_odd_sorted = even_and_odd_averages(sorted_list)
# print both average results
print("avg_even = {0} \n avg_odd = {1} \n".format(avg_even, avg_odd))

print("avg_even_sorted = {0} \n avg_odd_sorted = {1} \n".format(avg_even_sorted, avg_odd_sorted))
