set1={1,2,'b',4}
set2={3,5,1,'a'}

#   union
print(set1.union(set2),'\t\tunion') # Merge
set1.update(set2)       # Merge
print(set1, '\t\tupdate')
set1={1,2,'b',4}

#   intersection
print(set1.intersection(set2),'\t\t\t\t\tintersection')      # Same value
set1.intersection_update(set2)       # Same value
print(set1,'\t\t\t\t\tintersection_update')
set1={1,2,'b',4}

#   symmentric_difference (minus)
print(set1.symmetric_difference(set2),'\t\t\tminus of SQL is called symmmentric_difference')
set1.symmetric_difference_update(set2)
print(set1,'\t\t\tminus of SQL is called symmmentric_difference_update')
set1={1,2,'b',4}

#   difference
print(set1.difference(set2), '\t\t\t\tdifference')
set2.difference_update(set1)
print(set2,'\t\t\t\tdiffrence_update')
set2={3,5,1,'a'}

#   isdisjoint
s={1,2}
s1={3,4}
print(s.isdisjoint(s1),'isdisjoint'.center(80)) # return bool value

# issuperset, issubset
s={1,2,3,4}
s1={3,4}
print(s.issuperset(s1),"issuperset".center(80))
print(s.issubset(s1),"issubset".center(75))


s.add('hello')  # take only one argunment
print(s,'add'.center(40))

s.discard('hello')
print(s,'discard'.center(62))

s.pop()
print(s,'pop'.center(63))

s.clear()
del s

if 3 in s1:
    print('he')
else:
    print('nahi he')