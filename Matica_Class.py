class basic_matrica (object):
    matrica_size: int

    def __init__(self):
        self.input_string = input()
        self.prepared_matrica = [[]]
        self.matrica_elements = []
        self.matrica_size = 0
    def preparation (self):
        number = 0
        for i in self.input_string:
            if i == " ":
                self.matrica_elements.append(number*minus_identificator)
                minus_identificator = 1
                number = 0
            elif i == "-":
                minus_identificator = -1
            else:
                number = number * 10 + int(i)
        self.matrica_elements.append(number * minus_identificator)
        self.matrica_size = int(pow(len(self.matrica_elements), 0.5))
        self.prepared_matrica = [[0 for j in range(self.matrica_size)] for i in range(self.matrica_size)]
        for w in range(self.matrica_size):
            for q in range(self.matrica_size):
                self.prepared_matrica[w][q] = self.matrica_elements[w*self.matrica_size+q]
        print(self.prepared_matrica)
matrica_A = basic_matrica()
matrica_A.preparation()









