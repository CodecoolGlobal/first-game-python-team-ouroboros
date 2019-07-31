def transpose(table):
    return [list(row) for row in zip(*table)]


def reverse_rows(table):
    return [list(reversed(row)) for row in table]


def slide_down(table):
    return transpose(slide_right(transpose(table)))


def slide_right(table):
    remove_all(0, table)
    for rows in table:
        if len(rows) == 2:
            if rows[-1] == rows[-2]:
                rows[-1] += rows[-2]
                del rows[-2]
        elif len(rows) == 3:
            if rows[-1] == rows[-2]:
                rows[-1] += rows[-2]
                del rows[-2]
            elif rows[-2] == rows[-3]:
                rows[-2] += rows[-3]
                del rows[-3]
        elif len(rows) == 4:
            if rows[-1] == rows[-2] and rows[-3] == rows[-4]:
                rows[-1] += rows[-2]
                rows[-2] = rows[-3] + rows[-4]
                del rows[-4]
                del rows[-3]
            elif rows[-1] == rows[-2]:
                rows[-1] += rows[-2]
                del rows[-2]
            elif rows[-2] == rows[-3]:
                rows[-2] += rows[-3]
                del rows[-3]
            elif rows[-3] == rows[-4]:
                rows[-3] += rows[-4]
                del rows[-4]
    for i in range(4):
        while len(table[i]) != 4:
            table[i].insert(0, 0)
    return table


def remove_all(what, from_where):
    for nested_list in from_where:
        while what in nested_list:
            nested_list.remove(what)


def slide_up(table):
    return transpose(reverse_rows(slide_right((reverse_rows(transpose(table))))))


def slide_left(table):
    return reverse_rows(slide_right(reverse_rows(table)))


table = [[2, 18, 64, 8], [2, 4, 128, 4], [2, 2, 0, 0], [1, 0, 1, 1]]

print(table)
print()
table = slide_down(table)
print(table)
table[2][1] = 0
table = transpose(table)
print(table)
