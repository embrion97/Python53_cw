diapazon_first_1 = int(input("первая граница первого диапазона"))
diapazon_first_2 = int(input("вторая граница первого диапазона"))
diapazon_second_1 = int(input("первая граница второго диапазона"))
diapazon_second_2 = int(input("вторая граница второго диапазона"))
diapazon_three_1 = int(input("первая граница третьего диапазона"))
diapazon_three_2 = int(input("вторая граница третьего диапазона"))
x = int(input("chislo"))
ch = 0
if diapazon_first_1 <= x <= diapazon_first_2:
    ch +=ch
if diapazon_second_1 <= x <= diapazon_second_2:
    ch +=ch
if diapazon_three_1 <= x <= diapazon_three_2:
    ch +=ch

print(ch)

