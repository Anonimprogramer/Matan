# coding=utf-8
from typing import Any


def gcd(my_list):
    result = my_list[0]
    for x in my_list[1:]:
        if result < x:
            temp = result
            result = x
            x = temp
        while x != 0:
            temp = x
            x = result % x
            result = temp
    return result


def fab(n):
    if n < 0:
        return -n
    else:
        return n


def nok(list):
    nod = fab(gcd(list))
    d = nod
    for i in list:
        d = d * i // nod
    return d


class Martica(object):

    def __init__(self):
        self.basic = [[]]
        self.column = 0
        self.lines = 0
        self.simple_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                               53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        self.determine_dictionary = {}
        self.determinant = 0
        self.transformer = [[]]
        self.extended = []
        self.trans = [[]]
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
        self.transformer = self.basic

    def determination(self, minor):
        if self.column != self.lines:
            print("Матрица не является квадратной.Вычисление определителя невозможно")
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

    def row_swap(self, row1, row2):
        for i in range(len(self.transformer[0])):
            self.transformer[row1][i], self.transformer[row2][i] = self.transformer[row2][i], self.transformer[row1][i]

    def column_swap(self,column1,column2):
        for i in range(len(self.transformer)):
            self.transformer[i][column1],self.transformer[i][column2] = self.transformer[i][column2],self.transformer[i][column1]

    def row_transformation(self, x, row1, row2):

        for i in range(len(self.transformer[0])):
            self.transformer[row2][i] = self.transformer[row2][i] + x * self.transformer[row1][i]
            if 0 > self.transformer[row2][i] > -0.00000000000001:
                self.transformer[row2][i] = 0


    def transpose(self):

        """Returns the transpose of matrix A.
        Preconditions: A is a matrix in the form of nested list."""

        m = len(self.transformer)
        n = len(self.transformer[0])

        self.trans = []
        for i in range(n):
            self.trans.append([])

        for i in range(n):
            for j in range(m):
                self.trans[i].append(self.transformer[j][i])

        return self.trans

    def rank_on_rank(self):
        m = len(self.transformer)
        n = len(self.transformer[0])
        for q in range(n-1):
            for w in range(q, m):
                for r in self.transformer:
                    print(r)
                print("раздел")
                if self.transformer[w][q] != 0:
                    for i in range(m):
                        if i != w and self.transformer[i][q] != 0:
                            x = self.transformer[i][q] / self.transformer[w][q]
                            self.row_transformation(-1 * x, w, i)
        return self.transformer


print("Вас привествует мистер Пудж. Могу сотворить пару колднуств.Колдунство номер 1 - определитель")
print("Колдунство номер 2 - это определитель матрицы")
print("Колднуство номер 3 - это решение СЛАУ(но пока что только определённых)")
print("Введите номер колдунства")
i = int(input())
matrix = Martica()
if i == 1:
    print(matrix.determination)
elif i == 2:
    print(matrix.trans)
elif i == 3:
    q = matrix.rank_on_rank()
    r = 0
    for t in q:
        r = r + 1
        first = 0
        second = 0
        for j in t:
            if j != 0 and first == 0:
                first = j
            elif j != 0 and first != 0:
                second = j
        print(r, '-й корень уравнения равен', int(second / first))

