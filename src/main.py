import operator
import time

import word_count as wdc

if __name__ == "__main__":
    with open("example.txt") as file:  # import data
        file_text = file.read()

    st = time.time()  # get the start time

    result = wdc.map_reduce_naive(text=file_text)
    result.sort(
        key=operator.itemgetter(1), reverse=True
    )  # descending sort based on the number of occurrences

    et = time.time()  # get the end time

    elapsed_time = et - st  # get the execution time
    print("Execution time:", elapsed_time, "seconds")

    print(result[:10])  # top 10
