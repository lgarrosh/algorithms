

if __name__ == '__main__':
    testTuple = '()', '()', 9, 9
    testList = [1, 1]
    print(testTuple, type(testTuple), id(testTuple))
    testTuple += tuple(testList)
    print(testList, type(testList), id(testList))
    print(testTuple, type(testTuple), id(testTuple))
