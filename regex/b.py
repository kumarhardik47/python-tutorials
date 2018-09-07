import os
import re


string = "abbbbbbba"

pattern = re.compile(r'^ab+') ### after a, b should be there (1+ occurence of b)
out = pattern.search(string)
print out.group()

string2 = "accccbbbbbb"
pattern = re.compile(r'^ab?') ##  after a, not necessary to have b (0 or 1 ocurence of b)
out = pattern.search(string2)
print out.group()

#a followed by 3 b
string3 = "abbbaabbbb"
pattern = re.compile(r'^abbb')
out = pattern.search(string3)
print out.group()


#a followed by 2,3 b
string4 = "abbabbbab"
pattern = re.findall(r'ab{2,3}', string4)
print pattern

#sequence of lowercase letters joined with underscore
string5 = "abasda_dsasdasd"
pattern = re.compile('^[a-z]*_[a-z]*')
if pattern.search(string5):
	print string5
else:
	print "Not found sequence of lowercase letters joined with underscore"

#sequence of one uppercase letter followed by lowecase letter
string6="asdasdWojiojsid"
#pattern = re.compile('^[A-Z][a-z]*')
pattern = re.compile('[A-Z][a-z]*')
if pattern.search(string6):
	print string6
else:
	print "No such sequence of one uppercase letter followed by lowecase letter"
# string that has a followed by anything, ending with b
string7="asdasdWoj98798732iojsidb"
pattern = re.compile('a[A-Za-z0-9]*b$')
if pattern.search(string7):
	print string7
else:
	print "string that has a followed by anything, ending with b"

#srting starting with particular word
string8 = "hardik is a python developer"
pattern = re.compile('^hardik')
if pattern.search(string8):
	print string8
else:
	print "Not found srting starting with particular word"


#srting ending with particular word and optional punctuation
string9 = "hardik is a python developer"
pattern = re.compile('developer[.!?,;\'"]?$')
if pattern.search(string9):
	print string9
else:
	print "Not found srting ending with particular word and optional punctuation"

#word containing d
string10 = "hardik is not a python developerd\n \nasdd"
#pattern = re.findall('\w*', string10)#['hardik', '', 'is', '', 'not', '', 'a', '', 'python', '', 'developerd', '', '', '', 'asdd', '']
#pattern = re.findall('\w*d', string10) # ['hard', 'developerd', 'asdd']
#pattern = re.findall('\w*d\w', string10) #['hardi', 'de', 'asdd']
#pattern = re.findall('\w*d\w*', string10) #['hardik', 'developerd', 'asdd']
################# Here \w takes every character
pattern = re.findall('\w*d.\w*', string10) #['hardik', 'developerd', 'asdd']
if pattern:
	print pattern
else:
	print "Not found word containing d"


#word containing d but not at start or at end
string11 = "hardik is not a python developerd asdd"
pattern = re.findall('\Bh\w\B', string11) 
if pattern:
	print pattern
else:
	print "Not found word containing d"


#"Exercises number 1, 12, 13, and 345 are important" --> get numbers

string12 = "Exercises number 1, 12, 13, and 345 are important 34345"
pattern = re.findall(r'([0-9]{1,3}[\, ])',string12)
if pattern:
	print pattern
else:
	print "No numbers found"


#search a literals string in a string and also find the location within the original string where the pattern occurs
string13 ="The quick brown fox jumps over the lazy dog."
pattern = "fox"

out = re.search(pattern,string13)
if out:
	print out.group(), out.start(), out.end()
else:
	print "Not found"

#find the substrings within a string
string14 = "Python exercises, PHP exercises, C# exercises"
pattern = "exercises"
out = re.findall(pattern,string14)
if out:
	print out
else:
	print "No substring not found"

########################################DIFFERENT ##############################
#########################################TRY ################################
#program to find the occurrence and position of the substrings within a string
string15 = "Python exercises, PHP exercises, C# exercises"
pattern = "exercises"
for match in re.finditer(pattern, string15):
	if match:
		print string15[match.start():match.end()], match.start(), match.end()
	else:
		print "No substring found"


#replace whitespaces with an underscore and vice versa. They are two programs in one
string16 = "Python_exercises"
#NOTE: re.sub() can also be done


text = string16.replace("_"," ")
print text
text = string16.replace(" ","_")
print text

# extract date from url
url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/899/odelllittle-ball-josh-norman-tells-author/"
out = re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url) # 3 patterns in three () 
if out:
	print out

#######################TODO: IMPORTANT##############
#convert a date of yyyy-mm-dd format to dd-mm-yyyy format
string17 = "2018-03-09"
out = re.sub('(\d{4})-(\d{1,2})-(\d{1,2})','\\3-\\2-\\1',string17)
if out:
	print "original date:",string17, "new_date:", out


#match if two words from a list of words starting with letter 'P'
string18="Hello My name is Prem Patani"
out = re.findall(r'P[a-zA-Z]*',string18)
if out:
	print out
else:
	print "No words starting with P found"


#match if two words from a list of words starting with letter 'P'
words = ["Python PHP", "Java JavaScript", "c c++"]
#print words, str(words)
out = re.findall(r'P[a-zA-Z]*',str(words))
if out:
	print out
else:
	print "No words starting with P found"


#Separate numbers and print them
text = "Ten 10, Twenty 20, Thirty 30"
#out = re.findall('[0-9]+',text)
###OR###
out = re.split("\D+",text)
if out:
	print out
else:
	print "No numbers found in the string"


#find all words starting with 'a' or 'e' in a given string
string19 = "Afterall my name is emily rose anderson"
#s = re.split(" ", string19)
#for word in s:
#	if word.startswith('a') or word.startswith('e'):	
#		print word

#the above gives more accurate result
out = re.findall('[AEae]\w+', string19)
if out:
	print out
else:
	print "Not found words starting with a or e"


#separate and print the numbers and their position of a given string.
string20 = "Ten 10, Twenty 20, Thirty 30"
pattern = re.compile(r'[0-9]+')
for match in re.finditer(pattern, string20):
	if match:
		print string20[match.start():match.end()], match.start(), match.end()


#abbreviate 'Road' as 'Rd.' in a given string
string21 = "i will use Burlinghame Road"
out = re.sub("Road","Rd.",string21)
if out:
	print out

#replace all occurrences of space, comma, or dot with a colon.
string22 = "Hello Hardik. How are you? And, where have you been?"
out = re.sub(" ",":",string22)
out1 = re.sub(",",":",out)
out2 = re.sub("\.",":",out1)
if out2:
	print out2

#replace maximum 2 occurrences of space, comma, or dot with a colon.
string22 = "Hello  Hardik.. How are you? And,, where have you been?"
out = re.sub("  ",":",string22)
out1 = re.sub(",,",":",out)
out2 = re.sub("\.\.",":",out1)
if out2:
	print out2

#find all five characters long word in a string.
string23 = "Hello Hardik Mahto !! Where have you been these days?"
words = string23.split(" ")
print '*' * 80
for word in words:
	if len(word)==5:
		print word
print '*' * 80


#find all three, four, five characters long words in a string. 
string24 = "Hello Hardik Mahto !! Where have you been these days?"
words = string24.split(" ")
print '*' * 80
for word in words:
	if len(word) in (3,4,5):
		print word
print '*' * 80

#find all words which are at least 4 characters long in a string.
string25 = "Hello Hardik Mahto !! Where have you been these days?"
words = string25.split(" ")
print '*' * 80
for word in words:
	if len(word) >= 4:
		print word
print '*' * 80

################################################TWIST#######################################
#convert camel case string to snake case string.
#camel case sample = MatchWord
#snake case sample = Match_Word
string26 = "HelloHardik"
s = re.sub('(.)([A-Z][a-z]+)',r'\1_\2',string26).lower()
print s

#convert camel case string to snake case string.
string26 = "hello_hardik"
out = "".join(x.capitalize() for x in string26.split("_"))
print out


#extract values between quotation marks of a string
string27 = "Hello \"Hardik\" how are you?"
print re.findall('\"([A-Za-z]+)\"',string27)

#remove multiple spaces in a string
string28 = "Hello Hardik              Mahto !! Where have you been these days?"
print re.sub(" +"," ",string28)


#remove all whitespaces from a string
string28 = "Hello Hardik              Mahto !! Where have you been these days?"
print re.sub("\s+"," ",string28)



#remove everything except alphanumeric characters from a string.
