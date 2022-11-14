"""
Chapter 20
Techniques for Code Optimization

Exercises
The following exercises provide you with the opportunity to practice with optimizing your code.
"""

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

        for player in array_n:
            first_name = player.get("first_name")
            last_name  = player.get("last_name")
            full_name  = f"{first_name} {last_name}"

            array_n_hashmap[full_name] = True

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
    def solution(array):
        hashmap_of_array = {number: True for number in array}
        #print(f"[DEBUG] hashmap_of_array {hashmap_of_array}")
        
        for num in range(len(array)):
            if not hashmap_of_array.get(num):
                return num

    array1 = [2, 3, 0, 6, 1, 5]
    array2 = [8, 2, 3, 9, 4, 7, 5, 0, 6]

    print(array1)
    result1 = solution(array1)
    print(f"The missing number is {result1}")
    print(array2)
    result2 = solution(array2)
    print(f"The missing number is {result2}")

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
        min_price = float('inf')
        greatest_profit = 0

        for price in array:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > greatest_profit:
                    greatest_profit = profit

        return greatest_profit

    array = [10, 7, 5, 8, 11, 2, 6]

    print(array)
    result = solution(array)
    print(f"The greatest profit can be ${result}")

# Solve Questions
print(f"== Question 1 ==")
question1()
print(f"\n== Question 2 ==")
question2()
print(f"\n== Question 3 ==")
question3()