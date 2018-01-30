from palindrome_check import palindrome_check


# Basic Tests
def test_palindrome_check_with_odd_character_count_input():
    test_string = "madam"

    assert palindrome_check(test_string) is True


def test_palindrome_with_even_character_count_input():
    test_string = "redder"

    assert palindrome_check(test_string) is True


def test_palindrome_check_with_non_palindrome_input():
    test_string = "empty"

    assert palindrome_check(test_string) is False


def test_palindrome_check_with_empty_string_input():
    test_string = ""

    assert palindrome_check(test_string) is True


def test_palindrome_check_with_single_character_input():
    test_string = "A"

    assert palindrome_check(test_string) is True


# Edge cases
def test_palindrome_check_with_None_input():
    test_string = None

    assert palindrome_check(test_string) is False


def test_palindrome_check_ignores_single_spaces_in_input():
    test_string = "nurses run"

    assert palindrome_check(test_string) is True


def test_palindrome_check_ignores_multiple_spaces_in_input():
    test_string = " pull   up "

    assert palindrome_check(test_string) is True


def test_palindrome_check_with_non_palindrome_including_whitespace():
    test_string = " not in  "

    assert palindrome_check(test_string) is False
