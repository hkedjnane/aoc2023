import sys

d : dict = {}

def check_surround(m, i, j, checked):
    l1 = len(m)
    l2 = len(m[0])
    for x in range(i - 1, i + 2):
        if (x < 0 or x >= l1):
            continue
        for y in range(j - 1, j + 2):
            if y < 0 or y >= l2:
                continue
            if m[x][y] == '*' and not (x,y) in checked:
                d[(x,y)] = d.get((x,y), []) + [(i,j)]
                checked.append((x,y))

def create_matrix(input):
    m = []
    for line in open(input).readlines():
        line = line.strip()
        ml = []
        num = ""
        for c in line:
            if c.isnumeric():
                num += c
            else:
                if num != "":
                    for i in range(len(num)):
                        ml.append(num)
                    num = ""
                ml.append(c)
        if num != "":
            for i in range(len(num)):
                ml.append(num)
            num = ""
        m.append(ml)
    return m


def main(argv, argc):
    input = argv[1]
    m = create_matrix(input)
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in m]))
    l1 = len(m)
    l2 = len(m[0])
    print(l1, l2)
    total = 0
    for i in range(l1):
        checked = []
        for j in range(l2):
            s = m[i][j]
            if s.isnumeric():
                check_surround(m, i, j, checked)
            else:
                checked.clear()
    for coords in d.values():
        if (len(coords) != 2):
            continue
        c1 = coords[0]
        c2 = coords[1]
        gear = int(m[c1[0]][c1[1]]) * int(m[c2[0]][c2[1]])
        total += gear
    print(total)


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
