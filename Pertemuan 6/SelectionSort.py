def selection_sort(data):
    n = len(data)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if data[j] < data[min_index]: 
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]

#Simulasi
my_list=[22,77,88,66,55,33,44,11]
selection_sort(my_list)
print(f"Data setelah diurutkan: {my_list}")