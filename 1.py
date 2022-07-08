
def task(array):
    count = 0
    for char in array:
        if (array[count]) == "0":
            return count
        else:
            count += 1


print(task("111111111110000000000000000"))
