class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return self.factor * number

# Usage
m = Multiplier(3)
print("Is callable?", callable(m))
print("Result:", m(10))

