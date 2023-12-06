import sys

def main(argv, argc):
    input = argv[1]
    time, distance = open(input).readlines()
    time = int(time.split(':')[1].replace(' ', ''))
    record_distance = int(distance.split(':')[1].replace(' ', ''))
    total = 0
    for pressing_time in range(time+1):
        speed = pressing_time
        run_time = time - pressing_time
        d = speed * run_time
        if (d > record_distance):
            total+=1
    print(total)
            




if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
