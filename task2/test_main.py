from main import allocate


def test_1():
    preferences = [[1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]]
    officers_per_org = [[10, 8, 9], [5, 7, 8], [1, 4, 7]]
    max_shifts = 20
    min_shifts = 12

    result = allocate(preferences, officers_per_org, min_shifts, max_shifts)

    assert result is None


def test_2():
    preferences = [[1, 0, 0], [1, 0, 0]]
    officers_per_org = [[1, 0, 0]]
    max_shifts = 30
    min_shifts = 15

    result = allocate(preferences, officers_per_org, min_shifts, max_shifts)

    assert result is not None


def test_3():
    preferences = [[1, 0, 0], [1, 0, 0]]
    officers_per_org = [[1, 0, 0]]
    max_shifts = 30
    min_shifts = 16

    result = allocate(preferences, officers_per_org, min_shifts, max_shifts)

    assert result is None


def test_4():
    preferences = [[1, 0, 0], [1, 0, 0]]
    officers_per_org = [[1, 0, 0]]
    max_shifts = 14
    min_shifts = 0

    result = allocate(preferences, officers_per_org, min_shifts, max_shifts)

    assert result is None


def test_5():
    preferences = [[1, 0, 0], [1, 0, 0]]
    officers_per_org = [[1, 0, 0]]
    min_shifts = 13
    max_shifts = 14

    result = allocate(preferences, officers_per_org, min_shifts, max_shifts)

    assert result is None


def test_6():
    preferences = [[1, 0, 0], [1, 0, 0]]
    officers_per_org = [[1, 0, 0]]
    min_shifts = 14
    max_shifts = 15

    result = allocate(preferences, officers_per_org, min_shifts, max_shifts)

    assert result is not None


def test_7():
    preferences = [
        [0, 1, 1],
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
    ]
    officers_per_org = [[1, 1, 1]]
    assert allocate(preferences, officers_per_org, 11, 30) is None


def test_8():
    result = allocate(
        [[0, 1, 0], [1, 1, 1], [0, 0, 1], [0, 1, 1], [1, 0, 1], [0, 1, 0], [0, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 0]],
        [[2, 2, 5]], 26, 28)
    assert result is not None


def test_9():
    result = allocate(
        [[0, 0, 0], [0, 0, 1], [1, 0, 0], [0, 0, 1], [1, 1, 1], [0, 1, 1], [0, 0, 0], [0, 0, 0], [1, 1, 1], [1, 1, 1]],
        [[4, 5, 1], [7, 3, 3], [5, 7, 3], [9, 2, 9], [5, 6, 9], [5, 6, 8], [5, 6, 1], [10, 1, 2], [9, 7, 8],
         [10, 7, 9]], 7, 18)
    assert result is None
