
def equal(list1, list2):
    if len(list1) != len(list2):
        return False

    for e1, e2 in zip(list1, list2):
        if e1 != e2:
            return False

    return True
