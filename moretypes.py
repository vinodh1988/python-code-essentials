one=(1,3,4,3)
two=[32,534,32,35]
three=set(one)
four=set(two)
five={24,531,154,323,325,123,1235,123,1566,2531,111}
six={1:2,3:4,5:7,1:5,3:5,3:9,None:12}
print(type(one))
print(type(two))
print(type(three))
print(type(four))

print(one)
print(two)
print(three)
print(four)
print(five)

print(type(six))
print(six)

print( 12 in one)
print( 4 in one)
print(12 not in one)
print(123 in five )
print(5 in six.keys())
print(six.keys())