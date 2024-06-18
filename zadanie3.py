""""""
def array_element(arr, index):
    """"""
    try:
        element = arr[index]
        print(f"Элемент по индексу {index} равен {element}")
    except IndexError:
        print(f"Ошибка: Индекс {index} выходит за границы массива")

array = [1, 2, 3, 4, 5, 6]

array_element(array, 2)
array_element(array, 10)
array_element(array, -1)
