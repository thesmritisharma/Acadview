#TUPLES
print("           TUPLES")
#Question 1
tup1 = ('Hello', 6, 'How', 84, 'Bye')
print("Q.1-\n     Tuple:", tup1)
print("     Length of Tuple:", len(tup1))

#Question 2
tup2 = (67, 23, 82, 56, 10)
print("Q.2-\n     Tuple:", tup2)
print("     Smallest Element:", min(tup2))
print("     Largest Element:", max(tup2))

#Question 3
tup3 = (1, 2, 3, 4, 5)
print("Q.3-\n     Tuple:", tup3)
prod = 1
for item in tup3:
    prod = prod * item
print("     Product of Elements:", prod)

#SETS
print("           SETS")
#Question 4(1)
set1 = {'Apple', 'Orange', 'Banana'}
set2 = {'Apple', 23, 86}
print("Q.1-\n     Set 1:", set1)
print("\n     Set 2:", set1,"\n")
print("(1)- Difference:", set1-set2)

#Question 4(2)
if (set1 <= set2) & (set2 <= set1):
    print("(2)- Comparison:", "Equal")
print("(2)- Comparison:", "Not Equal")

#Question 4(3)
print("(3)- Intersection:", set1 & set2)

#DICTIONARIES
print("\n           DICTIONARIES")
#Question 1
print("Q.1-\n     ")
dict = {}
keys = ["Smriti", "Siddhant", "Vipul", "Piyush", "Simran", "Tushar", "Radhika", "Shreya", "Rajat", "Shaffi"]
for i in keys:
        print("Enter marks of %s: " % i)
        dict[i] = input()
print("Dictionary:", dict)
