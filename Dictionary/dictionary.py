# 사전 (dictionary)
# key - value
# 순서 X

dict1 = {}

dict1[5] = 25
dict1[2] = 4
dict1[3] = 9

print(dict1)
print(dict1[5])

family = {}

family['mom'] = 'grace'
family['dad'] = 'crhis'
family['son'] = 'young'
family['daughter'] = 'key'

#print(family)
#print(family['dad'])

print(family.keys()) # get All keys
print('son' in family) # boolean
print('brother' in family)

family_keys = list(family.keys()) # key -> list
print(family_keys)
print(type(family_keys))

print(family.values()) # get All value

family_values = list(family.values()) # value -> list
print(family_values)
print(type(family_values))

