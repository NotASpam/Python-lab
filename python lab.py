# write your code here
a = int(2)
b = int(5)
a,b = 2,5

# Taken from mission Variable: Declaration and Value Setting

# write your code here
a,b = 2,5


# write your code here
add = a+b
multi = a*b

# write your code here
def func () :
    pass

# Taken from mission Empty Function

# write your code here
def func (arg) :
    return arg


print("Example:")
print(func(3))

# These "asserts" are used for self-checking
assert func(3) == 3
assert func("string") == "string"
assert func(True) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")


def mult_two(a: int, b: int) -> int:
    # your code here
    return a*b


print("Example")
print(mult_two(1, 2))

assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0

print("The first mission is done! Click 'Check' to earn cool rewards!")


def is_even(num: int) -> bool:
    # your code here
    return num%2 == 0


print("Example:")
print(is_even(2))

# These "asserts" are used for self-checking
assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")


def determine_sign(num: int) -> str:
    txt = "zero"
    if num >0 :
        txt = "positive"
    elif num<0 :
        txt = "negative"
    return txt


print("Example:")
print(determine_sign(11))

# These "asserts" are used for self-checking
assert determine_sign(5) == "positive"
assert determine_sign(0) == "zero"
assert determine_sign(-10) == "negative"
assert determine_sign(1) == "positive"
assert determine_sign(-1) == "negative"
assert determine_sign(999) == "positive"
assert determine_sign(-1000) == "negative"
assert determine_sign(123456789) == "positive"
assert determine_sign(-987654321) == "negative"
assert determine_sign(2) == "positive"

print("The mission is done! Click 'Check Solution' to earn rewards!")



def find_remainder(dividend: int, divisor: int) -> int:
    # your code here
    return dividend%divisor


print("Example:")
print(find_remainder(3, 2))

# These "asserts" are used for self-checking
assert find_remainder(10, 3) == 1
assert find_remainder(14, 4) == 2
assert find_remainder(27, 4) == 3
assert find_remainder(10, 5) == 0
assert find_remainder(10, 1) == 0
assert find_remainder(5, 7) == 5
assert find_remainder(7, 5) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")


def backward_string(val: str) -> str:
    res = ""
    for i in range(len(val)) :
        res+= val[len(val) - i-1]
    return res


print("Example:")
print(backward_string("val"))

# These "asserts" are used for self-checking
assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"

print("The mission is done! Click 'Check Solution' to earn rewards!")


def checkio(num: int) -> str:
    res = str(num)
    if num%3 == 0 :
        res = "Fizz"
    return res


print("Example:")
print(checkio(3))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz"
assert checkio(6) == "Fizz"
assert checkio(10) == "10"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")


def first_word(text: str) -> str:
    return text.split(' ')[0]


print("Example:")
print(first_word("Hello world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")


def number_length(value: int) -> int:
    return len(str(value))


print("Example:")
print(number_length(10))

# These "asserts" are used for self-checking
assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2

print("The mission is done! Click 'Check' to earn cool rewards!")


# Taken from mission Just Fizz!

def checkio(num: int) -> str:
    res = str(num)
    if num%15 == 0 :
        res = "Fizz Buzz"
    elif num%3 == 0 :
        res = "Fizz"
    elif num%5 == 0 :
        res ="Buzz"        
    return res


print("Example:")
print(checkio(15))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")


def sum_upto_n(N: int) -> int:
    # your code here
    return N*(N+1)//2


print("Example:")
print(sum_upto_n(11))

# These "asserts" are used for self-checking
assert sum_upto_n(1) == 1
assert sum_upto_n(2) == 3
assert sum_upto_n(3) == 6
assert sum_upto_n(4) == 10
assert sum_upto_n(5) == 15
assert sum_upto_n(10) == 55
assert sum_upto_n(20) == 210
assert sum_upto_n(100) == 5050
assert sum_upto_n(200) == 20100
assert sum_upto_n(500) == 125250

print("The mission is done! Click 'Check Solution' to earn rewards!")


def to_title_case(sentence: str) -> str:
    # your code here
    return sentence.title()


print("Example:")
print(to_title_case("hello world"))

# These "asserts" are used for self-checking
assert to_title_case("hello world") == "Hello World"
assert to_title_case("openai gpt-4") == "Openai Gpt-4"
assert to_title_case("this is a title") == "This Is A Title"
assert to_title_case("THE QUICK BROWN FOX") == "The Quick Brown Fox"
assert to_title_case("JUMPs ovER a LAZy dog") == "Jumps Over A Lazy Dog"
assert to_title_case("typescript is great") == "Typescript Is Great"
assert to_title_case("the answer is 42") == "The Answer Is 42"
assert to_title_case("to be or not to be") == "To Be Or Not To Be"
assert to_title_case("that is the question") == "That Is The Question"
assert to_title_case("") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")


def factorial(n: int) -> int:
    res = 1
    for i in range(1,n+1) :
        res = res *i
    return res


print("Example:")
print(factorial(4))

# These "asserts" are used for self-checking
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800
assert factorial(15) == 1307674368000

print("The mission is done! Click 'Check Solution' to earn rewards!")


def between_markers(text: str, start: str, end: str) -> str:
    # your code here
    return text.split(start)[1].split(end)[0]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

# These "asserts" are used for self-checking
assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"

print("The mission is done! Click 'Check Solution' to earn rewards!")



def goes_after(word: str, first: str, second: str) -> bool:
    for i in range(len(word)-1) :
        if word[i] == first :
            if word[i+1] == second :
                return True
    return False


print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")



def max_digit(value: int) -> int:
    return max(int(i) for i in list(str(value)))


print("Example:")
print(max_digit(10))

# These "asserts" are used for self-checking
assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
assert max_digit(10000) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")


def sum_numbers(text: str) -> int:
    res = 0
    for word in text.split(' ') :
        if word.isdigit() :
            res += int(word)
    return res


print("Example:")
print(sum_numbers("hi"))

# These "asserts" are used for self-checking
assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (
    sum_numbers(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 3755
)
assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")


def checkio(words: str) -> bool:
    liste = words.split(' ')
    for i in range ( len (liste )- 2) :
        if not liste[i].isdigit() :
            if not liste[i+1].isdigit() :
                if not liste[i+2].isdigit() :
                    return True
    return False


print("Example:")
print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

def beginning_zeros(a: str) -> int:
    for i,d in enumerate(a) :
        if d != "0" :
            return i
    return len(a)


print("Example:")
print(beginning_zeros("10"))

# These "asserts" are used for self-checking
assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2
assert beginning_zeros("012345679") == 1
assert beginning_zeros("0000") == 4



def longest_word(sentence: str) -> str:
    words = sentence.split(' ')
    res = ""
    for i in words :
        if len(i) > len (res) :
            res = i
    return res


print("Example:")
print(longest_word("hello world"))

# These "asserts" are used for self-checking
assert longest_word("hello world") == "hello"
assert longest_word("openai gpt-4") == "openai"
assert longest_word("this is a sentence") == "sentence"
assert longest_word("the quick brown fox") == "quick"
assert longest_word("jumped over the lazy dog") == "jumped"
assert longest_word("typescript is great") == "typescript"
assert longest_word("the answer is 42") == "answer"
assert longest_word("to be or not to be") == "not"
assert longest_word("that is the question") == "question"
assert longest_word("") == ""
assert longest_word(" ") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")


def correct_sentence(text: str) -> str:
    text = text[0].upper()+text[1:]
    if text[-1] != "." :
        text+="."
    return text


print("Example:")
print(correct_sentence("greetings, friends"))

# These "asserts" are used for self-checking
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."

print("The mission is done! Click 'Check Solution' to earn rewards!")



def max_of_three(a: int, b: int, c: int) -> int:
    # your code here
    return max([a,b,c])


print("Example:")
print(max_of_three(1, 2, 3))

# These "asserts" are used for self-checking
assert max_of_three(1, 2, 3) == 3
assert max_of_three(3, 2, 1) == 3
assert max_of_three(1, 3, 2) == 3
assert max_of_three(0, 0, 0) == 0
assert max_of_three(-1, -2, -3) == -1
assert max_of_three(5, 5, 4) == 5
assert max_of_three(-5, -5, -6) == -5
assert max_of_three(10, 9, 10) == 10
assert max_of_three(123, 456, 789) == 789
assert max_of_three(789, 123, 456) == 789

print("The mission is done! Click 'Check Solution' to earn rewards!")


import re

def first_word(text: str) -> str:
    return re.findall(r"\b\w+'?\w*\b", text)[0]
    


print("Example:")
print(first_word(" a word "))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")



def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    res = abs(len(str1) - len(str2))
    for i in range (min(len(str1),len(str2))) :
        if str1[i] != str2[i] :
            res += 1
    return threshold >= res


print("Example:")
print(fuzzy_string_match("apple", "appel", 2))

# These "asserts" are used for self-checking
assert fuzzy_string_match("apple", "appel", 2) == True
assert fuzzy_string_match("apple", "bpple", 1) == True
assert fuzzy_string_match("apple", "bpple", 0) == False
assert fuzzy_string_match("apple", "apples", 1) == True
assert fuzzy_string_match("apple", "bpples", 2) == True
assert fuzzy_string_match("apple", "apxle", 1) == True
assert fuzzy_string_match("apple", "pxxli", 3) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")


def translation(text: str) -> str:
    look = 0
    res = ""
    for i in text :
        if look == 0 :
            if i in "aeiouy" :
                look = 2
            elif i != " " :
                look = 1
            res += i
        else :
            look -=1
    return res


print("Example:")
print(translation("hieeelalaooo"))

# These "asserts" are used for self-checking
assert translation("hieeelalaooo") == "hello"
assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translation("aaa bo cy da eee fe") == "a b c d e f"
assert translation("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")

def count_occurrences(main_str: str, sub_str: str) -> int:
    res = 0
    for i in range (0, len(main_str)-len(sub_str)+1) :
        print(main_str[i:i+len(sub_str)])
        if main_str[i:i+len(sub_str)].lower() == sub_str.lower() :
            res +=1
    return res


print("Example:")
print(count_occurrences("hello world hello", "hello"))

# These "asserts" are used for self-checking
assert count_occurrences("hello world hello", "hello") == 2
assert count_occurrences("Hello World hello", "hello") == 2
assert count_occurrences("hello", "world") == 0
assert count_occurrences("hello world hello world hello", "world") == 2
assert count_occurrences("HELLO", "hello") == 1
assert count_occurrences("appleappleapple", "appleapple") == 2
assert count_occurrences("HELLO WORLD", "WORLD") == 1
assert count_occurrences("hello world hello", "o w") == 1
assert count_occurrences("apple apple apple", "apple") == 3
assert count_occurrences("apple Apple apple", "apple") == 3
assert count_occurrences("apple", "APPLE") == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")


# Taken from mission Goes Right After (simplified)

def goes_after(word: str, first: str, second: str) -> bool:
    for i in range(len(word)-1) :
        if word[i] == first :
            if word[i+1].lower() == second.lower() :
                return True
    return False


print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
assert goes_after("Almaz", "a", "l") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")


def longest_prefix(arr: list[str]) -> str:
    unique = ""
    for i,char in enumerate( arr[0]) :
        for word in arr:
            if i<len(word) and word[i] != char :
                return unique
        unique += char             
    return unique


print("Example:")
print(repr(longest_prefix(["flower", "flow", "flight"])))

# These "asserts" are used for self-checking
assert longest_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_prefix(["dog", "racecar", "car"]) == ""
assert longest_prefix(["apple", "application", "appetizer"]) == "app"
assert longest_prefix(["a"]) == "a"
assert longest_prefix(["", "b"]) == ""
assert longest_prefix(["same", "same", "same"]) == "same"
assert longest_prefix(["mismatch", "mister", "miss"]) == "mis"
assert longest_prefix(["alphabet", "alpha", "alphadog"]) == "alpha"
assert longest_prefix(["book", "boot", "booster"]) == "boo"
assert longest_prefix(["short", "shore", "shot"]) == "sho"

print("The mission is done! Click 'Check Solution' to earn rewards!")


def reverse_digits(num: int) -> int:
    stri = str(num)
    str2 = ""
    for i in range(len(stri)) :
        str2+= stri[len(stri) -i-1]
    if str2[-1] == "-" :
        str2 = "-"+str2[:-1]
    return int(str2)


print("Example:")
print(reverse_digits(32))

# These "asserts" are used for self-checking
assert reverse_digits(1234) == 4321
assert reverse_digits(0) == 0
assert reverse_digits(-123) == -321
assert reverse_digits(5) == 5
assert reverse_digits(-9) == -9
assert reverse_digits(100) == 1
assert reverse_digits(-100) == -1
assert reverse_digits(54321) == 12345
assert reverse_digits(1111) == 1111
assert reverse_digits(987654321) == 123456789

print("The mission is done! Click 'Check Solution' to earn rewards!")


def is_armstrong(num: int) -> bool:
    stri = str(num)
    sum = 0
    for digit in stri :
        sum+=int(digit)**len(stri)
     
    return num == sum


print("Example:")
print(is_armstrong(11))

# These "asserts" are used for self-checking
assert is_armstrong(153) == True
assert is_armstrong(370) == True
assert is_armstrong(947) == False
assert is_armstrong(371) == True
assert is_armstrong(407) == True
assert is_armstrong(163) == False
assert is_armstrong(100) == False
assert is_armstrong(8208) == True
assert is_armstrong(930) == False
assert is_armstrong(4) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")


import datetime
def convert_date(date: str) -> str:
    inter = date.split("/")
    try:
        datetime.datetime(year = int(inter[2]), month = int(inter[1]), day = int(inter[0])) 
    except ValueError :
        return "Error: Invalid date."
    if len(inter[0]) != 2 or len(inter[1]) != 2 or len(inter[2]) != 4 or len(inter) != 3 :
        return "Error: Invalid date."
    
    return inter[2]+"-"+inter[1]+"-"+inter[0]


print("Example:")
print(convert_date("01/01/2023"))

# These "asserts" are used for self-checking
assert convert_date("25/12/2021") == "2021-12-25"
assert convert_date("01/01/2000") == "2000-01-01"
assert convert_date("15/06/1995") == "1995-06-15"
assert convert_date("29/02/2020") == "2020-02-29"
assert convert_date("10/10/2010") == "2010-10-10"
assert convert_date("31/05/1985") == "1985-05-31"
assert convert_date("07/08/1960") == "1960-08-07"
assert convert_date("02/09/1999") == "1999-09-02"
assert convert_date("30/04/1975") == "1975-04-30"
assert convert_date("29/02/2019") == "Error: Invalid date."
assert convert_date("30/04/1975/1") == "Error: Invalid date."

print("The mission is done! Click 'Check Solution' to earn rewards!")


from collections.abc import Iterable
from itertools import permutations


def string_permutations(s: str):
    perm = set(''.join(p) for p in permutations(s))
    return sorted(perm)
     


print("Example:")
print(list(string_permutations("ab")))

# These "asserts" are used for self-checking
assert list(string_permutations("ab")) == ["ab", "ba"]
assert list(string_permutations("abc")) == ["abc", "acb", "bac", "bca", "cab", "cba"]
assert list(string_permutations("a")) == ["a"]
assert list(string_permutations("abcd")) == [
    "abcd",
    "abdc",
    "acbd",
    "acdb",
    "adbc",
    "adcb",
    "bacd",
    "badc",
    "bcad",
    "bcda",
    "bdac",
    "bdca",
    "cabd",
    "cadb",
    "cbad",
    "cbda",
    "cdab",
    "cdba",
    "dabc",
    "dacb",
    "dbac",
    "dbca",
    "dcab",
    "dcba",
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
