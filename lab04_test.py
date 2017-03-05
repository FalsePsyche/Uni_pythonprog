import lab04

print(lab04.reverse_iter([1, 2, 3, 4]))

print(lab04.reverse_recursive([1, 2, 3, 4]))

print(lab04.map(lambda x: x*x, [1, 2, 3]))

print(lab04.filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))

print(lab04.reduce(lambda x, y: x + y, [1, 2, 3, 4]))

text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
print(text)

table = lab04.build_successors_table(text)
print(sorted(table)) # [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']

print(table['to']) # ['investigate', 'eat']

print(table['pie']) # ['.']

print(table['.']) # ['We']

shakestokens = lab04.shakespeare_tokens()
shakestable = lab04.build_successors_table(shakestokens)
trumptokens = lab04.trump_tokens()
trumptable = lab04.build_successors_table(trumptokens)

print("Shakespeare random tweet: {0}".format(lab04.random_tweet(shakestable)))
print("Trump random tweet: {0}".format(lab04.random_tweet(trumptable)))