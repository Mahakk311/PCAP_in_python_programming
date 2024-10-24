# step 1 - create an empty list named beatles;

beatles = []
print("Step 1:", beatles)

# step 2 - use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;

beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Step 2:", beatles)

# step 3 - use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;

for i in range(len(beatles)-1):
    beatles.append(input('Enter singer\'s name:'))

print("Step 3:", beatles)


# step 4 - use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
for i in range(2):
    del beatles[-1]

print("Step 4:", beatles)


# step 5 - use the insert() method to add Ringo Starr to the beginning of the list.
beatles.insert(0, 'Ringo Star')
print("Step 5:", beatles)
