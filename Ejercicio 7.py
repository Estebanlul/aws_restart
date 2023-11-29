string = "23 34 1 45 67 78 100 2"

array = string.split()

array = [int(number) for number in array]
n = len(array)

for i in range(n):
    min_index = i

    for j in range(i+1, n):
        if array[j] < array[min_index]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]

print(array)