import dynamic_programming as dut

def test_add_until_100():
    test1 = [10, 20, 30]
    result1 = 60

    test2 = [10, 20, 30, 40]
    result2 = 100

    test3 = [10, 20, 30, 40, 50]
    result3 = 100

    test4 = [99, 1]
    result4 = 100

    test5 = [99, 2]
    result5 = 2

    test6 = [2, 99]
    result6 = 99

    test7 = [49, 50]
    result7 = 99

    test8 = [77]
    result8 = 77

    assert dut.add_until_100(test1) == result1
    assert dut.add_until_100(test2) == result2
    assert dut.add_until_100(test3) == result3
    assert dut.add_until_100(test4) == result4
    assert dut.add_until_100(test5) == result5
    assert dut.add_until_100(test6) == result6
    assert dut.add_until_100(test7) == result7
    assert dut.add_until_100(test8) == result8

def test_golomb():
    test1 = 1
    result1 = 1

    test2 = 2
    result2 = 2

    test3 = 3
    result3 = 2

    test4 = 4
    result4 = 3

    test5 = 5
    result5 = 3

    test6 = 6
    result6 = 4

    test7 = 7
    result7 = 4

    test8 = 8
    result8 = 4

    assert dut.golomb(test1) == result1
    assert dut.golomb(test2) == result2
    assert dut.golomb(test3) == result3
    assert dut.golomb(test4) == result4
    assert dut.golomb(test5) == result5
    assert dut.golomb(test6) == result6
    assert dut.golomb(test7) == result7
    assert dut.golomb(test8) == result8

def test_unique_paths():
    rows1 = 1
    columns1 = 1
    result1 = 1

    rows2 = 2
    columns2 = 2
    result2 = 2

    rows3 = 3
    columns3 = 3
    result3 = 6

    rows3 = 4
    columns3 = 4
    result3 = 20

    rows4 = 10
    columns4 = 10
    result4 = 48620

    assert dut.unique_paths(rows1, columns1) == result1
    assert dut.unique_paths(rows2, columns2) == result2
    assert dut.unique_paths(rows3, columns3) == result3
    assert dut.unique_paths(rows4, columns4) == result4