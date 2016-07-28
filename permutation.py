from itertools import permutations

content = [
    {"group": 123, "content": "a"},
    {"group": 0, "content": "+"},
    {"group": 445, "content": "b"},
    {"group": 0, "content": "="},
    {"group": 322, "content": "c"}]

change_list = []
unchange_list = []

for item in content:
    if item['group'] == 0 :
        unchange_list.append(item)
    else:
        change_list.append(item)


list = []
for i in permutations(change_list):
    if i[0]['group'] + i[1]['group'] == i[2]['group']:
        result = '%s%s%s%s%s' % (i[0]['content'],unchange_list[0]['content'],i[1]['content'],unchange_list[1]['content'],i[2]['content'])
        list.append(result)


print list