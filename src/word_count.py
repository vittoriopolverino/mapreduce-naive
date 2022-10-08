from collections import defaultdict


def mapper(sentence: str) -> list[(str, int)]:
    words = split_sentence(sentence=sentence)
    mapper = lambda word: (word, 1)
    return list(map(mapper, words))


def shuffler(map_result: list[(str, int)]) -> dict[str, list[int]]:
    shuffler = defaultdict(list)
    for word, occurrence in map_result:
        shuffler[word].append(occurrence)
    return shuffler


def reducer(shuffle_result: dict[str, list[int]]) -> list[(str, int)]:
    occurrences = [sum(occurrence) for word, occurrence in shuffle_result.items()]
    # print(occurrences)
    reducer = lambda word, occurrence: (word, occurrence)
    return list(map(reducer, shuffle_result, occurrences))


def map_reduce_naive(sentence: str) -> list[(str, int)]:
    map_result = mapper(sentence=sentence)
    # print(map_result)
    shuffle_result = shuffler(map_result=map_result)
    # print(shuffle_result.items())

    return reducer(shuffle_result=shuffle_result)