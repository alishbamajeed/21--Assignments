class A:
    def show(self):
        print("A.show()")

class B(A):
    def show(self):
        print("B.show()")

class C(A):
    def show(self):
        print("C.show()")

class D(B, C):
    pass

# Usage
d = D()
d.show()  # Will follow MRO (B -> C -> A)
print("MRO:", D.__mro__)
