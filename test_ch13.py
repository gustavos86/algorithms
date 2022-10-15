import ch13

def test_exercise01():
    test1 = [1, 5, 9, 2, 7, 6, 8]
    result1 = 504

    test2 = [1, 5, 30, 9, 2, 90, 7, 6, 20, 8, 3]
    result2 = 54000

    test3 = [11, 5, 9, 2, 15, 7, 12, 6, 8, 1, 7]
    result3 = 1980

    assert ch13.exercise01(test1) == result1
    assert ch13.exercise01(test2) == result2
    assert ch13.exercise01(test3) == result3

def test_exercise02():
    test1 =  [5, 2, 4, 1, 0]
    result1 = 3

    test2 = [9, 3, 2, 5, 6, 7, 1, 0, 4]
    result2 = 8

    assert ch13.exercise02(test1) == result1
    assert ch13.exercise02(test2) == result2

def test_exercise03():
    test1 =  [5, 2, 4, 1, 0]
    result1 = 5

    test2 = [9, 3, 2, 5, 6, 7, 1, 0, 4]
    result2 = 9

    assert ch13.exercise03a(test1) == result1
    assert ch13.exercise03b(test1) == result1
    assert ch13.exercise03c(test1) == result1

    assert ch13.exercise03a(test2) == result2
    assert ch13.exercise03b(test2) == result2
    assert ch13.exercise03c(test2) == result2