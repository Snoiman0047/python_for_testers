def replace(_list, _index1, _index2):
    """
    Exchanges list entries in submitted indexes
    :param _list:
    :param _index1:
    :param _index2:
    :return:
    """
    value = _list[_index1]
    _list[_index1] = _list[_index2]
    _list[_index2] = value

countries = ['Israel', 'Germany', 'Austria', 'Switzerland', 'France', 'United Kingdom', 'Slovakia', 'Hungary']


print('first 3 countries:', countries[:3])

replace(countries, 0, 1)
print('list after replacing indexes:', countries)

countries.reverse()
print('list after reversing:', countries)

countries.sort()
print('list after ABC sorting:', countries)

last_country_index = len(countries) - 1
countries.pop(last_country_index)
print('list after popping:', countries)

countries.remove('Slovakia')
print('list after removing:', countries)

countries.insert(int(len(countries) / 2), "Russia")
print('list after inserting value:', countries)
