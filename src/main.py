import operator
import os
import time

import config
import word_count as wdc

if __name__ == "__main__":
    os.chdir(config.ROOT_DIR)

    # import data
    with open("data.txt") as file:
        file_text = file.read()

    # get the start time
    st = time.time()

    # mapreduce output
    result = wdc.map_reduce_naive(text=file_text)

    # descending sort based on the number of occurrences
    result.sort(key=operator.itemgetter(1), reverse=True)

    # get the end time
    et = time.time()

    # get the execution time
    elapsed_time = et - st
    print("Execution time:", elapsed_time, "seconds")

    # top 10
    print(result[:10])
