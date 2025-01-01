import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

def get_digit_in_word(digit):
    if digit == 1:
        return "one"
    if digit == 2:
        return "two"
    if digit == 3:
        return "three"
    if digit == 4:
        return "four"
    if digit == 5:
        return "five"
    if digit == 6:
        return "six"
    if digit == 7:
        return "seven"
    if digit == 8:
        return "eight"
    if digit == 9:
        return "nine"
    return ""

def get_tens_digit_in_word(digit):
    if digit == 2:
        return "twenty"
    if digit == 3:
        return "thirty"
    if digit == 4:
        return "forty"
    if digit == 5:
        return "fifty"
    if digit == 6:
        return "sixty"
    if digit == 7:
        return "seventy"
    if digit == 8:
        return "eighty"
    if digit == 9:
        return "ninety"
    return ""

def get_number_in_words_from_position(digit, position):
    digit_string = str(digit)
    if set(digit_string) == {'0'}:
        return ""
    if position == 2:
        if digit >= 20:
            return "{} {}".format(get_tens_digit_in_word(int(digit_string[0])), get_digit_in_word(int(digit_string[1])))
        if digit < 10:
            return get_digit_in_word(digit)
        if digit == 10:
            return "ten"
        if digit == 11:
            return "eleven"
        if digit == 12:
            return "twelve"
        if digit == 13:
            return "thirteen"
        if digit == 14:
            return "fourteen"
        if digit == 15:
            return "fifteen"
        if digit == 16:
            return "sixteen"
        if digit == 17:
            return "seventeen"
        if digit == 18:
            return "eighteen"
        if digit == 19:
            return "nineteen"
        print("ERROR: {}", digit_string)
        exit()
    if position == 3:
        return "{} hundred".format(get_digit_in_word(int(digit_string[0])))
    if position == 4:
        return "{} thousand".format(get_digit_in_word(int(digit_string[0])))

def get_number_in_words(number):
    if number < 100:
        return get_number_in_words_from_position(number, 2)
    if number < 1000:
        hundred_words = get_number_in_words_from_position(number, 3)
        tens_words = get_number_in_words_from_position(int(str(number)[1:]), 2)
        if len(tens_words) > 0:
            return "{} and {}".format(hundred_words, tens_words)
        return hundred_words
    if number < 10000:
        thousand_words = "{} {}".format(get_number_in_words_from_position(number, 4), get_number_in_words_from_position(int(str(number)[1:]), 3))
        tens_words = get_number_in_words_from_position(int(str(number)[2:]), 2)
        if len(tens_words) > 0:
            return "{} and {}".format(thousand_words, tens_words)
        return thousand_words

count = 0
for i in range(1, input_value + 1):
    number_words = get_number_in_words(i)
    count += len(number_words) - number_words.count(' ')
print(count)
