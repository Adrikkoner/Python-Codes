#List defination

a = [1,1,5,8,6,5]
print(a)

#List append()
a.append(10)
print(a)
b = [1,5,8]
a.append(b)
print(a)
a.append('addffg')
print(a)

#List extend
a = [4,5,8,5,6,7]
b = [7,8,5,8,4,6]
a.extend(b)
print(a)
c = a + b
print(c)

# List Index
print(c.index(4))

# List insert
c.insert(0,1)
print(c)

# list pop
c.pop(0)
print(c)

# reverse
c.reverse()
print(c)

# List count
print(c.count(7))

# list sort
c.sort(reverse = True)
print(c)


# multiplication operator
print(c*4)
print(len(c))

# Accessing Value
print(c[5])
print(c[-1])
print(c[2:5])