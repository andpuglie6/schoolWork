print("#Andre Pugliese")
print("#CS 100-H01")
print("#HW 04, Sept 21, 2017")

# Exercise 1

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for i in months:
    if(i[0] == "J"):
        print(i)
else:
    if(i[0] != "J"):
        print("")
        
# Exercise 2

for x in range(0, 100, 10):
    print(x)
    
# Exercise 3

horton = "A person's a person, no matter how small"
vowels = "aeiouAEIOU"

for v in horton:
    if v in vowels:
        print(v)