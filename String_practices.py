#practice_string

def completed():
    print("#--------------------------------x--------------------------------------")
def output():
    print("#________ OUTPUT _________")
def error():
    print("#xxxxxxxxxxx ERROR xxxxxxxxxxxx")
def Note():
    print("#========== NOTE =============")


#1. PRINT STRING USINF print():
"""output()
print("Hello")
print('jotheeswaran')
completed()"""
#________ OUTPUT _________
#Hello
#jotheeswaran
#--------------------------------x--------------------------------------

#2. PRINT MULTILINE STRING USING print() and WITH VARIABLE DECLARATION:
"""output()
a="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididuntut labore et dolore magna aliqua."
print(a)
completed()
Note()
"""
#========== NOTE =============
"""NOTE: single line only we can print in double quotes(") and single quotes(') but we cannot print multi line
if we need to multiline print use triple quotes(\""")
"""
#________ OUTPUT _________
# SINGLE LINE:
#Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididuntut labore et dolore magna aliqua.
#--------------------------------x--------------------------------------

#2.1- PRINT MULTILINE :
#output()
#a="""NOTE: single line only we can print in double quotes(")
#and single quotes(') but we cannot print multi line
#if we need to multiline print use triple quotes(\""").
#"""
#print(a)
#completed()
#________ OUTPUT _________
#"""NOTE: single line only we can print in double quotes(")
#and single quotes(') but we cannot print multi line
#if we need to multiline print use triple quotes(\""")
#"""
#--------------------------------x-----------------------------------

#3. CONVERT LIST TO STRING:

"""output()
a=['s', 't', 'r', 'i', 'n', 'g']
str1=""
for i in a:
    str1+=i
print(str1)
completed()"""
#________ OUTPUT _________
#string
#--------------------------------x--------------------------------------

#4. REPLACE THE STRING VALUE:

"""output()
c=""
s ="strong"
# need to replace 'o' to 'i'
b=list(s)
b[3]='i'
for str1 in b:
    c+=str1
print(c)
completed()"""

#________ OUTPUT _________
#string
#--------------------------------x--------------------------------------

#5. REPLACE THE PARTICULAR WORD IN STRING
"""output()
str1=""
s = "Replace the particular word in string"
a=s.split(' ')
a[1]= 'the value'
out = ' '.join(str(i) for i in a)
print(out)
completed()"""

#________ OUTPUT _________
#Replace the value particular word in string
#--------------------------------x--------------------------------------

#6. PRACTICE INTERVIEW QUESTION

###########

#7. VERIFY STRING EXIST OR NOT:

s = "orange"
print("orange" in "This is orange juice" )

