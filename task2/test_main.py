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
    max_shifts = 14
    min_shifts = 13

    result = allocate(preferences, officers_per_org, min_shifts, max_shifts)

    assert result is None


def test_6():
    preferences = [[1, 0, 0], [1, 0, 0]]
    officers_per_org = [[1, 0, 0]]
    max_shifts = 15
    min_shifts = 14

    result = allocate(preferences, officers_per_org, min_shifts, max_shifts)

    assert result is not None


def test_7():
    preferences = [[1, 0, 0], [1, 0, 0]]
    officers_per_org = [[1, 0, 0]]
    max_shifts = 15
    min_shifts = 14

    result = allocate(preferences, officers_per_org, min_shifts, max_shifts)

    assert result is not None


def test_8():
    preferences = [[1, 0, 0], [1, 0, 0]]
    officers_per_org = [[1, 0, 0]]
    max_shifts = 15
    min_shifts = 14

    result = allocate(preferences, officers_per_org, min_shifts, max_shifts)

    assert result is not None
