f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/tasks/26_1M__3whph.txt')
count_details = int(f.readline())
#список, в котором у нас будут все детали файла
array_details = []
for i in range(count_details):
    detail = list(map(int,f.readline().split()))
    if detail[0] > detail[1]:
        # добавляем второе число, указываем,
        # что эту деталь отправим на покраску и передаём её номер
        array_details.append((detail[1],"paint",i+1))
    else:
        # добавляем первое число, указываем,
        # что эту деталь отправим на шлифовку и передаём её номер
        array_details.append((detail[0],"grind",i+1))
array_details.sort()
# симулируем ленту транспортёра
lenta = [0]*count_details
# список, в котором у нас будут детали
# которые мы положили на ленту
details = []
for detail in array_details:
    # если эту деталь нужно отправить на шлифовку
    # то делаем перебор с начала ленты
    if detail[1] == "grind":
        for i in range(len(lenta)):
            # если эта ячейка свободна
            # указываем, что она занята
            if lenta[i] == 0:
                lenta[i] = 1
                details.append(detail)
                # сброс цикла для того, чтобы перейти к следующей детали
                break
    else:
        for i in range(len(lenta)-1,-1,-1):
            # если эта ячейка свободна
            # указываем, что она занята
            if lenta[i] == 0:
                lenta[i] = 1
                details.append(detail)
                break
#выводим номер, предпоследней детали,
# а также количество покрашенных деталей до этой детали
print(details[-2][2])
# так как предпоследняя деталь будет центральной
# на ленте и эта деталь отправленная на шлифовку
# то до нее не будет покрашено ни одной детали

