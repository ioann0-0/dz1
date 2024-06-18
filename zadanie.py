"""шахматы"""
def queen_move(start, end):
    """"""
    x1, y1 = start
    x2, y2 = end
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return True
    else:
        return False

def knight_move(start, end):
    """"""
    x1, y1 = start
    x2, y2 = end
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
        return True
    else:
        return False

def parsing_position(position):
    """"""
    column = position[0].upper()
    row = int(position[1])
    column_index = ord(column) - ord('A')
    row_index = 8 - row
    return (row_index, column_index)

def main():
    """"""
    try:
        start_position = input("Введите начальную позицию: ")
        end_position = input("Введите конечную позицию: ")

        start = parsing_position(start_position)
        end = parsing_position(end_position)

        if queen_move(start, end):
            print("Ферзь может попасть на указанную клетку одним ходом.")
        else:
            print("Ферзь не может попасть на указанную клетку одним ходом.")

        if knight_move(start, end):
            print("Конь может попасть на указанную клетку одним ходом.")
        else:
            print("Конь не может попасть на указанную клетку одним ходом.")

    except ValueError:
        print("Неверный формат ввода ")
    except IndexError:
        print("Некорректные координаты ")

if __name__ == "__main__":
    main()
