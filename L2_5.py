# Пользователь вводит число N. Создать массив размера N, который одинаково читается как слева направо, так и справа налево.

a = int(input())
if a>0 : 
    sq1 = [i for i in range(a//2+a%2)]
    sq2 = sq1[:]
    sq2.reverse()
    if (a%2) : sq2.pop(0)
    sq = sq1[:] + sq2[:]
    print(sq)
else :
    print('Введите число > 0')