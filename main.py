# coding=utf-8
from typing import Any
import kivy.uix.boxlayout
import kivy.app
import kivy.uix.textinput
import kivy.uix.label
import kivy.uix.button

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

    def __init__(self,input_matrix):
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
        self.basic = input_matrix
        self.transformer = self.basic

    def determination(self, minor):
        if self.column != self.lines:
            return Error
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
                e = e + minor[0][i]*self.determination(smaller) * pow(-1, i)
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
                    if self.transformer[w][q] != 0:
                        for i in range(m):
                            if i != w and self.transformer[i][q] != 0:
                                x = self.transformer[i][q] / self.transformer[w][q]
                                self.row_transformation(-1 * x, w, i)
        return self.transformer


class OurSimpleApp(kivy.app.App):
    def build(self):
        self.textInput = kivy.uix.textinput.TextInput()
        self.label = kivy.uix.label.Label(text='Результат будет здесь')
        self.button = kivy.uix.button.Button(text='Понеслась')
        self.button.bind(on_press=self.displayMessage)
        self.boxLayout = kivy.uix.boxlayout.BoxLayout(orientation='vertical')
        self.boxLayout.add_widget(self.textInput)
        self.boxLayout.add_widget(self.label)
        self.boxLayout.add_widget(self.button)
        return self.boxLayout

    def preparation(self):
        prepared_matrica = [[]]
        matrica_elements = []
        n = 1
        matrica_size = 0
        number = 0
        minus_identificator = 1
        for i in self.textInput.text:
            if i =='\n':
                n = n + 1
            if i ==' ' or i =='\n':
                matrica_elements.append(number * minus_identificator)
                minus_identificator = 1
                number = 0
            elif i == "-":
                minus_identificator = -1
            else:
                number = number * 10 + int(i)
        matrica_elements.append(number * minus_identificator)
        m = int(len(matrica_elements)/n)
        prepared_matrica = [[0 for j in range(n)] for i in range(m)]
        for w in range(n):
            for q in range(m):
                prepared_matrica[w][q] = matrica_elements[w * m + q]
        print(prepared_matrica)
        return prepared_matrica
    def work_with_data(self):
        data = self.preparation()
        a = Martica(data)
        self.textInput.text = 'Определитель - ' + str(a.determination(data))
    def displayMessage(self, btn):
        self.work_with_data()
        self.label.text = self.textInput.text
if __name__ == '__main__':
    simpleApp = OurSimpleApp()
    simpleApp.run()