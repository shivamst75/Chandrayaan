class Chandrayaan3Controller:
    def __init__(self):
        # Initialize spacecraft's current galactic coordinates
        self.x = 0  # Initial x-coordinate (east/west)
        self.y = 0  # Initial y-coordinate (north/south)
        self.z = 0  # Initial z-coordinate (above/below galactic plane)

    def move_east(self, distance):
        self.x += distance

    def move_west(self, distance):
        self.x -= distance

    def move_north(self, distance):
        self.y += distance

    def move_south(self, distance):
        self.y -= distance

    def move_up(self, distance):
        self.z += distance

    def move_down(self, distance):
        self.z -= distance

    def get_coordinates(self):
        return f"Current Coordinates: x={self.x}, y={self.y}, z={self.z}"

# Test Cases
def test_chandrayaan3_controller():
    # Initialize the controller
    controller = Chandrayaan3Controller()

    # Test initial coordinates
    assert controller.get_coordinates() == "Current Coordinates: x=0, y=0, z=0"

    # Test moving east
    controller.move_east(1000)
    assert controller.get_coordinates() == "Current Coordinates: x=1000, y=0, z=0"

    # Test moving up
    controller.move_up(500)
    assert controller.get_coordinates() == "Current Coordinates: x=1000, y=0, z=500"

    # Test moving south
    controller.move_south(200)
    assert controller.get_coordinates() == "Current Coordinates: x=1000, y=-200, z=500"

    # Test moving west
    controller.move_west(300)
    assert controller.get_coordinates() == "Current Coordinates: x=700, y=-200, z=500"

    # Test moving down
    controller.move_down(100)
    assert controller.get_coordinates() == "Current Coordinates: x=700, y=-200, z=400"

    print("All test cases passed.")

if __name__ == "__main__":
    test_chandrayaan3_controller()
