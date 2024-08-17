import strobject


class Test:

    int = 0
    float = 1.0
    string = "string"
    tuple = ("Test._tuple.item0", "Test._tuple.item1", "Test._tuple.item2")
    dict = {"Test._dict.key0": 0, "Test._dict.key1": 1, "Test._dict.key1": 2}


class Test:

    def __init__(self):

        self.none = None
        self.bool = True
        self.int = 0
        self.float = 1.0
        self.string = "string"
        self.tuple = ("Test._tuple.item0", "Test._tuple.item1", "Test._tuple.item2")
        self.dict = {"Test._dict.key0": 0, "Test._dict.key1": 1, "Test._dict.key1": 2}

        self.nested = Nested()



class Nested:

    def __init__(self):

        self.int = 0
        self.float = 1.0
        self.string = "nested_string"
        self.tuple = ("Test._tuple.item0", "Test._tuple.item1", "Test._tuple.item2")
        self.dict = {"Test._dict.key0": 0, "Test._dict.key1": 1, "Test._dict.key1": 2}


class Inheritance(Test):

    pass



test0 = Test()


for e in test0.__dict__.keys():

    print(e)


print(strobject.strobject(test0))





    
