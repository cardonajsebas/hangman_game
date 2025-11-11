import pytest
from project import get_word, validate_input, LIVES_BY_DIFFICULTY


def test_validate_input_correct_letter():
    """If user guesses a correct letter, it should update masked_word properly."""
    word = "apple"
    masked = "_ _ _ _ _"
    new_masked, correct, won = validate_input("a", word, masked)

    assert correct is True
    assert "a" in new_masked
    assert won is False


def test_validate_input_incorrect_letter():
    word = "apple"
    masked = "_ _ _ _ _"
    new_masked, correct, won = validate_input("z", word, masked)

    assert correct is False
    assert new_masked == masked
    assert won is False


def test_validate_input_full_word_correct():
    word = "apple"
    masked = "_ _ _ _ _"
    new_masked, correct, won = validate_input("apple", word, masked)

    assert correct is True
    assert won is True
    assert new_masked == word


def test_validate_input_full_word_wrong():
    word = "apple"
    masked = "_ _ _ _ _"
    new_masked, correct, won = validate_input("banana", word, masked)

    assert correct is False
    assert won is False
    assert new_masked == masked


def test_lives_by_difficulty_values():
    assert LIVES_BY_DIFFICULTY["1"] > LIVES_BY_DIFFICULTY["3"]
    assert set(LIVES_BY_DIFFICULTY.keys()) == {"1", "2", "3"}
