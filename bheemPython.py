""""
---------------PROBLEM STATEMENT-----------------------------------

A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string S, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

* Print the three most common characters along with their occurrence count.
* Sort in descending order of occurrence count.
* If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

GOOGLE would have it's logo with the letters G,O,E.

Input Format

A single line of input containing the string S.

Constraints
 3<len(s)<=10^4
 
Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0

aabbbccde
Sample Output 0

b 3
a 2
c 2
Explanation 0

aabbbccde

Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string S has at least 3 distinct characters

""""









s = input()
s1 = {}
s2 = {}
for i in s:
    if i in s1:
        s1[i] += 1
    else:
        s1[i] = 1
for j in range(1,4):
    for i in s1:
        if s1[i] == max(s1.values()):
            s2[i] = max(s1.values())
            break
    s1[i]= 0
names = []
values  = []
for i,j in s2.items():
    names.append(i)
    values.append(j)
if values[0]==values[1]==values[2] :
    names = sorted(names)
elif values[0]==values[1]:
    names[0:2] = sorted(names[0:2])
elif values[1]==values[2]:
    names[1:3] = sorted(names[1:3])
for i in range(0,3):
    print(names[i],":",values[i])
    
