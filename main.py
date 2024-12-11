#Функция ввода чисел
def input_figure():
    try:
        global figure
        figure = int(input("Введите число от 1 до 5: "))
        assert figure >= 1 and figure <= 5, \
            "Ошибка: нужно ввести числа от 1 до 5"
    except ValueError:
        print("Ошибка: введено не число!")


#Функция вывода слова
def print_word(fig):
    if fig == 1:
        return "One"
    elif fig == 2:
        return "Two"
    elif fig == 3:
        return "Three"
    elif fig == 4:
        return "Four"
    else:
        return "Five"


#Основное тело программы
input_figure()
print(print_word(figure))