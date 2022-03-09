my_list = [2, 3 , 4, 4, 3, 1, 8, 0, 9]
my_final_list = set(my_list)
print(list(my_final_list))
#Write a Python program that matches a string that has an 'a' followed by zero or more 'b's
import re
def text_match(text):
    patterns = '^a(b*)$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return('Not matched!')
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb")) 
#Write a Python program that matches a string that has an 'a' followed by three 'b's.          
import re
def text_match(text):
    patterns = 'ab{3}?'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return('Not matched')
print(text_match("abbb"))
print(text_match("aabbbbbc"))
#Write a Python program that matches a word containing 'z'           
import re
def text_match(text):
    patterns = 'w\w*z.\w*'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return('Not matched')
print(text_match("The boy is lazy all the time"))
print(text_match("Python Excercises"))
#Write a Python program to search some literals strings in a string.
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox', 'dog', 'horse'
import re
patterns = [ 'fox', 'dog', 'horse' ]
text ='The quick brown fox jumps over the lazy dog'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text), )
else:
    print('Not Matched!')
