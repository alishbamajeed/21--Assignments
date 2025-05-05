class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        return self.engine.start()

# Usage
eng = Engine()
car = Car(eng)
print(car.start_car())