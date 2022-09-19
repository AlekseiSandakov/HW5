class VehicleBase:
    def __init__(self, vehicle_weight):
        self.vehicle_weight = vehicle_weight


class Ship(VehicleBase):
    def __init__(self, vehicle_weight, max_weight):
        super().__init__(vehicle_weight)
        self.max_weight = max_weight

    def set_sail(self):
        print('Поднять паруса!!!')


class Plane(VehicleBase):
    def __init__(self, vehicle_weight, cargo=0):
        super().__init__(vehicle_weight)
        self.cargo = cargo

    def add_cargo(self, additional_cargo=0):
        self.cargo += additional_cargo
        return self.cargo


def main():
    ship = Ship(100, 500)
    print(ship)
    ship.set_sail()

    plane = Plane(200, 500)
    print(plane)
    print(plane.add_cargo(100))
    print(plane.add_cargo(200))


if __name__ == '__main__':
    main()
