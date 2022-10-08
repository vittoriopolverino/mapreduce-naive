from src.word_count import mapper, reducer, shuffler


def test_mapper(mock_input_data):
    mapping_result = mapper(text=mock_input_data)
    assert mapping_result == [
        ("dante", 1),
        ("nel", 1),
        ("mezzo", 1),
        ("del", 1),
        ("cammin", 1),
        ("di", 1),
        ("nostra", 1),
        ("vita", 1),
        ("dante", 1),
    ]


def test_shuffler(mock_mapped_data):
    shuffling_result = shuffler(mapped_data=mock_mapped_data)
    assert shuffling_result == {
        "dante": [1, 1],
        "nel": [1],
        "mezzo": [1],
        "del": [1],
        "cammin": [1],
        "di": [1],
        "nostra": [1],
        "vita": [1],
    }


def test_occurrences_count(mock_shuffled_data):
    occurences = [sum(occurrence) for word, occurrence in mock_shuffled_data.items()]
    assert occurences == [2, 1, 1, 1, 1, 1, 1, 1]


def test_reducer(mock_shuffled_data):
    reducer_result = reducer(shuffled_data=mock_shuffled_data)
    assert reducer_result == [
        ("dante", 2),
        ("nel", 1),
        ("mezzo", 1),
        ("del", 1),
        ("cammin", 1),
        ("di", 1),
        ("nostra", 1),
        ("vita", 1),
    ]
