from Car import Car


def test_car_brake():
    car = Car(50)
    car.brake()
    assert car.speed == 45

def test_car_brake():
    car = Car(50)
    car.accelerate()
    assert car.speed == 50