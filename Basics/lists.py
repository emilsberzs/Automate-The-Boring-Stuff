import random

spam = [['cat','bat'],[1,2,3,4,5]]
print(spam[1][-1])
print(spam[1][0:3])

spam= [1,2,3,4,5,6,7,8,9]
random.shuffle(spam) #Shuffles and replaces current list

spam.index(1)  #Gets index
spam.append(10) #Appends at end
spam.insert(0,0) #Inserts at first argument
spam.remove(1) #Removes first occurrence of value
spam.sort() #sorts list in place, can pass argument
spam.reverse() #Reverses list in place
print(spam[3:]) #From index to end (not including)
print(spam[:3]) #From start to index (not including)
print(spam[3:6]) #From index to index
print(len(spam)) #Length of list



ham = ['cat','bat','rat','fat']
print(ham)

ham[0] = 'dog' #Sets specified item
print(ham)

ham[1] = ham[2] 
print(ham)

del ham[1:] #Deletes everything starting from index 
print(ham)

ram = spam + ham #Joins both lists into one
print(ram)

dam = ham + spam
print(dam)

print(random.choice(ram)) #Prints random element of list
print(spam)

