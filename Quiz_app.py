import random
import tkinter as tk
from tkinter import messagebox

#here are the dictionaries of questions of different subjects and different difficulty levels

easy_math_questions = {
    1: {
        "question": "What is the value of 2 + 2?",
        "options": {
            "a": "3",
            "b": "4",
            "c": "5",
            "d": "6"
        },
        "answer": "b"  # 4
    },
    2: {
        "question": "What is 5 multiplied by 3?",
        "options": {
            "a": "10",
            "b": "12",
            "c": "15",
            "d": "20"
        },
        "answer": "c"  # 15
    },
    3: {
        "question": "How many sides does a triangle have?",
        "options": {
            "a": "2",
            "b": "3",
            "c": "4",
            "d": "5"
        },
        "answer": "b"  # 3
    },
    4: {
        "question": "What is the square of 4?",
        "options": {
            "a": "8",
            "b": "12",
            "c": "16",
            "d": "20"
        },
        "answer": "c"  # 16
    },
    5: {
        "question": "What is the next number in the sequence: 2, 4, 6, 8, ___?",
        "options": {
            "a": "9",
            "b": "10",
            "c": "12",
            "d": "10"
        },
        "answer": "d"  # 10
    },
    6: {
        "question": "What is the result of 10 divided by 2?",
        "options": {
            "a": "3",
            "b": "4",
            "c": "5",
            "d": "5"
        },
        "answer": "d"  # 5
    },
    7: {
        "question": "What is the sum of the interior angles of a square?",
        "options": {
            "a": "180 degrees",
            "b": "270 degrees",
            "c": "360 degrees",
            "d": "450 degrees"
        },
        "answer": "c"  # 360 degrees
    },
    8: {
        "question": "How many centimeters are in a meter?",
        "options": {
            "a": "10",
            "b": "50",
            "c": "100",
            "d": "1000"
        },
        "answer": "c"  # 100
    },
    9: {
        "question": "What is the perimeter of a rectangle with sides of length 4 and 6 units?",
        "options": {
            "a": "12 units",
            "b": "20 units",
            "c": "24 units",
            "d": "30 units"
        },
        "answer": "c"  # 24 units
    },
    10: {
        "question": "What is the value of 3 squared?",
        "options": {
            "a": "6",
            "b": "9",
            "c": "12",
            "d": "9"
        },
        "answer": "b"  # 9
    },
    11: {
        "question": "How many degrees are there in a right angle?",
        "options": {
            "a": "45 degrees",
            "b": "90 degrees",
            "c": "180 degrees",
            "d": "360 degrees"
        },
        "answer": "b"  # 90 degrees
    },
    12: {
        "question": "What is the next prime number after 7?",
        "options": {
            "a": "8",
            "b": "10",
            "c": "11",
            "d": "12"
        },
        "answer": "c"  # 11
    },
    13: {
        "question": "If a rectangle has a length of 8 units and a width of 5 units, what is its area?",
        "options": {
            "a": "20 square units",
            "b": "30 square units",
            "c": "40 square units",
            "d": "50 square units"
        },
        "answer": "b"  # 40 square units
    },
    14: {
        "question": "What is the value of 7 multiplied by 9?",
        "options": {
            "a": "56",
            "b": "63",
            "c": "72",
            "d": "81"
        },
        "answer": "b"  # 63
    },
    15: {
        "question": "How many sides does a hexagon have?",
        "options": {
            "a": "4",
            "b": "5",
            "c": "6",
            "d": "7"
        },
        "answer": "c"  # 6
    },
    16: {
        "question": "What is the result of 15 minus 7?",
        "options": {
            "a": "6",
            "b": "8",
            "c": "9",
            "d": "10"
        },
        "answer": "b"  # 8
    },
    17: {
        "question": "What is the square root of 49?",
        "options": {
            "a": "5",
            "b": "6",
            "c": "7",
            "d": "8"
        },
        "answer": "c"  # 7
    },
    18: {
        "question": "How many millimeters are in a centimeter?",
        "options": {
            "a": "10",
            "b": "100",
            "c": "1000",
            "d": "10,000"
        },
        "answer": "a"  # 10
    },
    19: {
        "question": "What is the sum of the first 5 prime numbers?",
        "options": {
            "a": "10",
            "b": "15",
            "c": "20",
            "d": "25"
        },
        "answer": "b"  # 15
    },
    20: {
        "question": "What is the value of 6 squared?",
        "options": {
            "a": "12",
            "b": "24",
            "c": "36",
            "d": "48"
        },
        "answer": "c"  # 36
    },
    21: {
        "question": "How many sides does a pentagon have?",
        "options": {
            "a": "4",
            "b": "5",
            "c": "6",
            "d": "7"
        },
        "answer": "b"  # 5
    },
    22: {
        "question": "What is the result of 20 divided by 5?",
        "options": {
            "a": "2",
            "b": "3",
            "c": "4",
            "d": "5"
        },
        "answer": "d"  # 4
    },
    23: {
        "question": "What is the area of a square with a side length of 7 units?",
        "options": {
            "a": "21 square units",
            "b": "28 square units",
            "c": "35 square units",
            "d": "49 square units"
        },
        "answer": "d"  # 49 square units
    },
    24: {
        "question": "What is the sum of the angles in a triangle?",
        "options": {
            "a": "90 degrees",
            "b": "180 degrees",
            "c": "270 degrees",
            "d": "360 degrees"
        },
        "answer": "b"  # 180 degrees
    },
    25: {
        "question": "How many centimeters are in a meter?",
        "options": {
            "a": "10",
            "b": "50",
            "c": "100",
            "d": "1000"
        },
        "answer": "c"  # 100
    },
    26: {
        "question": "What is the value of 4 cubed?",
        "options": {
            "a": "16",
            "b": "32",
            "c": "64",
            "d": "128"
        },
        "answer": "c"  # 64
    },
    27: {
        "question": "If a rectangle has a length of 10 units and a width of 3 units, what is its perimeter?",
        "options": {
            "a": "20 units",
            "b": "26 units",
            "c": "32 units",
            "d": "36 units"
        },
        "answer": "c"  # 32 units
    },
    28: {
        "question": "What is the next prime number after 13?",
        "options": {
            "a": "14",
            "b": "15",
            "c": "16",
            "d": "17"
        },
        "answer": "d"  # 17
    },
    29: {
        "question": "What is the result of 25 minus 9?",
        "options": {
            "a": "14",
            "b": "16",
            "c": "18",
            "d": "22"
        },
        "answer": "c"  # 16
    },
    30: {
        "question": "What is the square root of 64?",
        "options": {
            "a": "6",
            "b": "7",
            "c": "8",
            "d": "9"
        },
        "answer": "c"  # 8
    },
    31: {
        "question": "How many millimeters are in a centimeter?",
        "options": {
            "a": "10",
            "b": "100",
            "c": "1000",
            "d": "10,000"
        },
        "answer": "a"  # 10
    },
    32: {
        "question": "What is the sum of the first 5 even numbers?",
        "options": {
            "a": "10",
            "b": "15",
            "c": "20",
            "d": "25"
        },
        "answer": "c"  # 20
    },
    33: {
        "question": "What is the value of 5 squared?",
        "options": {
            "a": "10",
            "b": "15",
            "c": "25",
            "d": "30"
        },
        "answer": "c"  # 25
    },
    34: {
        "question": "How many sides does a heptagon have?",
        "options": {
            "a": "5",
            "b": "6",
            "c": "7",
            "d": "8"
        },
        "answer": "c"  # 7
    },
    35: {
        "question": "What is the result of 16 divided by 4?",
        "options": {
            "a": "3",
            "b": "4",
            "c": "5",
            "d": "6"
        },
        "answer": "b"  # 4
    },
    36: {
        "question": "What is the area of a rectangle with a length of 6 units and a width of 4 units?",
        "options": {
            "a": "10 square units",
            "b": "16 square units",
            "c": "20 square units",
            "d": "24 square units"
        },
        "answer": "b"  # 16 square units
    },
    37: {
        "question": "What is the sum of the angles in a square?",
        "options": {
            "a": "180 degrees",
            "b": "270 degrees",
            "c": "360 degrees",
            "d": "450 degrees"
        },
        "answer": "c"  # 360 degrees
    },
    38: {
        "question": "How many millimeters are in a centimeter?",
        "options": {
            "a": "10",
            "b": "100",
            "c": "1000",
            "d": "10,000"
        },
        "answer": "a"  # 10
    },
    39: {
        "question": "What is the value of 3 cubed?",
        "options": {
            "a": "6",
            "b": "9",
            "c": "27",
            "d": "81"
        },
        "answer": "c"  # 27
    },
    40: {
        "question": "If a rectangle has a length of 12 units and a width of 7 units, what is its perimeter?",
        "options": {
            "a": "22 units",
            "b": "26 units",
            "c": "30 units",
            "d": "36 units"
        },
        "answer": "a"  # 22 units
    },
    41: {
        "question": "What is the next prime number after 19?",
        "options": {
            "a": "20",
            "b": "21",
            "c": "22",
            "d": "23"
        },
        "answer": "d"  # 23
    },
    42: {
        "question": "What is the result of 30 minus 8?",
        "options": {
            "a": "20",
            "b": "22",
            "c": "24",
            "d": "28"
        },
        "answer": "b"  # 22
    },
    43: {
        "question": "What is the square root of 81?",
        "options": {
            "a": "7",
            "b": "8",
            "c": "9",
            "d": "10"
        },
        "answer": "c"  # 9
    },
    44: {
        "question": "How many millimeters are in a meter?",
        "options": {
            "a": "10",
            "b": "100",
            "c": "1000",
            "d": "10,000"
        },
        "answer": "c"  # 1000
    },
    45: {
        "question": "What is the sum of the first 5 odd numbers?",
        "options": {
            "a": "15",
            "b": "20",
            "c": "25",
            "d": "30"
        },
        "answer": "a"  # 15
    },
    46: {
        "question": "What is the value of 7 squared?",
        "options": {
            "a": "42",
            "b": "49",
            "c": "56",
            "d": "64"
        },
        "answer": "b"  # 49
    },
    47: {
        "question": "How many sides does an octagon have?",
        "options": {
            "a": "6",
            "b": "7",
            "c": "8",
            "d": "9"
        },
        "answer": "c"  # 8
    },
    48: {
        "question": "What is the result of 18 divided by 3?",
        "options": {
            "a": "4",
            "b": "5",
            "c": "6",
            "d": "7"
        },
        "answer": "c"  # 6
    },
    49: {
        "question": "What is the area of a square with a side length of 10 units?",
        "options": {
            "a": "80 square units",
            "b": "90 square units",
            "c": "100 square units",
            "d": "110 square units"
        },
        "answer": "c"  # 100 square units
    },
    50: {
        "question": "What is the sum of the angles in a triangle?",
        "options": {
            "a": "90 degrees",
            "b": "180 degrees",
            "c": "270 degrees",
            "d": "360 degrees"
        },
        "answer": "b"  # 180 degrees
    },
    51: {
        "question": "How many millimeters are in a centimeter?",
        "options": {
            "a": "10",
            "b": "100",
            "c": "1000",
            "d": "10,000"
        },
        "answer": "a"  # 10
    },
    52: {
        "question": "What is the value of 5 cubed?",
        "options": {
            "a": "125",
            "b": "150",
            "c": "175",
            "d": "200"
        },
        "answer": "a"  # 125
    },
    53: {
        "question": "If a rectangle has a length of 15 units and a width of 4 units, what is its perimeter?",
        "options": {
            "a": "30 units",
            "b": "38 units",
            "c": "42 units",
            "d": "54 units"
        },
        "answer": "b"  # 38 units
    },
    54: {
        "question": "What is the next prime number after 29?",
        "options": {
            "a": "31",
            "b": "32",
            "c": "33",
            "d": "34"
        },
        "answer": "a"  # 31
    },
    55: {
        "question": "What is the result of 35 minus 9?",
        "options": {
            "a": "20",
            "b": "24",
            "c": "26",
            "d": "28"
        },
        "answer": "c"  # 26
    },
    56: {
        "question": "What is the square root of 100?",
        "options": {
            "a": "8",
            "b": "9",
            "c": "10",
            "d": "11"
        },
        "answer": "c"  # 10
    },
    57: {
        "question": "How many millimeters are in a centimeter?",
        "options": {
            "a": "1",
            "b": "10",
            "c": "100",
            "d": "1000"
        },
        "answer": "b"  # 10
    },
    58: {
        "question": "What is the sum of the first 5 prime numbers?",
        "options": {
            "a": "10",
            "b": "15",
            "c": "20",
            "d": "25"
        },
        "answer": "b"  # 15
    },
    59: {
        "question": "What is the value of 4 squared?",
        "options": {
            "a": "12",
            "b": "14",
            "c": "16",
            "d": "18"
        },
        "answer": "c"  # 16
    },
    60: {
        "question": "How many sides does a hexagon have?",
        "options": {
            "a": "5",
            "b": "6",
            "c": "7",
            "d": "8"
        },
        "answer": "b"  # 6
    },
    61: {
        "question": "What is the result of 2 multiplied by 2?",
        "options": {
            "a": "3",
            "b": "4",
            "c": "5",
            "d": "6"
        },
        "answer": "b"  # 4
    },
    62: {
        "question": "What is the sum of the interior angles of a triangle?",
        "options": {
            "a": "90 degrees",
            "b": "180 degrees",
            "c": "270 degrees",
            "d": "360 degrees"
        },
        "answer": "b"  # 180 degrees
    },
    63: {
        "question": "What is the value of 3 squared?",
        "options": {
            "a": "6",
            "b": "9",
            "c": "12",
            "d": "15"
        },
        "answer": "b"  # 9
    },
    64: {
        "question": "How many sides does a pentagon have?",
        "options": {
            "a": "4",
            "b": "5",
            "c": "6",
            "d": "7"
        },
        "answer": "b"  # 5
    },
    65: {
        "question": "What is the next prime number after 7?",
        "options": {
            "a": "8",
            "b": "10",
            "c": "11",
            "d": "12"
        },
        "answer": "c"  # 11
    },
    66: {
        "question": "What is the result of 4 multiplied by 5?",
        "options": {
            "a": "16",
            "b": "18",
            "c": "20",
            "d": "22"
        },
        "answer": "c"  # 20
    },
    67: {
        "question": "How many degrees are there in a circle?",
        "options": {
            "a": "90",
            "b": "180",
            "c": "270",
            "d": "360"
        },
        "answer": "d"  # 360
    },
    68: {
        "question": "What is the value of 7 squared?",
        "options": {
            "a": "42",
            "b": "49",
            "c": "56",
            "d": "64"
        },
        "answer": "b"  # 49
    },
    69: {
        "question": "How many sides does a hexagon have?",
        "options": {
            "a": "4",
            "b": "5",
            "c": "6",
            "d": "7"
        },
        "answer": "c"  # 6
    },
    70: {
        "question": "What is the next prime number after 17?",
        "options": {
            "a": "18",
            "b": "19",
            "c": "20",
            "d": "21"
        },
        "answer": "b"  # 19
    },
    71: {
        "question": "What is the value of 8 squared?",
        "options": {
            "a": "60",
            "b": "62",
            "c": "64",
            "d": "66"
        },
        "answer": "c"  # 64
    },
    72: {
        "question": "How many sides does an octagon have?",
        "options": {
            "a": "6",
            "b": "7",
            "c": "8",
            "d": "9"
        },
        "answer": "c"  # 8
    },
    73: {
        "question": "What is the square root of 36?",
        "options": {
            "a": "4",
            "b": "5",
            "c": "6",
            "d": "7"
        },
        "answer": "c"  # 6
    },
    74: {
        "question": "How many millimeters are in a centimeter?",
        "options": {
            "a": "5",
            "b": "10",
            "c": "50",
            "d": "100"
        },
        "answer": "b"  # 10
    },
    75: {
        "question": "What is the value of 3 cubed?",
        "options": {
            "a": "6",
            "b": "9",
            "c": "27",
            "d": "30"
        },
        "answer": "c"  # 27
    },
    76: {
        "question": "What is the value of 5 squared?",
        "options": {
            "a": "20",
            "b": "25",
            "c": "30",
            "d": "35"
        },
        "answer": "b"  # 25
    },
    77: {
        "question": "How many sides does a triangle have?",
        "options": {
            "a": "2",
            "b": "3",
            "c": "4",
            "d": "5"
        },
        "answer": "b"  # 3
    },
    78: {
        "question": "What is the next prime number after 13?",
        "options": {
            "a": "14",
            "b": "15",
            "c": "16",
            "d": "17"
        },
        "answer": "d"  # 17
    },
    79: {
        "question": "What is the result of 25 divided by 5?",
        "options": {
            "a": "3",
            "b": "4",
            "c": "5",
            "d": "6"
        },
        "answer": "c"  # 5
    },
    80: {
        "question": "What is the sum of the first 5 natural numbers?",
        "options": {
            "a": "10",
            "b": "15",
            "c": "20",
            "d": "25"
        },
        "answer": "b"  # 15
    },
     81: {
        "question": "What is the value of 6 multiplied by 7?",
        "options": {
            "a": "36",
            "b": "42",
            "c": "48",
            "d": "54"
        },
        "answer": "b"  # 42
    },
    82: {
        "question": "How many sides does a heptagon have?",
        "options": {
            "a": "6",
            "b": "7",
            "c": "8",
            "d": "9"
        },
        "answer": "b"  # 7
    },
    83: {
        "question": "What is the square root of 49?",
        "options": {
            "a": "6",
            "b": "7",
            "c": "8",
            "d": "9"
        },
        "answer": "b"  # 7
    },
    84: {
        "question": "How many centimeters are in a meter?",
        "options": {
            "a": "10",
            "b": "50",
            "c": "100",
            "d": "1000"
        },
        "answer": "c"  # 100
    },
    85: {
        "question": "What is the sum of the interior angles of a quadrilateral?",
        "options": {
            "a": "180 degrees",
            "b": "270 degrees",
            "c": "360 degrees",
            "d": "450 degrees"
        },
        "answer": "c"  # 360 degrees
    },
    86: {
        "question": "What is the value of 9 squared?",
        "options": {
            "a": "72",
            "b": "81",
            "c": "90",
            "d": "99"
        },
        "answer": "b"  # 81
    },
    87: {
        "question": "How many sides does a decagon have?",
        "options": {
            "a": "8",
            "b": "9",
            "c": "10",
            "d": "11"
        },
        "answer": "c"  # 10
    },
    88: {
        "question": "What is the result of 40 divided by 5?",
        "options": {
            "a": "6",
            "b": "7",
            "c": "8",
            "d": "9"
        },
        "answer": "c"  # 8
    },
    89: {
        "question": "What is the square root of 64?",
        "options": {
            "a": "6",
            "b": "7",
            "c": "8",
            "d": "9"
        },
        "answer": "c"  # 8
    },
    90: {
        "question": "What is the sum of the angles in a pentagon?",
        "options": {
            "a": "360 degrees",
            "b": "450 degrees",
            "c": "540 degrees",
            "d": "630 degrees"
        },
        "answer": "a"  # 360 degrees
    },
    91: {
        "question": "What is the result of 15 multiplied by 3?",
        "options": {
            "a": "35",
            "b": "40",
            "c": "45",
            "d": "50"
        },
        "answer": "c"  # 45
    },
    92: {
        "question": "How many sides does a nonagon have?",
        "options": {
            "a": "7",
            "b": "8",
            "c": "9",
            "d": "10"
        },
        "answer": "c"  # 9
    },
    93: {
        "question": "What is the value of 11 squared?",
        "options": {
            "a": "110",
            "b": "121",
            "c": "132",
            "d": "143"
        },
        "answer": "b"  # 121
    },
    94: {
        "question": "How many millimeters are in a meter?",
        "options": {
            "a": "10",
            "b": "100",
            "c": "1000",
            "d": "10000"
        },
        "answer": "c"  # 1000
    },
    95: {
        "question": "What is the sum of the interior angles of a hexagon?",
        "options": {
            "a": "360 degrees",
            "b": "450 degrees",
            "c": "540 degrees",
            "d": "630 degrees"
        },
        "answer": "a"  # 360 degrees
    },
    96: {
        "question": "What is the result of 24 divided by 4?",
        "options": {
            "a": "4",
            "b": "6",
            "c": "8",
            "d": "10"
        },
        "answer": "c"  # 8
    },
    97: {
        "question": "What is the value of 12 squared?",
        "options": {
            "a": "120",
            "b": "132",
            "c": "144",
            "d": "156"
        },
        "answer": "c"  # 144
    },
    98: {
        "question": "How many sides does a dodecagon have?",
        "options": {
            "a": "10",
            "b": "11",
            "c": "12",
            "d": "13"
        },
        "answer": "c"  # 12
    },
    99: {
        "question": "What is the square root of 100?",
        "options": {
            "a": "9",
            "b": "10",
            "c": "11",
            "d": "12"
        },
        "answer": "b"  # 10
    },
    100: {
        "question": "What is the sum of the angles in a quadrilateral?",
        "options": {
            "a": "180 degrees",
            "b": "270 degrees",
            "c": "360 degrees",
            "d": "450 degrees"
        },
        "answer": "c"  # 360 degrees
    }
}

medium_math_questions = {
    1: {
        "question": "What is the value of sin(45\u00b0) * cos(45\u00b0)?",
        "options": {
            "a": "1/2",
            "b": "1/4",
            "c": "sqrt(2)/2",
            "d": "1"
        },
        "answer": "a"
    },
    2: {
        "question": "If P(A) = 0.4, P(B) = 0.3, and P(A \u2229 B) = 0.1, what is P(A | B)?",
        "options": {
            "a": "0.25",
            "b": "0.30",
            "c": "0.33",
            "d": "0.50"
        },
        "answer": "c"
    },
    3: {
        "question": "What is the determinant of the matrix [[2, 4], [3, 6]]?",
        "options": {
            "a": "0",
            "b": "2",
            "c": "6",
            "d": "12"
        },
        "answer": "a"
    },
    4: {
        "question": "What is the solution to the differential equation dy/dx = x^2?",
        "options": {
            "a": "x^3 + C",
            "b": "x^2 + C",
            "c": "(1/3)x^3 + C",
            "d": "(1/2)x^2 + C"
        },
        "answer": "c"
    },
    5: {
        "question": "What is the integral of e^x dx?",
        "options": {
            "a": "e^x + C",
            "b": "ln(x) + C",
            "c": "1/x + C",
            "d": "cos(x) + C"
        },
        "answer": "a"
    },
    6: {
        "question": "What is the value of tan(60\u00b0)?",
        "options": {
            "a": "sqrt(3)",
            "b": "1/sqrt(3)",
            "c": "1",
            "d": "0"
        },
        "answer": "a"
    },
    7: {
        "question": "If two cards are drawn from a standard deck of 52 playing cards without replacement, what is the probability that both cards are aces?",
        "options": {
            "a": "1/221",
            "b": "1/169",
            "c": "1/132",
            "d": "1/102"
        },
        "answer": "c"
    },
    8: {
        "question": "What is the cross product of the vectors [1, 2, -1] and [3, -1, 2]?",
        "options": {
            "a": "[5, -5, -5]",
            "b": "[5, 5, 5]",
            "c": "[-5, 5, -5]",
            "d": "[-5, -5, 5]"
        },
        "answer": "a"
    },
    9: {
        "question": "What is the solution to the differential equation dy/dx = y, given that y(0) = 2?",
        "options": {
            "a": "2e^x",
            "b": "2e^-x",
            "c": "2e^2x",
            "d": "2e^-2x"
        },
        "answer": "a"
    },
    10: {
        "question": "What is the integral of 1/(x^2 + 1) dx?",
        "options": {
            "a": "tan^-1(x) + C",
            "b": "cot^-1(x) + C",
            "c": "sec^-1(x) + C",
            "d": "csc^-1(x) + C"
        },
        "answer": "a"
    },
    11: {
        "question": "What is the value of cos(\u03c0/3)?",
        "options": {
            "a": "1/2",
            "b": "sqrt(3)/2",
            "c": "1",
            "d": "sqrt(2)/2"
        },
        "answer": "b"
    },
    12: {
        "question": "If two dice are rolled, what is the probability of getting a sum of 7?",
        "options": {
            "a": "1/6",
            "b": "1/12",
            "c": "1/9",
            "d": "1/8"
        },
        "answer": "c"
    },
    13: {
        "question": "What is the inverse of the matrix [[2, -1], [3, 4]]?",
        "options": {
            "a": "[[2, 1], [3, 4]]",
            "b": "[[4, -1], [3, 2]]",
            "c": "[[4, 1], [3, 2]]",
            "d": "[[4, -1], [2, 3]]"
        },
        "answer": "b"
    },
    14: {
        "question": "What is the solution to the differential equation dy/dx = y^2, given that y(0) = 1?",
        "options": {
            "a": "1/(1 - x)",
            "b": "1/(1 + x)",
            "c": "1/(1 - x^2)",
            "d": "1/(1 + x^2)"
        },
        "answer": "a"
    },
    15: {
        "question": "What is the integral of e^(2x)sin(x) dx?",
        "options": {
            "a": "1/5 e^(2x) (2 sin(x) - cos(x)) + C",
            "b": "1/5 e^(2x) (2 cos(x) - sin(x)) + C",
            "c": "1/5 e^(2x) (2 sin(x) + cos(x)) + C",
            "d": "1/5 e^(2x) (sin(x) + 2 cos(x)) + C"
        },
        "answer": "a"
    },
    16: {
        "question": "What is the value of tan(\u03c0/4)?",
        "options": {
            "a": "1",
            "b": "sqrt(3)",
            "c": "1/2",
            "d": "sqrt(2)"
        },
        "answer": "a"
    },
    17: {
        "question": "If a card is drawn from a standard deck of 52 playing cards, what is the probability that it is a face card?",
        "options": {
            "a": "1/13",
            "b": "3/13",
            "c": "1/4",
            "d": "3/4"
        },
        "answer": "c"
    },
    18: {
        "question": "What is the dot product of the vectors [1, -2, 3] and [2, 3, 4]?",
        "options": {
            "a": "5",
            "b": "9",
            "c": "11",
            "d": "15"
        },
        "answer": "b"
    },
    19: {
        "question": "What is the solution to the differential equation dy/dx = x^3, given that y(0) = 0?",
        "options": {
            "a": "x^4/4",
            "b": "x^5/5",
            "c": "x^6/6",
            "d": "x^7/7"
        },
        "answer": "b"
    },
    20: {
        "question": "What is the integral of 1/(x^2 - 1) dx?",
        "options": {
            "a": "1/2 ln|x - 1| - 1/2 ln|x + 1| + C",
            "b": "ln|x - 1| - ln|x + 1| + C",
            "c": "1/2 ln|x - 1| + 1/2 ln|x + 1| + C",
            "d": "ln|x - 1| + ln|x + 1| + C"
        },
        "answer": "a"
    },
    21: {
        "question": "What is the value of sec(\u03c0/6)?",
        "options": {
            "a": "sqrt(3)/2",
            "b": "2",
            "c": "2sqrt(3)",
            "d": "1/2"
        },
        "answer": "b"
    },
    22: {
        "question": "If three cards are drawn from a standard deck of 52 playing cards without replacement, what is the probability that all three cards are red?",
        "options": {
            "a": "1/52",
            "b": "1/26",
            "c": "1/13",
            "d": "1/4"
        },
        "answer": "d"
    },
    23: {
        "question": "What is the cross product of the vectors [2, -3, 1] and [4, 5, -2]?",
        "options": {
            "a": "[-7, -10, -7]",
            "b": "[-7, -10, 7]",
            "c": "[7, -10, -7]",
            "d": "[7, 10, -7]"
        },
        "answer": "a"
    },
    24: {
        "question": "What is the solution to the differential equation dy/dx = y^3, given that y(0) = 1?",
        "options": {
            "a": "(3x + 1)/(3x - 1)",
            "b": "(3x - 1)/(3x + 1)",
            "c": "(1 - 3x)/(1 + 3x)",
            "d": "(1 + 3x)/(1 - 3x)"
        },
        "answer": "b"
    },
    25: {
        "question": "What is the integral of x^2 e^x dx?",
        "options": {
            "a": "(x^2 - 2x + 2)e^x + C",
            "b": "(x^2 + 2x + 2)e^x + C",
            "c": "(x^2 + 2x + 2)e^-x + C",
            "d": "(x^2 - 2x + 2)e^-x + C"
        },
        "answer": "d"
    },
    26: {
        "question": "What is the value of cos(\u03c0/6)?",
        "options": {
            "a": "1/2",
            "b": "sqrt(3)/2",
            "c": "sqrt(2)/2",
            "d": "1"
        },
        "answer": "b"
    },
    27: {
        "question": "If two cards are drawn from a standard deck of 52 playing cards without replacement, what is the probability that both cards are red?",
        "options": {
            "a": "1/26",
            "b": "25/102",
            "c": "1/13",
            "d": "13/51"
        },
        "answer": "b"
    },
    28: {
        "question": "What is the determinant of the matrix [[3, -1], [5, 2]]?",
        "options": {
            "a": "-11",
            "b": "11",
            "c": "-13",
            "d": "13"
        },
        "answer": "b"
    },
    29: {
        "question": "What is the integral of e^x sin(x) dx?",
        "options": {
            "a": "1/2 (e^x sin(x) - e^x cos(x)) + C",
            "b": "1/2 (e^x sin(x) + e^x cos(x)) + C",
            "c": "1/2 (e^x sin(x) - e^-x cos(x)) + C",
            "d": "1/2 (e^x sin(x) + e^-x cos(x)) + C"
        },
        "answer": "c"
    },
    30: {
        "question": "What is the value of sin(\u03c0/4)?",
        "options": {
            "a": "1/2",
            "b": "sqrt(3)/2",
            "c": "sqrt(2)/2",
            "d": "1"
        },
        "answer": "c"
    },
    31: {
        "question": "What is the dot product of the vectors [2, -1, 3] and [4, 3, -2]?",
        "options": {
            "a": "5",
            "b": "9",
            "c": "11",
            "d": "15"
        },
        "answer": "b"
    },
    32: {
        "question": "What is the value of tan(\u03c0/6)?",
        "options": {
            "a": "sqrt(3)/3",
            "b": "1",
            "c": "sqrt(3)",
            "d": "1/sqrt(3)"
        },
        "answer": "a"
    },
    33: {
        "question": "If two cards are drawn from a standard deck of 52 playing cards without replacement, what is the probability that both cards are red?",
        "options": {
            "a": "1/13",
            "b": "25/102",
            "c": "1/4",
            "d": "13/51"
        },
        "answer": "b"
    }
}

hard_math_questions = {
    1: {
        "question": "What is the limit of (x^2 - 4)/(x - 2) as x approaches 2?",
        "options": {
            "a": "2",
            "b": "4",
            "c": "6",
            "d": "8"
        },
        "answer": "b"
    },
    2: {
        "question": "What is the limit of 1/x as x approaches infinity?",
        "options": {
            "a": "0",
            "b": "1",
            "c": "infinity",
            "d": "undefined"
        },
        "answer": "a"
    },
    3: {
        "question": "Which of the following is not a field?",
        "options": {
            "a": "R (real numbers)",
            "b": "Q (rational numbers)",
            "c": "Z (integers)",
            "d": "C (complex numbers)"
        },
        "answer": "c"
    },
    4: {
        "question": "What is the fundamental group of a circle?",
        "options": {
            "a": "Z (integers)",
            "b": "R (real numbers)",
            "c": "Q (rational numbers)",
            "d": "C (complex numbers)"
        },
        "answer": "a"
    },
    5: {
        "question": "What is the curvature of a flat plane?",
        "options": {
            "a": "0",
            "b": "1",
            "c": "\u03c0",
            "d": "\u221e"
        },
        "answer": "a"
    },
    6: {
        "question": "Which of the following is a prime number?",
        "options": {
            "a": "14",
            "b": "21",
            "c": "33",
            "d": "37"
        },
        "answer": "d"
    },
    7: {
        "question": "Which of the following problems is NP-hard?",
        "options": {
            "a": "Sorting",
            "b": "Matrix multiplication",
            "c": "Traveling salesman",
            "d": "Finding prime numbers"
        },
        "answer": "c"
    },
    8: {
        "question": "Which of the following spaces is a Banach space?",
        "options": {
            "a": "L^1(R)",
            "b": "L^2(R)",
            "c": "L^\u221e(R)",
            "d": "C[0,1]"
        },
        "answer": "a"
    },
    9: {
        "question": "What is the dimension of a sphere?",
        "options": {
            "a": "0",
            "b": "1",
            "c": "2",
            "d": "3"
        },
        "answer": "d"
    },
    10: {
        "question": "What is the Euler characteristic of a torus?",
        "options": {
            "a": "0",
            "b": "1",
            "c": "2",
            "d": "-1"
        },
        "answer": "a"
    },
    11: {
        "question": "What is the limit of sin(1/x) as x approaches 0?",
        "options": {
            "a": "0",
            "b": "1",
            "c": "Does not exist",
            "d": "Infinity"
        },
        "answer": "c"
    },
    12: {
        "question": "Which of the following is an example of a non-Abelian group?",
        "options": {
            "a": "Cyclic group",
            "b": "Dihedral group",
            "c": "Symmetric group",
            "d": "Quaternion group"
        },
        "answer": "d"
    },
    13: {
        "question": "What is the Euler characteristic of a projective plane?",
        "options": {
            "a": "0",
            "b": "1",
            "c": "2",
            "d": "-1"
        },
        "answer": "d"
    },
    14: {
        "question": "What is the Jacobian determinant of the transformation (x, y) -> (2x, 3y)?",
        "options": {
            "a": "2",
            "b": "3",
            "c": "6",
            "d": "9"
        },
        "answer": "c"
    },
    15: {
        "question": "What is the residue of 1/(z^2 + 1) at z = i?",
        "options": {
            "a": "1",
            "b": "i",
            "c": "-1",
            "d": "-i"
        },
        "answer": "d"
    },
    16: {
        "question": "What is the nth term of the Fibonacci sequence?",
        "options": {
            "a": "n-1 + n-2",
            "b": "n^2",
            "c": "2n",
            "d": "n!"
        },
        "answer": "a"
    },
    17: {
        "question": "What is the dual of the statement 'There exists x such that P(x)'?",
        "options": {
            "a": "For all x, not P(x)",
            "b": "For all x, P(x)",
            "c": "There exists x, P(x)",
            "d": "There exists x, not P(x)"
        },
        "answer": "b"
    },
    18: {
        "question": "What is the degree of a differentiable function?",
        "options": {
            "a": "1",
            "b": "2",
            "c": "n",
            "d": "Infinity"
        },
        "answer": "d"
    },
    19: {
        "question": "What is the determinant of the identity matrix?",
        "options": {
            "a": "0",
            "b": "1",
            "c": "-1",
            "d": "Depends on the size of the matrix"
        },
        "answer": "b"
    },
    20: {
        "question": "What is the nth derivative of e^x?",
        "options": {
            "a": "e^x",
            "b": "x^n e^x",
            "c": "x e^x",
            "d": "x^n e^x"
        },
        "answer": "a"
    },
    21: {
        "question": "What is the limit of 1/x as x approaches 0 from the right?",
        "options": {
            "a": "0",
            "b": "1",
            "c": "Infinity",
            "d": "Does not exist"
        },
        "answer": "c"
    },
    22: {
        "question": "Which of the following is not a property of a ring?",
        "options": {
            "a": "Commutativity of addition",
            "b": "Existence of multiplicative identity",
            "c": "Existence of multiplicative inverses",
            "d": "Associativity of multiplication"
        },
        "answer": "c"
    },
    23: {
        "question": "What is the Euler characteristic of a Klein bottle?",
        "options": {
            "a": "0",
            "b": "1",
            "c": "2",
            "d": "-1"
        },
        "answer": "d"
    },
    24: {
        "question": "What is the determinant of the matrix [[a, b], [c, d]]?",
        "options": {
            "a": "ad - bc",
            "b": "ac - bd",
            "c": "a + d",
            "d": "b + c"
        },
        "answer": "a"
    },
    25: {
        "question": "What is the residue of 1/(z - 1)^3 at z = 1?",
        "options": {
            "a": "0",
            "b": "1/2",
            "c": "1",
            "d": "Infinity"
        },
        "answer": "d"
    },
    26: {
        "question": "What is the nth term of the geometric sequence with first term a and common ratio r?",
        "options": {
            "a": "a * r^(n-1)",
            "b": "a * r^n",
            "c": "a + r^n",
            "d": "a + r^(n-1)"
        },
        "answer": "a"
    },
    27: {
        "question": "What is the dual of the statement 'For all x, P(x)'?",
        "options": {
            "a": "There exists x, not P(x)",
            "b": "There exists x, P(x)",
            "c": "For all x, P(x)",
            "d": "For all x, not P(x)"
        },
        "answer": "a"
    },
    28: {
        "question": "What is the degree of a polynomial function?",
        "options": {
            "a": "1",
            "b": "2",
            "c": "n",
            "d": "Depends on the highest power of x"
        },
        "answer": "d"
    },
    29: {
        "question": "What is the determinant of a diagonal matrix?",
        "options": {
            "a": "0",
            "b": "1",
            "c": "Product of diagonal entries",
            "d": "Depends on the size of the matrix"
        },
        "answer": "c"
    },
    30: {
        "question": "What is the nth derivative of x^n?",
        "options": {
            "a": "n!",
            "b": "x^(n-1)",
            "c": "nx^(n-1)",
            "d": "n^n"
        },
        "answer": "a"
    },
    31: {
        "question": "What is the limit of (sin(x))/x as x approaches 0?",
        "options": {
            "a": "0",
            "b": "1",
            "c": "Does not exist",
            "d": "Infinity"
        },
        "answer": "b"
    },
    32: {
        "question": "Which of the following is not a property of a group?",
        "options": {
            "a": "Closure",
            "b": "Associativity",
            "c": "Existence of additive identity",
            "d": "Existence of multiplicative inverses"
        },
        "answer": "c"
    },
    33: {
        "question": "What is the Euler characteristic of a sphere?",
        "options": {
            "a": "0",
            "b": "1",
            "c": "2",
            "d": "-1"
        },
        "answer": "b"
    },
    34: {
        "question": "What is the eigenvalue of the identity matrix?",
        "options": {
            "a": "0",
            "b": "1",
            "c": "-1",
            "d": "Depends on the size of the matrix"
        },
        "answer": "b"
    },
    35: {
        "question": "What is the limit of (1 - cos(x))/x as x approaches 0?",
        "options": {
            "a": "0",
            "b": "1",
            "c": "Does not exist",
            "d": "Infinity"
        },
        "answer": "a"
    }
}

easy_reasoning_questions = {
    1: {
        "question": "If all cats can fly and Tom is a cat, can Tom fly?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    2: {
        "question": "If all birds can swim and a penguin is a bird, can a penguin swim?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    3: {
        "question": "If all squares are circles and a triangle is a square, is a triangle a circle?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    4: {
        "question": "If all apples are oranges and a banana is not an apple, is a banana an orange?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    5: {
        "question": "If all cars are buses and a bicycle is not a car, is a bicycle a bus?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    6: {
        "question": "If all roses are red and a violet is not a rose, is a violet red?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    7: {
        "question": "If all doctors are lawyers and John is a doctor, is John a lawyer?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "A"
    },
    8: {
        "question": "If all students are teachers and Mary is not a student, is Mary a teacher?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    9: {
        "question": "If all fish can walk and a frog is a fish, can a frog walk?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "A"
    },
    10: {
        "question": "If all mammals lay eggs and a cat is a mammal, can a cat lay eggs?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    11: {
        "question": "If all humans have wings and Sarah is a human, does Sarah have wings?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    12: {
        "question": "If all dogs are cats and a mouse is not a dog, is a mouse a cat?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    13: {
        "question": "If all horses are donkeys and a zebra is a horse, is a zebra a donkey?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    14: {
        "question": "If all planets are stars and the Moon is not a planet, is the Moon a star?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    15: {
        "question": "If all apples are fruits and a potato is not an apple, is a potato a fruit?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    16: {
        "question": "If all birds can fly and a penguin is a bird, can a penguin fly?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    17: {
        "question": "If all doctors are musicians and Paul is not a doctor, is Paul a musician?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    18: {
        "question": "If all fish can breathe underwater and a turtle is not a fish, can a turtle breathe underwater?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    19: {
        "question": "If all apples are fruits and a carrot is not an apple, is a carrot a fruit?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    20: {
        "question": "If all insects have six legs and a spider is not an insect, does a spider have six legs?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    }
}

medium_reasoning_questions = {
    1: {
        "question": "If all birds can fly and a penguin is a bird, can a penguin fly?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Sometimes",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    2: {
        "question": "If all doctors are scientists and some scientists are engineers, can all doctors be engineers?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "C"
    },
    3: {
        "question": "If all cats are mammals and some mammals are not dogs, can all cats be dogs?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    4: {
        "question": "If all politicians are dishonest and some dishonest people are not politicians, can all politicians be honest?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "D"
    },
    5: {
        "question": "If all triangles have three sides and a square is not a triangle, can a square have three sides?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Sometimes",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    6: {
        "question": "If all swans are white and some white birds are not swans, can all swans be black?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "D"
    },
    7: {
        "question": "If all teachers are educators and some educators are writers, can all teachers be writers?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "C"
    },
    8: {
        "question": "If all mammals give birth to live young and some animals that give birth to live young are not mammals, can all mammals lay eggs?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Sometimes",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    9: {
        "question": "If all politicians are rich and some rich people are not politicians, can all rich people be politicians?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "C"
    },
    10: {
        "question": "If all roses are flowers and some flowers are not red, can all roses be red?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Sometimes",
            "D": "Cannot be determined"
        },
        "answer": "C"
    },
    11: {
        "question": "If all apples are fruits and some fruits are green, can all apples be green?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Sometimes",
            "D": "Cannot be determined"
        },
        "answer": "C"
    },
    12: {
        "question": "If all birds can fly and some flying animals are not birds, can all flying animals be birds?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    13: {
        "question": "If all humans are mortal and some mortal beings are not humans, can all humans be immortal?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    14: {
        "question": "If all squares have four sides and some four-sided figures are not squares, can all squares be rectangles?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Sometimes",
            "D": "Cannot be determined"
        },
        "answer": "A"
    },
    15: {
        "question": "If all cats have tails and some tailed animals are not cats, can all tailed animals be cats?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    16: {
        "question": "If all politicians are liars and some liars are not politicians, can all liars be politicians?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "C"
    },
    17: {
        "question": "If all dogs bark and some barking animals are not dogs, can all barking animals be dogs?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    18: {
        "question": "If all fish swim and some swimming creatures are not fish, can all swimming creatures be fish?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "C"
    },
    19: {
        "question": "If all books are novels and some novels are not stories, can all books be stories?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    20: {
        "question": "If all fish have gills and some gilled animals are not fish, can all gilled animals be fish?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    }
}

hard_reasoning_questions = {
    1: {
        "question": "If all widgets are gadgets and some gadgets are not gizmos, can all gizmos be widgets?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    2: {
        "question": "If all A is B, some B is C, and some C is not D, can all D be A?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    3: {
        "question": "If no X is Y, all Y is Z, and some Z is not A, can all A be X?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    4: {
        "question": "If all Q is R, some R is S, and all S is T, can all T be Q?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "C"
    },
    5: {
        "question": "If some P is Q, all Q is R, and all R is S, can all S be P?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "C"
    },
    6: {
        "question": "If all X is Y, no Y is Z, and some Z is not W, can all W be X?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    7: {
        "question": "If some M is N, some N is O, and some O is not P, can all P be M?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    8: {
        "question": "If all A is B, all B is C, and some C is not D, can all D be A?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    9: {
        "question": "If no X is Y, some Y is Z, and some Z is not A, can all A be X?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    10: {
        "question": "If all Q is R, some R is S, and all S is T, can all T be Q?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "C"
    },
    11: {
        "question": "If some P is Q, all Q is R, and all R is S, can all S be P?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "C"
    },
    12: {
        "question": "If all X is Y, no Y is Z, and some Z is not W, can all W be X?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    13: {
        "question": "If some M is N, some N is O, and some O is not P, can all P be M?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    14: {
        "question": "If all A is B, all B is C, and some C is not D, can all D be A?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    15: {
        "question": "If no X is Y, some Y is Z, and some Z is not A, can all A be X?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    16: {
        "question": "If all Q is R, some R is S, and all S is T, can all T be Q?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "C"
    },
    17: {
        "question": "If some P is Q, all Q is R, and all R is S, can all S be P?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "C"
    },
    18: {
        "question": "If all X is Y, no Y is Z, and some Z is not W, can all W be X?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    19: {
        "question": "If some M is N, some N is O, and some O is not P, can all P be M?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    },
    20: {
        "question": "If all A is B, all B is C, and some C is not D, can all D be A?",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe",
            "D": "Cannot be determined"
        },
        "answer": "B"
    }
}

easy_science_questions = {
    1: {
        "question": "What is the chemical symbol for gold?",
        "options": {
            "A": "Au",
            "B": "Ag",
            "C": "Fe",
            "D": "Hg"
        },
        "answer": "A"
    },
    2: {
        "question": "Which planet is known as the Red Planet?",
        "options": {
            "A": "Earth",
            "B": "Mars",
            "C": "Venus",
            "D": "Jupiter"
        },
        "answer": "B"
    },
    3: {
        "question": "What is the chemical symbol for water?",
        "options": {
            "A": "Wo",
            "B": "Wa",
            "C": "H2O",
            "D": "W"
        },
        "answer": "C"
    },
    4: {
        "question": "What is the process by which plants make their food?",
        "options": {
            "A": "Respiration",
            "B": "Photosynthesis",
            "C": "Decomposition",
            "D": "Transpiration"
        },
        "answer": "B"
    },
    5: {
        "question": "What is the closest star to Earth?",
        "options": {
            "A": "Proxima Centauri",
            "B": "Sirius",
            "C": "Alpha Centauri",
            "D": "Sun"
        },
        "answer": "D"
    },
    6: {
        "question": "Which gas is most abundant in Earth's atmosphere?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon Dioxide",
            "D": "Hydrogen"
        },
        "answer": "B"
    },
    7: {
        "question": "What is the chemical formula for table salt?",
        "options": {
            "A": "NaCl",
            "B": "HCl",
            "C": "CaCl2",
            "D": "KCl"
        },
        "answer": "A"
    },
    8: {
        "question": "Which organ in the human body produces insulin?",
        "options": {
            "A": "Liver",
            "B": "Pancreas",
            "C": "Kidney",
            "D": "Stomach"
        },
        "answer": "B"
    },
    9: {
        "question": "What is the hardest natural substance on Earth?",
        "options": {
            "A": "Diamond",
            "B": "Quartz",
            "C": "Gold",
            "D": "Graphite"
        },
        "answer": "A"
    },
    10: {
        "question": "Which force holds the planets in orbit around the Sun?",
        "options": {
            "A": "Gravity",
            "B": "Electromagnetism",
            "C": "Strong nuclear force",
            "D": "Weak nuclear force"
        },
        "answer": "A"
    },
    11: {
        "question": "What is the chemical symbol for carbon dioxide?",
        "options": {
            "A": "Co2",
            "B": "Co",
            "C": "CO",
            "D": "CO2"
        },
        "answer": "D"
    },
    12: {
        "question": "Which element is essential for human bones and teeth?",
        "options": {
            "A": "Iron",
            "B": "Calcium",
            "C": "Potassium",
            "D": "Sodium"
        },
        "answer": "B"
    },
    13: {
        "question": "What causes tides on Earth?",
        "options": {
            "A": "The Moon's gravitational pull",
            "B": "The Sun's gravitational pull",
            "C": "The Earth's rotation",
            "D": "Ocean currents"
        },
        "answer": "A"
    },
    14: {
        "question": "What is the chemical symbol for oxygen?",
        "options": {
            "A": "O2",
            "B": "Ox",
            "C": "Ox2",
            "D": "O"
        },
        "answer": "D"
    },
    15: {
        "question": "What is the unit of electrical resistance?",
        "options": {
            "A": "Volt",
            "B": "Ampere",
            "C": "Ohm",
            "D": "Watt"
        },
        "answer": "C"
    },
    16: {
        "question": "What is the process by which water turns into vapor?",
        "options": {
            "A": "Condensation",
            "B": "Melting",
            "C": "Evaporation",
            "D": "Sublimation"
        },
        "answer": "C"
    },
    17: {
        "question": "Which metal is liquid at room temperature?",
        "options": {
            "A": "Mercury",
            "B": "Iron",
            "C": "Copper",
            "D": "Aluminum"
        },
        "answer": "A"
    },
    18: {
        "question": "What is the chemical symbol for helium?",
        "options": {
            "A": "He",
            "B": "H",
            "C": "H2",
            "D": "He2"
        },
        "answer": "A"
    },
    19: {
        "question": "What is the largest organ in the human body?",
        "options": {
            "A": "Brain",
            "B": "Liver",
            "C": "Skin",
            "D": "Heart"
        },
        "answer": "C"
    },
    20: {
        "question": "What is the study of living organisms called?",
        "options": {
            "A": "Biology",
            "B": "Geology",
            "C": "Astronomy",
            "D": "Chemistry"
        },
        "answer": "A"
    },
    21: {
        "question": "What is the chemical symbol for iron?",
        "options": {
            "A": "Fe",
            "B": "Ir",
            "C": "In",
            "D": "Io"
        },
        "answer": "A"
    },
    22: {
        "question": "What is the smallest unit of matter?",
        "options": {
            "A": "Atom",
            "B": "Molecule",
            "C": "Cell",
            "D": "Electron"
        },
        "answer": "A"
    },
    23: {
        "question": "Which gas do plants absorb during photosynthesis?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Hydrogen"
        },
        "answer": "C"
    },
    24: {
        "question": "What is the chemical symbol for sodium?",
        "options": {
            "A": "Sa",
            "B": "So",
            "C": "S",
            "D": "Na"
        },
        "answer": "D"
    },
    25: {
        "question": "What is the study of earthquakes called?",
        "options": {
            "A": "Meteorology",
            "B": "Seismology",
            "C": "Geology",
            "D": "Climatology"
        },
        "answer": "B"
    },
    26: {
        "question": "Which is the largest planet in our solar system?",
        "options": {
            "A": "Earth",
            "B": "Jupiter",
            "C": "Saturn",
            "D": "Mars"
        },
        "answer": "B"
    },
   28: {
        "question": "What is the chemical symbol for potassium?",
        "options": {
            "A": "K",
            "B": "P",
            "C": "Ka",
            "D": "Ko"
        },
        "answer": "A"
    },
    29: {
        "question": "What is the chemical symbol for silver?",
        "options": {
            "A": "S",
            "B": "Si",
            "C": "Ag",
            "D": "Au"
        },
        "answer": "C"
    },
    30: {
        "question": "Which organ in the human body produces bile?",
        "options": {
            "A": "Liver",
            "B": "Pancreas",
            "C": "Kidney",
            "D": "Gallbladder"
        },
        "answer": "A"
    },
    31: {
        "question": "What is the chemical symbol for nitrogen?",
        "options": {
            "A": "Ni",
            "B": "N",
            "C": "Ne",
            "D": "Na"
        },
        "answer": "B"
    },
    32: {
        "question": "Which gas do humans exhale when they breathe out?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Hydrogen"
        },
        "answer": "C"
    },
    33: {
        "question": "What is the process by which rocks are broken down into smaller particles?",
        "options": {
            "A": "Erosion",
            "B": "Weathering",
            "C": "Deposition",
            "D": "Sedimentation"
        },
        "answer": "B"
    },
    34: {
        "question": "What is the chemical symbol for copper?",
        "options": {
            "A": "Co",
            "B": "Cu",
            "C": "Cp",
            "D": "Cr"
        },
        "answer": "B"
    },
    35: {
        "question": "What is the study of fossils called?",
        "options": {
            "A": "Paleontology",
            "B": "Archaeology",
            "C": "Anthropology",
            "D": "Geology"
        },
        "answer": "A"
    },
    36: {
        "question": "Which gas do plants give off during respiration?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Hydrogen"
        },
        "answer": "C"
    },
    37: {
        "question": "What is the chemical symbol for lead?",
        "options": {
            "A": "L",
            "B": "P",
            "C": "Pb",
            "D": "Pl"
        },
        "answer": "C"
    },
    38: {
        "question": "What is the study of the Earth's atmosphere called?",
        "options": {
            "A": "Meteorology",
            "B": "Geology",
            "C": "Climatology",
            "D": "Oceanography"
        },
        "answer": "A"
    },
    39: {
        "question": "Which element is essential for the process of photosynthesis?",
        "options": {
            "A": "Carbon",
            "B": "Oxygen",
            "C": "Chlorine",
            "D": "Nitrogen"
        },
        "answer": "A"
    },
    40: {
        "question": "What is the chemical symbol for carbon?",
        "options": {
            "A": "Ca",
            "B": "Cr",
            "C": "C",
            "D": "Co"
        },
        "answer": "C"
    },
    41: {
        "question": "Which gas is responsible for the greenhouse effect?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Hydrogen"
        },
        "answer": "C"
    },
    42: {
        "question": "What is the study of rocks called?",
        "options": {
            "A": "Meteorology",
            "B": "Seismology",
            "C": "Geology",
            "D": "Paleontology"
        },
        "answer": "C"
    },
    43: {
        "question": "Which organ in the human body produces urine?",
        "options": {
            "A": "Liver",
            "B": "Kidney",
            "C": "Pancreas",
            "D": "Gallbladder"
        },
        "answer": "B"
    },
    44: {
        "question": "What is the chemical symbol for silicon?",
        "options": {
            "A": "S",
            "B": "Si",
            "C": "Se",
            "D": "So"
        },
        "answer": "B"
    },
    45: {
        "question": "What is the process by which plants lose water through small openings in their leaves?",
        "options": {
            "A": "Respiration",
            "B": "Transpiration",
            "C": "Photosynthesis",
            "D": "Evaporation"
        },
        "answer": "B"
    },
    46: {
        "question": "What is the chemical symbol for hydrogen?",
        "options": {
            "A": "H2",
            "B": "Hg",
            "C": "H",
            "D": "Ho"
        },
        "answer": "C"
    },
    47: {
        "question": "What is the study of the ocean called?",
        "options": {
            "A": "Meteorology",
            "B": "Geology",
            "C": "Oceanography",
            "D": "Climatology"
        },
        "answer": "C"
    },
    48: {
        "question": "Which gas do humans need to breathe in order to survive?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Hydrogen"
        },
        "answer": "A"
    },
    49: {
        "question": "What is the chemical symbol for mercury?",
        "options": {
            "A": "Me",
            "B": "Hg",
            "C": "Mg",
            "D": "Mr"
        },
        "answer": "B"
    },
    50: {
        "question": "What is the study of the weather called?",
        "options": {
            "A": "Meteorology",
            "B": "Climatology",
            "C": "Oceanography",
            "D": "Geology"
        },
        "answer": "A"
    },
    51: {
        "question": "Which gas is known as laughing gas?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Nitrous oxide"
        },
        "answer": "D"
    },
    52: {
        "question": "What is the chemical symbol for phosphorus?",
        "options": {
            "A": "P",
            "B": "Ph",
            "C": "Po",
            "D": "Pi"
        },
        "answer": "A"
    },
    53: {
        "question": "What is the process by which liquid turns into vapor below its boiling point?",
        "options": {
            "A": "Boiling",
            "B": "Melting",
            "C": "Evaporation",
            "D": "Sublimation"
        },
        "answer": "C"
    },
    54: {
        "question": "Which gas do fire extinguishers contain to put out fires?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Carbon monoxide"
        },
        "answer": "C"
    },
    55: {
        "question": "What is the chemical symbol for sulfur?",
        "options": {
            "A": "Su",
            "B": "S",
            "C": "Sl",
            "D": "Sa"
        },
        "answer": "B"
    },
    56: {
        "question": "What is the study of the origin and evolution of the universe called?",
        "options": {
            "A": "Cosmology",
            "B": "Astronomy",
            "C": "Astrology",
            "D": "Geology"
        },
        "answer": "A"
    },
    57: {
        "question": "Which gas is used in balloons to make them float?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Helium",
            "D": "Hydrogen"
        },
        "answer": "C"
    },
    58: {
        "question": "What is the chemical symbol for chlorine?",
        "options": {
            "A": "Cl",
            "B": "C",
            "C": "Ch",
            "D": "Cl2"
        },
        "answer": "A"
    },
    59: {
        "question": "What is the study of the Earth's structure and composition called?",
        "options": {
            "A": "Geology",
            "B": "Meteorology",
            "C": "Seismology",
            "D": "Oceanography"
        },
        "answer": "A"
    },
    60: {
        "question": "Which gas is produced during the process of fermentation?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Hydrogen"
        },
        "answer": "C"
    },
    61: {
        "question": "What is the chemical symbol for neon?",
        "options": {
            "A": "No",
            "B": "Ne",
            "C": "N",
            "D": "Na"
        },
        "answer": "B"
    },
    62: {
        "question": "What is the process by which liquid turns into a solid?",
        "options": {
            "A": "Melting",
            "B": "Freezing",
            "C": "Evaporation",
            "D": "Condensation"
        },
        "answer": "B"
    },
    63: {
        "question": "Which gas do plants give off as a byproduct of photosynthesis?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Hydrogen"
        },
        "answer": "A"
    },
    64: {
        "question": "What is the process by which plants absorb water from the soil?",
        "options": {
            "A": "Transpiration",
            "B": "Photosynthesis",
            "C": "Respiration",
            "D": "Osmosis"
        },
        "answer": "D"
    },
    65: {
        "question": "Which gas is used in car airbags for rapid inflation?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Argon"
        },
        "answer": "B"
    },
    66: {
        "question": "What is the chemical symbol for argon?",
        "options": {
            "A": "Ag",
            "B": "Ar",
            "C": "An",
            "D": "Ao"
        },
        "answer": "B"
    },
    67: {
        "question": "What is the study of the Earth's oceans called?",
        "options": {
            "A": "Meteorology",
            "B": "Oceanography",
            "C": "Climatology",
            "D": "Geology"
        },
        "answer": "B"
    },
    68: {
        "question": "Which gas is produced during the process of respiration?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Hydrogen"
        },
        "answer": "C"
    },
    69: {
        "question": "What is the chemical symbol for zinc?",
        "options": {
            "A": "Zn",
            "B": "Z",
            "C": "Zi",
            "D": "Zc"
        },
        "answer": "A"
    },
    70: {
        "question": "What is the process by which plants and animals release energy from food?",
        "options": {
            "A": "Respiration",
            "B": "Photosynthesis",
            "C": "Digestion",
            "D": "Fermentation"
        },
        "answer": "A"
    },
    71: {
        "question": "Which gas is used in light bulbs to prevent the filament from burning?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Argon"
        },
        "answer": "D"
    },
    72: {
        "question": "What is the chemical symbol for uranium?",
        "options": {
            "A": "Ur",
            "B": "U",
            "C": "Un",
            "D": "Ut"
        },
        "answer": "B"
    },
    73: {
        "question": "What is the process by which rocks are transported from one place to another?",
        "options": {
            "A": "Weathering",
            "B": "Erosion",
            "C": "Deposition",
            "D": "Sedimentation"
        },
        "answer": "B"
    },
    74: {
        "question": "Which gas is used in the process of welding?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Acetylene"
        },
        "answer": "D"
    },
    75: {
        "question": "What is the chemical symbol for tin?",
        "options": {
            "A": "Ti",
            "B": "T",
            "C": "Sn",
            "D": "Si"
        },
        "answer": "C"
    },
    76: {
        "question": "What is the study of the Earth's climate called?",
        "options": {
            "A": "Meteorology",
            "B": "Climatology",
            "C": "Oceanography",
            "D": "Geology"
        },
        "answer": "B"
    },
    77: {
        "question": "Which gas is used in fire extinguishers to put out electrical fires?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Halon"
        },
        "answer": "D"
    },
    78: {
        "question": "What is the process by which rocks settle out of water or air?",
        "options": {
            "A": "Erosion",
            "B": "Weathering",
            "C": "Deposition",
            "D": "Sedimentation"
        },
        "answer": "C"
    },
    79: {
        "question": "Which gas is used in the production of soft drinks?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Hydrogen"
        },
        "answer": "C"
    },
    80: {
        "question": "What is the chemical symbol for radium?",
        "options": {
            "A": "R",
            "B": "Ra",
            "C": "Rd",
            "D": "Rm"
        },
        "answer": "B"
    },
    81: {
        "question": "Which gas is used in the process of photosynthesis?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Hydrogen"
        },
        "answer": "C"
    },
    82: {
        "question": "What is the chemical symbol for cobalt?",
        "options": {
            "A": "Co",
            "B": "Cl",
            "C": "Ca",
            "D": "C"
        },
        "answer": "A"
    },
    83: {
        "question": "Which gas is used in the process of sterilizing medical equipment?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon dioxide",
            "D": "Ethylene oxide"
        },
        "answer": "D"
    }
}

medium_science_questions = {
    1: {
        "question": "What is the name of the boundary between two tectonic plates that are moving away from each other?",
        "options": {
            "A": "Convergent boundary",
            "B": "Transform boundary",
            "C": "Divergent boundary",
            "D": "Subduction boundary"
        },
        "answer": "C"
    },
    2: {
        "question": "In quantum mechanics, what principle states that it's impossible to precisely know both the position and momentum of a particle simultaneously?",
        "options": {
            "A": "Pauli exclusion principle",
            "B": "Uncertainty principle",
            "C": "Conservation principle",
            "D": "Heisenberg principle"
        },
        "answer": "B"
    },
    3: {
        "question": "Which type of chemical bond involves the sharing of electron pairs between atoms?",
        "options": {
            "A": "Ionic bond",
            "B": "Metallic bond",
            "C": "Covalent bond",
            "D": "Hydrogen bond"
        },
        "answer": "C"
    },
    4: {
        "question": "What is the process by which a solid changes directly to a gas without passing through the liquid state?",
        "options": {
            "A": "Evaporation",
            "B": "Condensation",
            "C": "Sublimation",
            "D": "Deposition"
        },
        "answer": "C"
    },
    5: {
        "question": "What term refers to the measure of disorder or randomness in a closed system?",
        "options": {
            "A": "Entropy",
            "B": "Enthalpy",
            "C": "Exothermicity",
            "D": "Equilibrium"
        },
        "answer": "A"
    },
    6: {
        "question": "Which of the following is NOT a greenhouse gas?",
        "options": {
            "A": "Carbon dioxide",
            "B": "Methane",
            "C": "Nitrous oxide",
            "D": "Ozone"
        },
        "answer": "D"
    },
    7: {
        "question": "What is the name of the subatomic particle that carries a positive electrical charge?",
        "options": {
            "A": "Electron",
            "B": "Neutron",
            "C": "Proton",
            "D": "Positron"
        },
        "answer": "C"
    },
    8: {
        "question": "What term refers to the bending of light as it passes from one medium to another?",
        "options": {
            "A": "Refraction",
            "B": "Reflection",
            "C": "Diffraction",
            "D": "Absorption"
        },
        "answer": "A"
    },
    9: {
        "question": "Which scientist is credited with the discovery of the neutron?",
        "options": {
            "A": "Albert Einstein",
            "B": "James Clerk Maxwell",
            "C": "Ernest Rutherford",
            "D": "James Chadwick"
        },
        "answer": "D"
    },
    10: {
        "question": "What is the SI unit of electric charge?",
        "options": {
            "A": "Volt",
            "B": "Ampere",
            "C": "Ohm",
            "D": "Coulomb"
        },
        "answer": "D"
    },
    11: {
        "question": "What is the term for the process by which an unstable atomic nucleus loses energy by emitting radiation?",
        "options": {
            "A": "Fusion",
            "B": "Fission",
            "C": "Decay",
            "D": "Transmutation"
        },
        "answer": "C"
    },
    12: {
        "question": "Which of the following is a primary component of Earth's atmosphere?",
        "options": {
            "A": "Nitrogen",
            "B": "Oxygen",
            "C": "Carbon dioxide",
            "D": "All of the above"
        },
        "answer": "D"
    },
    13: {
        "question": "What is the process by which rocks are broken down into smaller pieces by physical means?",
        "options": {
            "A": "Erosion",
            "B": "Weathering",
            "C": "Deposition",
            "D": "Sedimentation"
        },
        "answer": "B"
    },
    14: {
        "question": "Which of the following is NOT a type of electromagnetic radiation?",
        "options": {
            "A": "X-rays",
            "B": "Microwaves",
            "C": "Ultrasound",
            "D": "Gamma rays"
        },
        "answer": "C"
    },
    15: {
        "question": "What is the process by which plants convert light energy into chemical energy?",
        "options": {
            "A": "Photosynthesis",
            "B": "Respiration",
            "C": "Transpiration",
            "D": "Pollination"
        },
        "answer": "A"
    },
    16: {
        "question": "Which of the following is the smallest bone in the human body?",
        "options": {
            "A": "Stapes",
            "B": "Femur",
            "C": "Tibia",
            "D": "Radius"
        },
        "answer": "A"
    },
    17: {
        "question": "What is the process by which an organism produces offspring that are identical to itself?",
        "options": {
            "A": "Fertilization",
            "B": "Reproduction",
            "C": "Cloning",
            "D": "Mutation"
        },
        "answer": "C"
    },
    18: {
        "question": "Which of the following is NOT a characteristic of a chemical reaction?",
        "options": {
            "A": "Formation of new substances",
            "B": "Change in energy",
            "C": "Reversible process",
            "D": "Change in physical state"
        },
        "answer": "D"
    },
    19: {
        "question": "What is the study of the movement of the Earth's crust called?",
        "options": {
            "A": "Meteorology",
            "B": "Geophysics",
            "C": "Seismology",
            "D": "Geology"
        },
        "answer": "C"
    },
    20: {
        "question": "Which of the following is NOT a type of chemical reaction?",
        "options": {
            "A": "Combustion",
            "B": "Redox",
            "C": "Fusion",
            "D": "Sublimation"
        },
        "answer": "D"
    }
}

hard_science_questions = {
    1: {
        "question": "What is the process by which stars convert hydrogen into helium through nuclear fusion?",
        "options": {
            "A": "Photosynthesis",
            "B": "Fission",
            "C": "Nebulization",
            "D": "Thermonuclear fusion"
        },
        "answer": "D"
    },
    2: {
        "question": "What is the name of the phenomenon in quantum mechanics where particles exhibit wave-like behavior?",
        "options": {
            "A": "Wave-particle duality",
            "B": "Quantum entanglement",
            "C": "Schrodinger's cat",
            "D": "Heisenberg uncertainty principle"
        },
        "answer": "A"
    },
    3: {
        "question": "What is the name of the theory in physics that attempts to unify the fundamental forces of nature?",
        "options": {
            "A": "String theory",
            "B": "Quantum mechanics",
            "C": "General relativity",
            "D": "Theory of everything"
        },
        "answer": "D"
    },
    4: {
        "question": "What is the study of the behavior of matter at extremely low temperatures called?",
        "options": {
            "A": "Thermodynamics",
            "B": "Quantum mechanics",
            "C": "Cryogenics",
            "D": "Nanotechnology"
        },
        "answer": "C"
    },
    5: {
        "question": "What is the term for a hypothetical particle that is its own antiparticle?",
        "options": {
            "A": "Boson",
            "B": "Fermion",
            "C": "Meson",
            "D": "Majorana fermion"
        },
        "answer": "D"
    },
    6: {
        "question": "Which of the following is NOT a fundamental particle of the Standard Model of particle physics?",
        "options": {
            "A": "Quark",
            "B": "Neutrino",
            "C": "Lepton",
            "D": "Photon"
        },
        "answer": "B"
    },
    7: {
        "question": "What is the name of the boundary that separates the Earth's crust from the underlying mantle?",
        "options": {
            "A": "Asthenosphere",
            "B": "Mohorovicic discontinuity",
            "C": "Lithosphere",
            "D": "Gutenberg discontinuity"
        },
        "answer": "B"
    },
    8: {
        "question": "What is the term for a sudden and violent release of energy from the Earth's crust?",
        "options": {
            "A": "Tornado",
            "B": "Earthquake",
            "C": "Volcano",
            "D": "Tsunami"
        },
        "answer": "B"
    },
    9: {
        "question": "What is the name of the process by which a star collapses under its own gravity after exhausting its nuclear fuel?",
        "options": {
            "A": "Supernova",
            "B": "Black hole formation",
            "C": "Nebula",
            "D": "White dwarf"
        },
        "answer": "B"
    },
    10: {
        "question": "Which of the following is NOT a greenhouse gas?",
        "options": {
            "A": "Carbon dioxide",
            "B": "Methane",
            "C": "Ozone",
            "D": "Nitrogen"
        },
        "answer": "D"
    },
    11: {
        "question": "What is the name of the phenomenon where light bends as it passes through different mediums?",
        "options": {
            "A": "Refraction",
            "B": "Reflection",
            "C": "Diffraction",
            "D": "Absorption"
        },
        "answer": "A"
    },
    12: {
        "question": "What is the term for the point at which a solid turns directly into a gas without passing through the liquid state?",
        "options": {
            "A": "Sublimation",
            "B": "Evaporation",
            "C": "Condensation",
            "D": "Vaporization"
        },
        "answer": "A"
    },
    13: {
        "question": "What is the name of the process by which a cell engulfs solid particles?",
        "options": {
            "A": "Phagocytosis",
            "B": "Exocytosis",
            "C": "Pinocytosis",
            "D": "Endocytosis"
        },
        "answer": "A"
    },
    14: {
        "question": "What is the term for the bending of seismic waves as they pass from one medium to another?",
        "options": {
            "A": "Reflection",
            "B": "Refraction",
            "C": "Compression",
            "D": "Rarefaction"
        },
        "answer": "B"
    },
    15: {
        "question": "Which of the following is NOT a type of chemical bond?",
        "options": {
            "A": "Ionic bond",
            "B": "Covalent bond",
            "C": "Hydrogen bond",
            "D": "Magnetic bond"
        },
        "answer": "D"
    },
    16: {
        "question": "What is the name of the process by which a substance transitions directly from a solid to a gas without passing through the liquid phase?",
        "options": {
            "A": "Deposition",
            "B": "Sublimation",
            "C": "Evaporation",
            "D": "Condensation"
        },
        "answer": "B"
    },
    17: {
        "question": "What is the term for the process by which cells break down molecules to release energy?",
        "options": {
            "A": "Fermentation",
            "B": "Glycolysis",
            "C": "Oxidation",
            "D": "Respiration"
        },
        "answer": "D"
    },
    18: {
        "question": "What is the name of the boundary between two air masses with different temperatures and densities?",
        "options": {
            "A": "Front",
            "B": "Isobar",
            "C": "Tropopause",
            "D": "Thermocline"
        },
        "answer": "A"
    },
    19: {
        "question": "What is the term for the process by which a liquid is transformed into a gas at temperatures below its boiling point?",
        "options": {
            "A": "Boiling",
            "B": "Evaporation",
            "C": "Condensation",
            "D": "Sublimation"
        },
        "answer": "B"
    },
    20: {
        "question": "What is the name of the force that opposes the motion of an object through a fluid?",
        "options": {
            "A": "Friction",
            "B": "Drag",
            "C": "Tension",
            "D": "Gravity"
        },
        "answer": "B"
    }
}

# Function to select 5 random questions from the given subject and difficulty level
def select_questions(subject, difficulty):
    all_questions = []
    if subject == "math":
        if difficulty == "easy":
            all_questions = list(easy_math_questions.values())
        elif difficulty == "medium":
            all_questions = list(medium_math_questions.values())
        elif difficulty == "hard":
            all_questions = list(hard_math_questions.values())
    elif subject == "reasoning":
        if difficulty == "easy":
            all_questions = list(easy_reasoning_questions.values())
        elif difficulty == "medium":
            all_questions = list(medium_reasoning_questions.values())
        elif difficulty == "hard":
            all_questions = list(hard_reasoning_questions.values())
    elif subject == "science":
        if difficulty == "easy":
            all_questions = list(easy_science_questions.values())
        elif difficulty == "medium":
            all_questions = list(medium_science_questions.values())
        elif difficulty == "hard":
            all_questions = list(hard_science_questions.values())

    if len(all_questions) >= 5:
        return random.sample(all_questions, 5)
    else:
        return None

# Function to evaluate the answer and move to the next question
def check_answer(question, user_answer):
    if user_answer == question["answer"]:
        return True
    else:
        return False

# Function to display the question and options
def ask_question():
    global question_index, correct_answers
    if question_index < len(questions):
        question = questions[question_index]

        # Clear the window
        for widget in root.winfo_children():
            widget.destroy()

        # Display the question
        question_label = tk.Label(root, text=question["question"], font=("Great Vibes", 14), wraplength=400, bg="#000000", fg="#ffffff")
        question_label.pack(pady=20)

        # Display the options
        for option, value in question["options"].items():
            option_button = tk.Button(root, text=f"{option}. {value}", font=("Great Vibes", 12), bg="#333333", fg="#ffffff", width=30, height=2,
                                      command=lambda ans=option: process_answer(question, ans))
            option_button.pack(pady=5)

    else:
        show_summary()

# Function to process the user's answer and move to the next question
def process_answer(question, user_answer):
    global question_index, correct_answers
    if check_answer(question, user_answer):
        correct_answers += 1

    user_answers.append(user_answer)
    question_index += 1
    ask_question()

# Function to show the main screen
def show_main_screen():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Subject selection
    subject_label = tk.Label(root, text="Choose a subject:", font=("Great Vibes", 14), bg="#000000", fg="#ffffff")
    subject_label.pack()
    subject_var.set("Math")
    subject_option_menu = tk.OptionMenu(root, subject_var, "Math", "Reasoning", "Science")
    subject_option_menu.config(bg="#333333", fg="#ffffff", width=20)
    subject_option_menu.pack()

    # Difficulty level selection
    difficulty_label = tk.Label(root, text="Choose a difficulty level:", font=("Great Vibes", 14), bg="#000000", fg="#ffffff")
    difficulty_label.pack()
    difficulty_var.set("Easy")
    difficulty_option_menu = tk.OptionMenu(root, difficulty_var, "Easy", "Medium", "Hard")
    difficulty_option_menu.config(bg="#333333", fg="#ffffff", width=20)
    difficulty_option_menu.pack()

    # Start quiz button
    start_button = tk.Button(root, text="Start Quiz", font=("Great Vibes", 14), bg="#333333", fg="#ffffff", width=20, height=2, command=start_quiz_from_input)
    start_button.pack(pady=20)
    
# Function to show the quiz summary
def show_summary():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Display the summary
    summary_label = tk.Label(root, text="Quiz Complete!", font=("Great Vibes", 20), bg="#000000", fg="#ffffff")
    summary_label.pack(pady=20)

    score_label = tk.Label(root, text=f"Your score: {correct_answers} / 5", font=("Great Vibes", 16), bg="#000000", fg="#ffffff")
    score_label.pack()

    # Create a frame for the summary with a vertical scrollbar
    summary_frame = tk.Frame(root, bg="#000000")
    summary_frame.pack(pady=10)

    summary_scroll = tk.Scrollbar(summary_frame)
    summary_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    summary_text = tk.Text(summary_frame, width=60, height=10, font=("Great Vibes", 12), bg="#333333", fg="#ffffff", yscrollcommand=summary_scroll.set)
    summary_text.pack(side=tk.LEFT, fill=tk.Y)

    summary_scroll.config(command=summary_text.yview)

    # Display the details of each question
    for i, (question, user_answer) in enumerate(zip(questions, user_answers), 1):
        question_text = question["question"]
        correct_answer = question["answer"]
        options = "\n".join([f"{option}. {value}" for option, value in question["options"].items()])
        result = "Correct" if user_answer == correct_answer else "Incorrect"
        summary_text.insert(tk.END, f"Question {i}: {question_text}\nOptions:\n{options}\nYour Answer: {user_answer}\nCorrect Answer: {correct_answer}\nResult: {result}\n\n")

    # Play Again button
    play_again_button = tk.Button(root, text="Play Again", font=("Great Vibes", 14), bg="#333333", fg="#ffffff", width=20, height=2, command=show_main_screen)
    play_again_button.pack(pady=20)
    
# Function to start the quiz
def start_quiz(subject, difficulty):
    global questions, question_index, correct_answers, user_answers
    questions = select_questions(subject, difficulty)
    if questions:
        question_index = 0
        correct_answers = 0
        user_answers = []
        ask_question()
    else:
        messagebox.showerror("Error", "No questions available for selected subject and difficulty.")

# Function to start the quiz based on user input
def start_quiz_from_input():
    subject = subject_var.get().lower()
    difficulty = difficulty_var.get().lower()
    start_quiz(subject, difficulty)

# GUI setup
root = tk.Tk()
root.title("Educational Quiz Game")
root.geometry("600x400")
root.configure(bg="#000000")


# Subject selection
subject_label = tk.Label(root, text="Choose a subject:", font=("Great Vibes", 14), bg="#000000", fg="#ffffff")
subject_label.pack()
subject_var = tk.StringVar(root)
subject_var.set("Math")
subject_option_menu = tk.OptionMenu(root, subject_var, "Math", "Reasoning", "Science")
subject_option_menu.config(bg="#333333", fg="#ffffff", width=20)
subject_option_menu.pack()

# Difficulty level selection
difficulty_label = tk.Label(root, text="Choose a difficulty level:", font=("Great Vibes", 14), bg="#000000", fg="#ffffff")
difficulty_label.pack()
difficulty_var = tk.StringVar(root)
difficulty_var.set("Easy")
difficulty_option_menu = tk.OptionMenu(root, difficulty_var, "Easy", "Medium", "Hard")
difficulty_option_menu.config(bg="#333333", fg="#ffffff", width=20)
difficulty_option_menu.pack()

# Start quiz button
start_button = tk.Button(root, text="Start Quiz", font=("Great Vibes", 14), bg="#333333", fg="#ffffff", width=20, height=2, command=start_quiz_from_input)
start_button.pack(pady=20)

question_index = 0
correct_answers = 0
user_answers = []

root.mainloop()

