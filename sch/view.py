def get_op():
    op = int(input("1 - д.у.,\n 2 - д. п.,\n 3 - д. о., \n 4 - показать весь список,\n 5 - показать ученика,\n 6 - выход \n"))
    return op

def input_student():
    name = input("Введите имя и фамилию \n")
    return name

def input_less():
    less = input("Введите предмет \n")
    return less

def get_mark():
    name = input("Введите фамилию \n")
    less = input("Введите предмет \n")
    mark = input("Введите оценку \n")
    return name, less, mark


def input_student_table():
    name = input("Введите имя и фамилию для просмотра оценок \n")
    return name
    