# coding=utf-8
from typing import Any


class Martica(object):

    def __init__(self):
        self.basic = [[]]
        self.column = 0
        self.lines = 0
        self.determine_dictionary = {}
        self.determinant = 0
        self.correct_protect = "incorrect"
        print("Введите количество строчек основной матрицы")
        self.lines = int(input())
        print("Введите количество столбцов основной матрицы")
        self.column = int(input())
        print("Вводите матрицу построчно")
        self.basic = [[int(j) for j in input().split()] for i in range(self.lines)]
        while self.correct_protect != "correct":
            for i in range(self.lines):
                print (self.basic[i])
            print("Ваша матрица имеет следующий вид.Если вас полсностью устраивает её текущий вид введите correct")
            self.correct_protect = input()
            if self.correct_protect != "correct":
                print("Введите строку изменяемого элемента")
                i = int(input())
                print("Введите столбец изменяемого элемента")
                j = int(input())
                print("Введите новое значение элемента")
                f = int(input())
                self.basic[i - 1][j - 1] = f

    def determination(self, minor):
        if self.column != self.lines:
            print("Матрица не является квадратичной.Вычисление определителя невозможно")
        elif len(minor) == 2:
            e = 0
            return minor[0][0] * minor[1][1] - minor[1][0] * minor[0][1]
        else:
            e = 0
            for i in range(len(minor)):
                smaller = [[0 for i in range(len(minor) - 1)] for j in range(len(minor) - 1)]
                for j in range(len(minor)-1):
                    for q in range(len(minor)-1):
                        if i <= q:
                            smaller[j][q] = minor[j+1][q+1]
                        else:
                            smaller[j][q] = minor[j+1][q]
                e = e + minor[0][i]*self.determination(smaller) * pow(-1, i-1)
            return e


moy = Martica()
ybivca =moy.determination(moy.basic)
print("Вот он определитель", ybivca)







