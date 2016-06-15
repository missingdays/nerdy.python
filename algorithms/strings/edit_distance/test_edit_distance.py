
from edit_distance import edit_distance

def test_edit_distance():

    assert edit_distance("", "") == 0

    assert edit_distance("", "a") == 1
    assert edit_distance("a", "") == 1
    assert edit_distance("", "aaaaa") == 5

    assert edit_distance("a", "a") == 0
    assert edit_distance("really big string with spaces", "really big string with spaces") == 0

    assert edit_distance("aaaaa", "bbbbb") == 5
    assert edit_distance("caaaa", "aaaaa") == 1
    assert edit_distance("aacaa", "aaaaa") == 1
    assert edit_distance("aaaac", "aaaaa") == 1

    assert edit_distance("bcd", "abcd") == 1
    assert edit_distance("abd", "abcd") == 1
    assert edit_distance("abc", "abcd") == 1

    assert edit_distance("abcd", "bcd") == 1
    assert edit_distance("abcd", "abd") == 1
    assert edit_distance("abcd", "abc") == 1

    assert edit_distance("cruel cruel world", "duel due war") == 8
