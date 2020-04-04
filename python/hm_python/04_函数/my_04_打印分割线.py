def print_line(char, time):
    print(char * time)


# print_line("|", 10)


def print_row_line(row, char, time):
    """

    :param row: some row line
    :param char: split char
    :param time: split char time
    """
    i = 0
    while i < 5:
        print_line(char, time)
        i += 1


print_row_line(5, "=", 20)