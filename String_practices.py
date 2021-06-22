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
"""output()
s = "orange"
print("orange" in "This is orange juice" )
completed()"""
#________ OUTPUT _________
#True
#--------------------------------x--------------------------------------

# TESTING
"""strings="The lyrics is not that poor!"
s1=strings.find("not")
s2=strings.find("poor")
print(s1)
print(s2)"""

# EXAMPLE-1 CODE TEST ONLINE
"""def not_poor(str1,re_string):
    find_str = str1.find(re_string)
    last_str = len(str1)
    if find_str >= 0:
        str1 = str1.replace(str1[find_str:(last_str-1)], 'good')
        return str1
    else:
        return str1
print(not_poor('The lyrics is poor but not that much of poor!',"poor"))
print(not_poor('The lyrics is poor!',"poor"))"""

# UNDERSTANDING BASED THIS EXAMPLE-1
"""FIND THE STRING INDEX NUMBER AND SLICING THE STRING AND REPLACE STRING USE replace()"""
# CODE
"""def not_poor(str1):
    #snot = str1.find('not') ==>14
    #spoor = str1.find('poor') ==>23
    if 23 > 14 and 14 > 0 and 23 > 0:
        str1 = str1.replace(str1[14:(23 + 4)], 'good')
        return str1
    else:
        return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))"""

#8. PRACTICE STRING INTERVIEW QUESTION:

# LEARNING-1  CHECKING STRING VALUE IS POLYNDROME OR NOT
"""output()
str1="MADAM"
l=len(str1)
s=""
for i in range(l-1,-1,-1): # Reverse the value using range function
    s+=str1[i]
if s == str1:
    print("It is polyndrome")
else:
    print("It is symmetric")
completed()"""
#________ OUTPUT _________
#It is polyndrome
#--------------------------------x--------------------------------------

# LEARNING-2 CHECKING NUMBER IS POLYNDROME OR NOT
"""LOGIC :
        r=n%10
        sum=(sum*10)+r
        n=n/10
"""
num = 151
sum=0
while (num>0):
    r=num%10
    sum=(sum*10)+r
    num=num/10
if num == sum:
    print("Polyndrome number")
else:
    print("not polyndrome")

#
