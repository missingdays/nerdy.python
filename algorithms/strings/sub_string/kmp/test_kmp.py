
from kmp import substring_index

def test_kmp_finds_substring():
    assert substring_index("abc", "abc") == 0
    assert substring_index("abc", "a") == 0
    assert substring_index("abcd", "d") == 3
    assert substring_index("hello", "e") == 1
    assert substring_index("hello", "ll") == 2

def test_kmp_fails_to_find():
    assert substring_index("a", "b") == -1
    assert substring_index("abc", "cd") == -1
    assert substring_index("a b", "ab") == -1
