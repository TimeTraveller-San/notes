import copy

class a():
    """
    a = b
    any change made in b will be made in a
    a reference b

    a = copy.copy(b)
    any change made in b will not be made in a uptil level 1 (hence shallow)
    a references the 1+ level elements of b

    a = copy.deepcopy(b)
    any change made in b will not be made in b till any level (hence deep)
    a doesnt reference anything related to b, simply copies it
    """
    def __init__(self, a):
        self.a = [1,2,[2,3,4],4]
        self.other_a = self.a
        self.shallowcopy_a = copy.copy(self.a)
        self.deepcopy_a = copy.deepcopy(self.a)
    def change(self):
        self.a[2][0] = 100
        self.a.append(12)
    def print(self):
        print(f"original: {self.a} \nOther: {self.other_a}\
                \nShallow: {self.shallowcopy_a} \nDeep: {self.deepcopy_a}")

if __name__ == "__main__":
    x = a(10)
    x.print()
    x.change()
    x.print()
    x.change()
    x.print()

