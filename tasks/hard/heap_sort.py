"""
ПИРАМИДАЛЬНАЯ СОРТИРОВКА (СОРТИРОВКА КУЧЕЙ)
Также известна как сортировка кучей. Этот популярный алгоритм, как и сортировки
вставками или выборкой, сегментирует список на две части:
отсортированную и неотсортированную. Алгоритм преобразует второй сегмент
списка в структуру данных «куча» (heap),
чтобы можно было эффективно определить самый большой элемент.
Сначала преобразуем список в Max Heap — бинарное дерево, где самый большой
элемент является вершиной дерева. Затем помещаем этот элемент в конец списка.
После перестраиваем Max Heap и снова помещаем новый
наибольший элемент уже перед последним элементом в списке.
Этот процесс построения кучи повторяется, пока все вершины дерева не будут удалены.
ВРЕМЯ СОРТИРОВКИ: в среднем O(n log n)
"""


def heapify(nums, heap_size, root_index):
    # Индекс наибольшего элемента считаем корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня — допустимый индекс, а элемент больше,
    # чем текущий наибольший, обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # То же самое для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Если наибольший элемент больше не корневой, они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    # Создаём Max Heap из списка
    # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении,
    # уменьшая счётчик i на 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Перемещаем корень Max Heap в конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


some_list = [5, 6, 1, 8, 2, 3]
heap_sort(some_list)
n = len(some_list)
for i in range(n):
    print(some_list[i])