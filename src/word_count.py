from collections import defaultdict


def splitter(text: str) -> list[str]:
    return text.lower().split()


def mapper(splitted_data: list[str]) -> list[(str, int)]:
    return list(map(lambda word: (word, 1), splitted_data))


def shuffler(mapped_data: list[(str, int)]) -> dict[str, list[int]]:
    word_occurrences = defaultdict(list)
    for word, occurrence in mapped_data:
        word_occurrences[word].append(occurrence)
    return word_occurrences


def reducer(shuffled_data: dict[str, list[int]]) -> list[(str, int)]:
    occurrences = [sum(occurrence) for word, occurrence in shuffled_data.items()]
    # print(occurrences)
    return list(
        map(lambda word, occurrence: (word, occurrence), shuffled_data, occurrences)
    )


def map_reduce_naive(text: str) -> list[(str, int)]:
    split_result = splitter(text=text)
    mapping_result = mapper(splitted_data=split_result)
    shuffling_result = shuffler(mapped_data=mapping_result)
    return reducer(shuffled_data=shuffling_result)
