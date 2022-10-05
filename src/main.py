from collections import defaultdict
import time
import operator


def split_sentence(sentence: str) -> list[str]:
    return sentence.split()


def mapper(sentence: str) -> list[(str, int)]:
    words = split_sentence(sentence=sentence)
    mapper = lambda word: (word, 1)
    return list(map(mapper, words))


def shuffler(map_result: list[(str, int)]) -> dict[str, list[int]]:
    shuffler = defaultdict(list)
    for word, occurrence in map_result:
        shuffler[word].append(occurrence)

    return shuffler


def reducer(shuffle_result: dict[str, list[int]]) -> list[tuple[str, int]]:
    occurrences = [sum(occurrence) for word, occurrence in shuffle_result.items()]
    # print(occurrences)

    reducer = lambda word, occurrence: (word, occurrence)
    return list(map(reducer, shuffle_result, occurrences))


def map_reduce_naive(sentence: str) -> list[tuple[str, int]]:
    map_result = mapper(sentence=sentence)
    # print(map_result)

    shuffle_result = shuffler(map_result=map_result)
    # print(shuffle_result.items())
    return reducer(shuffle_result=shuffle_result)


if __name__ == '__main__':
    # import data
    with open('example.txt') as file:
        sentence = file.read().lower()

    # get the start time
    st = time.time()

    result = map_reduce_naive(sentence=sentence)

    # descending sort based on the number of occurrences
    result.sort(key=operator.itemgetter(1), reverse=True)

    # get the end time
    et = time.time()

    # get the execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    # top 10
    print(result[:10])


