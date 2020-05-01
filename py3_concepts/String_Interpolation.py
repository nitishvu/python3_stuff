'''
python 3 String interpolations

1. F strings
2. str.format()
3. % formatting
4. Template strings
5. i Strings (coming soon)

'''

# 1. f strings

a = 'my'
b = 'python'

print(f"this is {a}_{b} repo.")

'''
O/P:
this is my_python repo.
'''


#we can include python expression inside strings

i= 10
j= 5
print(f'10*5 = {i*j}')

'''
O/P:
10*5 = 50
'''

#2. Str.format

print("this is {}_{} repo.".format(a,b))
'''
O/P:
this is my_python repo.
'''

#3. % formatting

print("this is %s_%s repo."%(a,b))

'''
O/P:
this is my_python repo.

'''


'''
4. Template strings
python3 Template strings provide simpler string substitutions.
A primary use case for template strings is for internationalization (i18n) since in that context,
the simpler syntax and functionality makes it easier to translate
than other built-in string formatting facilities in Python. 
'''

# Here is an example of how to use a Template:
from string import Template
s = Template('$i likes to $what.')

#substitute will raise KeyError incase required key is not present in the input  (remove whant and try)
new_string = s.substitute(i='Nitish', what="play")
print(new_string)

#based on user preference we can try multiple languages
english = dict(who='nitish',what='play')
french = dict(who='nitish',what='jouer')

#safe_substitute  doesnt expect all keys
print(Template('$who likes to $what').safe_substitute(english))
print(Template('$who likes to $what').safe_substitute(french))

'''
O/P:
Nitish likes to play.
nitish likes to play
nitish likes to jouer

'''

