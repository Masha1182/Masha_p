# Функция для сортировки списка по возрастанию методом вставок:
def sort_s(sp):
    for i in range(1, len(sp)):
        x = sp[i]
        idx = i
        while idx > 0 and sp[idx - 1] > x:
            sp[idx] = sp[idx - 1]
            idx -= 1
            sp[idx] = x
    return sp


# def sort_s(sp):
#    sp.sort()
# Функция для определение позиции элемента:
def index_n(sp, n):
    low = 0
    high = len(sp) - 1
    index = -1
    while (low <= high) and index == -1:
        mid = (low + high) // 2
        if sp[mid] < n <= sp[mid + 1]:
            index = mid
        else:
            if sp[mid] >= n:
             high = mid - 1
            else:
              low = mid + 1
    return index

try:
    nums = list(map(int, input('Введите последовательность разных целых чисел через пробел: ').split()))
    sorted_nums = sort_s(nums) #сортировка введенного списка

    if len(nums) < 2:      # проверка наличия как минимум 2-х чисел в последовательности
        print('Необходимо ввести хотя бы 2 числа через пробел!!!')
    else:
        num = int(input('Введите произвольное число: '))
        if num <= sorted_nums[0] or num > sorted_nums[-1]:     # проверка удовлетворения условий для поиска индекса
            print(f'Введенное число не входит в рамки диапазона от минимального значения  {sorted_nums[0]} до максимального {sorted_nums[-1]}')
        else:
            inx = index_n(sorted_nums, num) #вызов функции поиска индекса
            print(f' {inx} (Индекс элемента в упорядоченном списке {sorted_nums} меньшего по значению чем введенное число {num})')

except:
    print('Должны быть введены только числа через пробел!')  #исключение ввода чисел в неправильном формате