"""
Chapter 20
Techniques for Code Optimization

Exercises
The following exercises provide you with the opportunity to practice with optimizing your code.
"""
import numpy as np
from collections import defaultdict

def question1():
    """
    You're working on software that analyzes sports players. Following are two arrays of players of different sports:

    If you look carefully, you'll see that there are some players who participate in more than one kind of sport.
    Jill Huang and Wanda Vakulskas play both basketball and football.

    You are to write a function that accepts two arrays of players and returns an array of the players who play in both sports.
    In this case, that would be:

	["Jill Huang", "Wanda Vakulskas"]

    While there are players who share first names and players who share last names,
    we can assume there's only one person who has a particular full name (meaning first and last name).

    We can use a nested-loops approach, comparing each player from one array against each player from the other array,
    but this would have a runtime of O(N * M). Your job is to optimize the function so that it can run in just O(N + M).
    """
    def solution(array_n, array_m):
        array_n_hashmap = {}
        players_on_both_teams = []

        # converting the first array into a hash table
        for player in array_n:
            first_name = player.get("first_name")
            last_name  = player.get("last_name")
            full_name  = f"{first_name} {last_name}"
            array_n_hashmap[full_name] = True

        # iterating over the second array
        for player in array_m:
            first_name = player.get("first_name")
            last_name  = player.get("last_name")
            full_name  = f"{first_name} {last_name}"

            if array_n_hashmap.get(full_name):
                players_on_both_teams.append(full_name)

        return players_on_both_teams

    basketball_players = [
        {"first_name": "Jill",  "last_name": "Huang",     "team": "Gators"},
        {"first_name": "Janko", "last_name": "Barton",    "team": "Sharks"},
        {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
        {"first_name": "Jill",  "last_name": "Moloney",   "team": "Gators"},
        {"first_name": "Luuk",  "last_name": "Watkins",   "team": "Gators"}
    ]
    
    football_players = [
        {"first_name": "Hanzla", "last_name": "Radosti",   "team": "32ers"},
        {"first_name": "Tina",   "last_name": "Watkins",   "team": "Barleycorns"},
        {"first_name": "Alex",   "last_name": "Patel",     "team": "32ers"},
        {"first_name": "Jill",   "last_name": "Huang",     "team": "Barleycorns"},
        {"first_name": "Wanda",  "last_name": "Vakulskas", "team": "Barleycorns"}
    ]

    print(solution(basketball_players, football_players))

def question2():
    """
    You're writing a function that accepts an array of distinct integers from 0, 1, 2, 3…up to N.
    However, the array will be missing one integer, and your function is to return the missing one.

    For example, this array has all the integers from 0 to 6, but is missing the 4:
    [2, 3, 0, 6, 1, 5]
    Therefore, the function should return 4.

    The next example has all the integers from 0 to 9, but is missing the 1:
    [8, 2, 3, 9, 4, 7, 5, 0, 6]
    In this case, the function should return the 1.

    Using a nested-loops approach would take up to O(N^2). Your job is to optimize the code so that it has a runtime of O(N).
    """
    def my_solution(array):
        hashmap_of_array = {number: True for number in array}
        #print(f"[DEBUG] hashmap_of_array {hashmap_of_array}")
        
        for num in range(len(array)):
            if not hashmap_of_array.get(num):
                return num

    def solution(array):
        expected_sum = 0
        for e in range(1, len(array)+1):
            expected_sum += e

        actual_sum = 0
        for e in array:
            actual_sum += e

        return expected_sum - actual_sum

    array1 = [2, 3, 0, 6, 1, 5]
    array2 = [8, 2, 3, 9, 4, 7, 5, 0, 6]

    print(array1)
    result1 = solution(array1)
    print(f"The missing number is {result1}")  # result should be: 4
    print(array2)
    result2 = solution(array2)
    print(f"The missing number is {result2}")  # result should be: 1

def question3():
    """
    You're working on some more stock-prediction software. The function you're writing accepts an array of predicted prices for a particular stock over the course of time.

    For example, this array of seven prices:
    [10, 7, 5, 8, 11, 2, 6]
    predicts that a given stock will have these prices over the next seven days.
    (On Day 1, the stock will close at $10; on Day 2, the stock will close at $7; and so on.)

    Your function should calculate the greatest profit that could be made from a single “buy” transaction followed by a single “sell” transaction.

    In the previous example, the most money could be made if we bought the stock when it was worth $5 and sold it when it was worth $11.
    This yields a profit of $6 per share.

    Note that we could make even more money if we buy and sell multiple times, but for now, 
    this function focuses on the most profit that could be made from just one purchase followed by one sale.

    Now, we could use nested loops to find the profit of every possible buy-and-sell combination.
    However, this would be O(N^2) and too slow for our hotshot trading platform.
    Your job is to optimize the code so that the function clocks in at just O(N).
    """
    def solution(array):
        buy_price = float('inf')
        greatest_profit = 0

        for price in array:
            if price < buy_price:
                buy_price = price
            else:
                potential_profit = price - buy_price
                if potential_profit > greatest_profit:
                    greatest_profit = potential_profit

        return greatest_profit

    array = [10, 7, 5, 8, 11, 2, 6]

    print(array)
    result = solution(array)
    print(f"The greatest profit can be ${result}")

def question4():
    """
    You're writing a function that accepts an array of numbers and computes the highest product of any two numbers in the array.
    At first glance, this is easy, as we can just find the two greatest numbers and multiply them. However, our array can contain negative numbers and look like this:

	[5, -10, -6, 9, 4]
    In this case, it's actually the product of the two lowest numbers, -10 and -6 that yield the highest product of 60.

    We could use nested loops to multiply every possible pair of numbers, but this would take O(N^2) time.
    Your job is to optimize the function so that it's a speedy O(N).
    """
    def solution(array):
        min1 = float('inf')
        min2 = float('inf')
        max1 = float('-inf')
        max2 = float('-inf')
        for e in array:
            if e < 0:  # is negative
                if e < min1:
                    min2 = min1
                    min1 = e
                elif e < min2:
                    min2 = e
            elif e > 0:  # is positive
                if e > max1:
                    max2 = max1
                    max1 = e
                elif e > max2:
                    max2 = e

        product_of_mins = min1 * min2
        product_of_maxs = max1 * max2

        if product_of_mins >= product_of_maxs:
            return product_of_mins
        else:
            return product_of_maxs

    array = [5, -10, -6, 9, 4]
    result = solution(array)
    print(f"The greatest product of {array} is: {result}")

def question5():
    """
    You're creating software that analyzes the data of body temperature readings taken from hundreds of human patients.
    These readings are taken from healthy people and range from 97.0 degrees Fahrenheit to 99.0 degrees Fahrenheit.
    An important point: within this application, the decimal point never goes beyond the tenths place.

    Here's a sample array of temperature readings:

	[98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]
    You are to write a function that sorts these readings from lowest to highest.

    If you used a classic sorting algorithm such as Quicksort, this would take O(N log N).
    However, in this case, it's actually possible to write a faster sorting algorithm.

    Yes, that's right. Even though you've learned that the fastest sorts are O(N log N), this case is different.
    Why? In this case, there's a limited number of possibilities of what the readings will be. In such a case, we can sort these values in O(N).
    It may be N multiplied by a constant, but that's still considered O(N).
    """
    def solution(array):
        all_possibilities_ordered = [round(e, 1) for e in np.arange(97.0, 99.1, 0.1)]

        array_hashmap = defaultdict(int)
        for e in array:
            array_hashmap[e] += 1

        result = []
        for e in all_possibilities_ordered:
            if count:=array_hashmap.get(e):
                result += [e] * count

        return result

    array = [98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]
    result = solution(array)
    print(f"Original array\n{array}\nSorted array\n{result}")

def question6():
    """
    You're writing a function that accepts an array of unsorted integers and returns the length of the longest consecutive sequence among them.
    The sequence is formed by integers that increase by 1. For example, in the array:

    [10, 5, 12, 3, 55, 30, 4, 11, 2]
    the longest consecutive sequence is 2-3-4-5.
    These four integers form an increasing sequence because each integer is one greater than the previous one.
    While there's also a sequence of 10-11-12, it's only a sequence of three integers. In this case, the function should return 4,
    since that's the length of the longest consecutive sequence that can be formed from this array.

    One more example:

	[19, 13, 15, 12, 18, 14, 17, 11]
    This array's longest sequence is 11-12-13-14-15, so the function would return 5.

    If we sorted the array, we can then traverse the array just once to find the longest consecutive sequence.
    However, the sorting itself would take O(N log N). Your job is to optimize the function so that it takes O(N) time.
    """
    def solution(array):
        hashmap_of_array = {number: True for number in array}

        greatest_sequence_length = 0
        for number in array:
            if not hashmap_of_array.get(number - 1):
                sequence_count = 1
                current_number = number
                while hashmap_of_array.get(current_number + 1):
                    sequence_count += 1
                    current_number += 1

                if sequence_count > greatest_sequence_length:
                    greatest_sequence_length = sequence_count

        return greatest_sequence_length

    def sorted_bad_solution(array):
        if not array:
            return 0

        array_sorted = sorted(array)
        largest_sequence = 0
        sequence = 1

        last_idx = len(array_sorted) - 1
        for idx, number in enumerate(array_sorted):
            if idx < last_idx:
                if number + 1 == array_sorted[idx + 1]:
                    sequence += 1
                else:
                    if sequence > largest_sequence:
                        largest_sequence = sequence
                    sequence = 1
        
        if sequence > largest_sequence:
            largest_sequence = sequence
            
        return largest_sequence

    array1 = [10, 5, 12, 3, 55, 30, 4, 11, 2]  # Result expected: 4
    array2 = [19, 13, 15, 12, 18, 14, 17, 11, 20, 21, 22, 23, 24, 25, 26]  # Result expected: 5

    result1 = solution(array1)
    result2 = solution(array2)

    print(f"For {array1} the largest sequence has {result1} numbers")
    print(f"For {array2} the largest sequence has {result2} numbers")

# Solve Questions
print(f"== Question 1 ==")
question1()
print(f"\n== Question 2 ==")
question2()
print(f"\n== Question 3 ==")
question3()
print(f"\n== Question 4 ==")
question4()
print(f"\n== Question 5 ==")
question5()
print(f"\n== Question 6 ==")
question6()
