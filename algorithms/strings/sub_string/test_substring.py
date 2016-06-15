
from kmp import substring_index as kmp_substring_index
from naive import substring_index as naive_substring_index

def test_finds_substring():
    assert kmp_substring_index("abc", "abc") == 0
    assert kmp_substring_index("abc", "a") == 0
    assert kmp_substring_index("abcd", "d") == 3
    assert kmp_substring_index("hello", "e") == 1
    assert kmp_substring_index("hello", "ll") == 2

    assert naive_substring_index("abc", "abc") == 0
    assert naive_substring_index("abc", "a") == 0
    assert naive_substring_index("abcd", "d") == 3
    assert naive_substring_index("hello", "e") == 1
    assert naive_substring_index("hello", "ll") == 2

def test_fails_to_find():
    assert kmp_substring_index("a", "b") == -1
    assert kmp_substring_index("abc", "cd") == -1
    assert kmp_substring_index("a b", "ab") == -1

    assert naive_substring_index("a", "b") == -1
    assert naive_substring_index("abc", "cd") == -1
    assert naive_substring_index("a b", "ab") == -1
