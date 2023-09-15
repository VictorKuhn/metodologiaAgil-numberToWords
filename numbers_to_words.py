def number_to_words(num):
    num_to_words = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }

    if num <= 20:
        return num_to_words[num]
    elif num < 100:
        tens = num_to_words[num // 10 * 10]
        ones = num_to_words[num % 10]
        if ones == "zero":
            return tens
        else:
            return f"{tens}-{ones}"
    elif num < 1000:
        hundreds = num_to_words[num // 100]
        remainder = num % 100
        if remainder == 0:
            return f"{hundreds} hundred"
        else:
            return f"{hundreds} hundred {number_to_words(remainder)}"
    else:
        thousands = num // 1000
        remainder = num % 1000
        if remainder == 0:
            return f"{number_to_words(thousands)} thousand"
        else:
            return f"{number_to_words(thousands)} thousand {number_to_words(remainder)}"