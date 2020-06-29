def merge_intervals(inp_arr):
    # input
    if not inp_arr or len(inp_arr) <= 1:
        return inp_arr

    # sort using the left value of the intervals

    inp_arr.sort(key=lambda interval: interval[0])

    # output array
    out_arr = []

    for index, interval in enumerate(inp_arr):

        # output array is empty OR last interval in output array is smaller than new interval
        if out_arr == [] or out_arr[-1][1] < interval[0]:
            out_arr.append(interval)

        # if the current interval value is larger than last interval in output array, merge them using max
        else:
            out_arr[-1][1] = max(out_arr[-1][1], interval[1])

    return out_arr
