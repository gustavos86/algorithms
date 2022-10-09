import recursion

def test_traverse_array(capfd):
    """
    Test def traverse_array(list1) which is in recursion.py
    """
    array = [  1,
           2,
           3,
           [4, 5, 6],
           7,
           [8,
             [9, 10, 11,
               [12, 13, 14]
             ]
           ],
           [15, 16, 17, 18, 19,
             [20, 21, 22,
               [23, 24, 25,
                 [26, 27, 29]
               ], 30, 31
             ], 32
           ], 33
        ]

    result = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 29 30 31 32 33 "

    recursion.traverse_array(array)
    out, err = capfd.readouterr()
    assert out == result

def test_ch11_exercise1():
    test1 = ["ab", "c", "def", "ghij"]
    result1 = 10

    test2 = ["abc", "xyz"]
    result2 = 6

    test3 = ["asdf", "asdf", "poi"]
    result3 = 11

    assert recursion.ch11_exercise1(test1) == result1
    assert recursion.ch11_exercise1(test2) == result2
    assert recursion.ch11_exercise1(test3) == result3

def test_ch11_exercise2():
    test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result1 = [2, 4, 6, 8, 10]

    test2 = [8, 8]
    result2 = [8, 8]

    test3 = [5]
    result3 = []

    test4 = [1, 3, 5, 8, 10, 11, 15, 16, 17]
    result4 = [8, 10, 16]

    assert recursion.ch11_exercise2(test1) == result1
    assert recursion.ch11_exercise2(test2) == result2
    assert recursion.ch11_exercise2(test3) == result3

def test_ch11_exercise3():
    test1 = 7
    result1 = 28

    test2 = 8
    result2 = 36

    test3 = 9
    result3 = 45

    assert recursion.ch11_exercise3(test1) == result1
    assert recursion.ch11_exercise3(test2) == result2
    assert recursion.ch11_exercise3(test3) == result3

def test_ch11_exercise4():
    test1 = "abcdefghijklmnopqrstuvwxyz"
    result1 = 23

    test2 = "x"
    result2 = 0

    test3 = "aax"
    result3 = 2

    test4 = "abcdxefg"
    result4 = 4

    assert recursion.ch11_exercise4(test1) == result1
    assert recursion.ch11_exercise4(test2) == result2
    assert recursion.ch11_exercise4(test3) == result3