rand_string = "   String   "

# Stripping whitespace

rand_string.lstrip()
rand_string.rstrip()
rand_string.strip()

text = "text"
text.capitalize() #Text
text.upper() #TEXT
list = ["stuff", "lol", "yylol"]
" ".join(list) # stuff lol yylol

#count the number of occurrances of a keyword in a string

text.count("keyword")

def acronym(text):
    text = text.upper()
    list = text.split()
    acronym = ""
    for word in list:
        acronym += word[0]
    return acronym


def ceasarCyph(text, rot):
    cyphrTxt = ""
    for char in text:
        if !char.isSpace():
            cyphrTxt += chr(ord(char) + rot%26)
    return cyphrTxt
