
family = {'shlomo': '000-000-0000', 'miriam': '111-111-1111', 'sima': '222-222-2222'}

print('family dictionary:', family)

print('persons in family:', len(family))

family['ester'] = '333-333-3333'              # first way
family.update({'shimon': '444-444-4444'})     # second way
print('family dictionary after adding and updating:', family)

