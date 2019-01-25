'''
boolsSeen = 0
bools = [not True, not False, True, False, True and False, True or False]
for expr in bools:
    if expr:
        boolsSeen += 1
print(boolsSeen)

mix = ['zero', 0, ['two'], -1]
print(mix[0:-1])

aList = ['one', -1, 2]
prefix = aList[:2]
suffix = aList[-1:]
print(prefix + suffix)

import turtle
s = turtle.Screen()
t = turtle.Turtle()
for i in range(4):
    if i%2 == 0:
        t.right(60)
        t.forward(100)
        t.right(60)
        
def check(aList):
    for element in range(len(aList)):
        if str(aList[element]) == aList[element+1]:
            return True
    return False

arg = [0, '0', 1, '1']
matched = check(arg)
print(matched)
'''

muchSnow = False
veryCold = True
takeTrain = True

if muchSnow:
 print("school closed")
else:
 print("give exam")
if veryCold:
 print("car won't start")
elif takeTrain:
 print("take exam")
else:
 print("miss exam")