"""
Exercises from Ch 10
Recursively Recurse With Recursion
"""

def traverse_array(list1):
    """
    Traverse a list with multiple levels of deep using a recursive function
    """
    for value in list1:
        if isinstance(value, list):
            traverse_array(value)
        else:
            print(value, end=" ")

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

traverse_array(array)