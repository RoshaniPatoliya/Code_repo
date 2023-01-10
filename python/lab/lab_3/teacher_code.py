import re
def multi_re_find(patterns, phrase):
    """
    Takes in a list of regex patterns
    print a list of matches
    """
    for pattern in patterns:
        print("Searching the phrase using the re check: %r"% pattern)
        print(re.findall(pattern,phrase))
        print('\n')
# * repetead zero or more times
# + must appear at least once
# ? pattern appears zero or 1 time
# use {m} after the pattern where m is replaced with the number of times the pattern should repeat
# use {m,n} m is minimum and n is max
test_phrase = "sdsd...sssddd...sdddsddd...dsds...dsssss...sdddd"
test_patterns = [
    'sd*',
    'sd+',
    'sd?',
    'sd{3}',
    'sd{2,3}',
]
#multi_re_find(test_patterns, test_phrase)
#test_phrase = "This is a string! But it has punctation. How can i remove it?"
#[^!.? ]
#print(re.findall('[^!.? ]+', test_phrase))
test_phrase = "This is an example sentence. Lets see if we can find som letters."
test_patterns=[
    '[a-z]+',
    '[A-Z]+',
    '[a-zA-Z]+',
    '[A-Z][a-z]+',
]
#multi_re_find(test_patterns,test_phrase)
tst_pharse = "This is a string_ with some numbers 1234 and a symbol #hashtag"
tst_patterns=[
    r'\d+', # sequence of digits
    r'\D+', # Non-digits
    r'\s+', # whitespace
    r'\S+', # Non-whitespace
    r'\w+', # alphanumeric characters
    r'\W+', # Non-alphanumeric
]
multi_re_find(tst_patterns,tst_pharse)