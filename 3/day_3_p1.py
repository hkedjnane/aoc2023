import sys

def check_surround(m, i, j):
    l1 = len(m)
    l2 = len(m[0])
    for x in range(i - 1, i + 2):
        if (x < 0 or x >= l1):
            continue
        for y in range(j - 1, j + 2):
            if y < 0 or y >= l2:
                continue
            #print(m[x][y],end=' ')
            if (x,y) == (i, j):
                continue
            if (m[x][y]) == '.' or (m[x][y]).isnumeric():
                continue
            return True
        #print('\n')
    return False

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
    #print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in m]))
    l1 = len(m)
    l2 = len(m[0])
    print(l1, l2)
    total = 0
    for i in range(l1):
        print(m[i])
        for j in range(l2):
            s = m[i][j]
            if s.isnumeric():
                if not prev_num and check_surround(m, i, j):
                    total += int(s)
                    prev_num = True
            else:
                prev_num = False

    print(total)

if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
