fishLine = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
indx = 0
while indx < len(fishLine):
     if len(fishLine[indx]) == 4:
         indx += 1
         continue
     indx += 5
print(indx)