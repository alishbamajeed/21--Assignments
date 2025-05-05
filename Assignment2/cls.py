class Counter:
  
    count = 0

    def __init__(self):
        
        Counter.count += 1

    @classmethod
    def display_count(cls):
        
        print(f"Total objects created: {cls.count}")

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Display the current object count using the class method
Counter.display_count()  # Output: Total objects created: 3
