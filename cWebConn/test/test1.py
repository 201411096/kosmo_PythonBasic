from ast import literal_eval

str1 = '(a, b, c)'
str1 = literal_eval(str1)
print(type(str1))