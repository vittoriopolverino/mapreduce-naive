import pytest


@pytest.fixture()
def mock_input_data():
    return "Dante Nel mezzo del cammin di nostra vita Dante"


@pytest.fixture()
def mock_splitted_data():
    return ["dante", "nel", "mezzo", "del", "cammin", "di", "nostra", "vita", "dante"]


@pytest.fixture()
def mock_mapped_data():
    return [
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


@pytest.fixture()
def mock_shuffled_data():
    return {
        "dante": [1, 1],
        "nel": [1],
        "mezzo": [1],
        "del": [1],
        "cammin": [1],
        "di": [1],
        "nostra": [1],
        "vita": [1],
    }


@pytest.fixture()
def mock_occurences_count():
    return [2, 1, 1, 1, 1, 1, 1, 1]
