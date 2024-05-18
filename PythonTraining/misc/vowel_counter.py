"""
Write a program that takes a sentence and do following tasks using multiple functions
    - a function should give the list of all vowel alphabets present in the provided sentence.
    - a function should give the count of all vowel alphabets
    - a function should give the unique list of all vowel alphabet present in the provided sentence. 
    - a function should give the unique count of all the vowel alphabet present in the provided sentence.
"""

def get_vowels(input_string):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowels_in_input_string = []
    for c in input_string:
        if c in vowels:
            vowels_in_input_string.append(c)

    return vowels_in_input_string


def get_vowels_count(input_string):
    vowels = ["a", "e", "i", "o", "u", "A", "I", "E", "O", "U"]
    vowels_count = 0
    for c in input_string:
        if c in vowels:
            vowels_count += 1  # equivalent to vowels_count = vowels_count + 1

    return vowels_count


def test_get_vowels_count():
    print("test function called")
    sample_string = "house"
    v_count = get_vowels_count(sample_string)

    assert v_count == 3

    sample_string2 = "DIPAK"
    v_count2 = get_vowels_count(sample_string2)
    assert v_count2 == 2


def main():
    # sentence = input("Enter a sentence\n")
    # result = get_vowels(sentence)
    # print(result)
    
    # vowel_count = len(result)
    # print(vowel_count)
    # # or
    # vowel_count = get_vowels_count(sentence)
    # print(vowel_count)

    test_get_vowels_count()


main()

