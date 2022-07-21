from itertools import chain

nested_list = [
    ['a','b','c'],
    ['d','e','f','h',False],
    [1,2,None, [3,5,[8,9,10]]]
]

#iterator для любого уровня вложенности:
class FlatIterator(list):

    def __init__(self,some_list):
        self.list = some_list

    def __iter__(self):
        self.cursor = iter(nested_list)
        return self

    def __next__(self):
        next_cursor = next(self.cursor)
        if isinstance (next_cursor,list):
            self.cursor = chain(next_cursor,self.cursor)
            return next(self.cursor)
        return next_cursor

for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

#generator для любого уровня вложенности:


def flat_generator(l):
    try:
        return flat_generator(l[0]) + (flat_generator(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]
    except IndexError:
        return []

for item in flat_generator(nested_list):
    print(item)