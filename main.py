import re

"""
Challenge 1:
    Make a function that receives as parameter a string, and return true or false
    if the string can read it at the same way at reverse
"""

def is_palindrome(string:str):
    lowered_string = string.lower()
    string_no_spaces = lowered_string.replace(" ", "")
    return string_no_spaces == string_no_spaces[::-1]

"""
Challenge 2:
    Make a function that receives as parameter a string, and return the first character
    repeted in the string or return None if no repeted characters
"""

def character_repet(string:str):
    lowered_string = string.lower()
    string_no_spaces = lowered_string.replace(" ", "")
    split_string = []
    for character in string_no_spaces:
        if character in split_string:
            return character
        split_string.append(character)
    return None

"""
Challenge 3:
    Make a function that receives as parameter a string with hour format 12:30 AM/PM, and return
    the same value but in 24 hrs format, for example 11:30 PM - 23:30
"""
    
def hour_formater(string:str):
    hour_split = string.split(sep=":")
    if string[-2:].lower() == "pm":
        if hour_split[0] != "12":
            return f"{(int(hour_split[0]) + 12)}:{hour_split[1]}"
    else:
        if hour_split[0] == "12":
            return f"00:{hour_split[1]}"
    return string

"""
Challenge 4:
    Make a function that receives as parameter two strings, and return boolean answer if
    both string are anagrams
"""

def is_anagram(first_string:str, second_string:str):
    first_string_characters = sorted(first_string.lower().replace(" ", ""))
    second_string_characters = sorted(second_string.lower().replace(" ", ""))
    return first_string_characters == second_string_characters

"""
Challenge 5:
    Make a function that receives as parameter string, this string
    "Slugyfied"
"""

def slugify(string:str):
      non_symbols_string = "".join(re.findall("[a-zA-Z- ]+", string))
      return non_symbols_string.replace(" ", "-")


"""
Challenge 6:
    Make a function that receive as parameter string and return if all parenthesis
    its closed properly
"""

def parenthesis_balance(string:str):
    open = 0
    if string[0] == ")" or string[-1] == "(" or string.count("(") != string.count(")"):
        return False
    for character in string:
        if character == "(":
            open += 1
        elif character ==")":
            open -= 1
            if open < 0:
                return False
    return open == 0

    


# print(parenthesis_balance("(()))(())(()"))

# print(slugify('this is%$ a test23#$@$# just-for slugy##'))

# print(is_anagram("amor", "roma"))

# print(hour_formater("12:30 PM"))

# print(character_repet("Hola mundo"))

# print(is_palindrome('Anita lava la tina'))