#!/bin/python3

#Importing

print("Importing is important:")
import sys #system function and parameters(sys is a module here the whole module is imported.)
from datetime import datetime# a part of the module datetime is imported.
print(datetime.now())

from datetime import datetime as dt # importing with an alias
print(dt.now())

def new_line():
    print('\n')

new_line()

#Advanced Strings 

print("Advanced strings:")
my_name = "Heath"
print(my_name[0])#first initial
print(my_name[-1])#last letter

sentence = "This is a sentence."

print(sentence[:4]) #first word

print(sentence[-9:-1])#last word

print(sentence[-0])#the out put would be the first letter because there is no minus zero.
print(sentence.split()) # split sentence by delimiter (space)

sentence_split = sentence.split()
sentence_join =' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))

quoteception = "I said, 'give me all the money'"
print(quoteception)

quoteceptin = "I said, \"give me all the money\""
print(quoteception)

print( "A" in "Apple")

letter1 = "A"
letter2 = "a"
word = "Apple"
print(letter1 in word)#true
print(letter2 in word)#false 
print(letter2.lower() in word.lower())#true#improved - cae insensitive

word_two = "Bingo"
print((letter2.lower() in word.lower()) and not (letter2.lower() in word_two.lower()))


too_much_space = "                    hello                       "
print(too_much_space)
print(too_much_space.strip())

full_name = "eath Adams"
print(full_name.replace("eath", "Heath"))
print(full_name.find("Adams"))

movie = "The Hangover"
print("My favourite movie is {}.".format(movie))

def favorite_book(title, author):
    fav = "My favorite book is \"{}\", which is written by {}".format(title,author)
    return fav

print(favorite_book("The Great Gatsby", "F. Scott Fitzgerald"))


new_line()

#Dictionaries 

print("Dictionaries are keys and values:")#[for list],(tuples), {Dictionaries}
drinks = {"White Russians": 7,"Old Fashion" : 10, "Lemon Drop":8,"Buttery Nipple":6}#drink is key, price is value #{key,value}
print(drinks)

employees = {"Finance":["Bob", "Linda", "Tina"],"IT":["Gene","Louise","Teddy"],"HR":["Jimmy Jr.", "Mort"]}
print(employees)

employees['Legal'] = ["Mr. Frond","Tarek"] #add new key: value pair
print(employees)

employees.update({"Sales":["Andie","Ollie"]})
print(employees)

drinks['White Rassians']=8
print(drinks)

print(drinks.get("White Russians"))
print(drinks.get("Martini"))
print(drinks["White Russians"])


#List and dictionries

movies = [ "When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]
person = ["Heath", "Bob", "Leah", "Jeff"]

combined = zip(movies, person)
movie_dictionary = {key:value for key, value in combined}
print(movie_dictionary) 

''' if you want to make a content of a folder online on your ip-address using python you have to into that folder und type the following command: python -m http.server 80.You can use this command too:python3 -m http.server 80 . 80 stands for the port number'''
	
'''commands:pip install pyftpdlib. Pip  is  a  Python  package  installer,  recommended for in‐
       stalling Python packages which are not available in the  De‐
       bian archive. we have installed the pyftpdlib.
       Python FTP server library provides a high-level portable interface to easily write asynchronous FTP servers with Python. 
pyftpdlib is currently the most complete RFC-959 FTP server implementation available for Python programming language. It is used in projects like Google Chromium and Bazaar. '''

