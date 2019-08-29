# Given a list filled with 0s and 1s, find the maximum number of consecutive 1s in this list.

# List of 0s and 1s
track_ones = [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1]

def find_max():

    count_ones = []
    only_ones = []
    ones = 0
    loop_count = 0

    for x in track_ones:
        loop_count += 1

        if x == 1:
            ones += 1
            only_ones.append(1)

        if x == 0 and loop_count > 1 and len(only_ones) > 0:
            count_ones.append(ones)
            ones = 0
            only_ones.clear()

        if loop_count == len(track_ones):
            count_ones.append(ones)
            if count_ones[len(count_ones) - 1] == 0:
                count_ones.remove(count_ones[len(count_ones) - 1])

    print("Input: ", track_ones)
    print("Output: ", max(count_ones))

# Return the maximum number of consecutive 1s
find_max()