
import sys

def create_map(map_str):
    ranges = []
    for line in map_str.strip().split('\n')[1::]:
        dest, source, upper = [int(x) for x in line.split(' ')]
        ranges.append([(dest, dest + upper),(source, source + upper)])
    return ranges


def treat_ranges(map, ranges):
    d_range, s_range = map
    d_low, _ = d_range
    s_low, s_high = s_range

    outside_ranges = []
    inside_ranges = []

    for curr_low, curr_high in ranges:
        if (curr_low < s_low):
            before = (curr_low, min(s_low, curr_high))
            outside_ranges.append(before)
        if (curr_high > s_high):
            after = (max(s_high, curr_low), curr_high)
            outside_ranges.append(after)
        if (curr_low >= s_high or curr_high <= s_low):
            continue
        b_low, b_high = (max(s_low, curr_low), min(s_high, curr_high))
        between_map = (d_low + (b_low - s_low), d_low + (b_high - s_low))
        inside_ranges.append(between_map)
    
    return outside_ranges, inside_ranges



def main(argv, argc):
    input = open(argv[1]).read().split('\n\n')
    seed_ranges = [int(x) for x in input[0].split(' ')[1::]]
    seed_ranges = zip(seed_ranges[0::2], seed_ranges[1::2])
    maps = []
    for map_str in input[1::]:
        maps.append(create_map(map_str))

    min_location = -1

    for seed_low, seed_range in seed_ranges:
        curr_ranges = [(seed_low, seed_low + seed_range)]
        for map in maps:
            outside_ranges, inside_ranges = curr_ranges,[]
            for range in map:
                new_outside, new_inside = treat_ranges(range, outside_ranges)
                inside_ranges += new_inside
                outside_ranges = new_outside
            curr_ranges = outside_ranges + inside_ranges
        local_min = -1
        for low, _ in curr_ranges:
            if low < local_min or local_min == -1:
                local_min = low
        if local_min < min_location or min_location == -1:
            min_location = local_min

    print(min_location)




if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
