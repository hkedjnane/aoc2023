import sys

def main(argv, argc):
    input = argv[1]
    time, distance = open(input).readlines()
    time = [int(x) for x in filter(None,time.split(':')[1].strip().split(' '))]
    record_distance = [int(x) for x in filter(None,distance.split(':')[1].strip().split(' '))]
    td = zip(time, record_distance)
    answer = 1
    for t, rd in td:
        total = 0
        for pressing_time in range(t+1):
            speed = pressing_time
            run_time = t - pressing_time
            d = speed * run_time
            if (d > rd):
                total+=1
        answer *= total
    print(answer)
            




if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
