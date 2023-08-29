class Chandrayaan3Controller:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move(self, command):
        if command == 'f':
            self._move_forward()
        elif command == 'b':
            self._move_backward()
        elif command == 'l':
            self._turn_left()
        elif command == 'r':
            self._turn_right()
        elif command == 'u':
            self._turn_up()
        elif command == 'd':
            self._turn_down()

    def _move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1
        elif self.direction == 'Up':
            self.z += 1
        elif self.direction == 'Down':
            self.z -= 1

    def _move_backward(self):
        # Move backward is essentially the opposite of moving forward
        if self.direction == 'N':
            self.y -= 1
        elif self.direction == 'S':
            self.y += 1
        elif self.direction == 'E':
            self.x -= 1
        elif self.direction == 'W':
            self.x += 1
        elif self.direction == 'Up':
            self.z -= 1
        elif self.direction == 'Down':
            self.z += 1

    def _turn_left(self):
        # Rotate 90 degrees counter-clockwise
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def _turn_right(self):
        # Rotate 90 degrees clockwise
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def _turn_up(self):
        # Rotate 90 degrees upwards
        if self.direction == 'N':
            self.direction = 'Up'
        elif self.direction == 'S':
            self.direction = 'Down'
        elif self.direction == 'Up':
            self.direction = 'S'
        elif self.direction == 'Down':
            self.direction = 'N'

    def _turn_down(self):
        # Rotate 90 degrees downwards
        if self.direction == 'N':
            self.direction = 'Down'
        elif self.direction == 'S':
            self.direction = 'Up'
        elif self.direction == 'Up':
            self.direction = 'N'
        elif self.direction == 'Down':
            self.direction = 'S'

    def get_coordinates(self):
        return f"Current Coordinates: x={self.x}, y={self.y}, z={self.z}, Direction={self.direction}"

def process_commands(initial_x, initial_y, initial_z, initial_direction, commands):
    controller = Chandrayaan3Controller(initial_x, initial_y, initial_z, initial_direction)
    
    for command in commands:
        controller.move(command)

    return controller.get_coordinates()

# Example usage:
if __name__ == "__main__":
    initial_x = 0
    initial_y = 0
    initial_z = 0
    initial_direction = 'N'
    commands = ['f', 'r', 'f', 'u', 'l', 'b']

    final_coordinates = process_commands(initial_x, initial_y, initial_z, initial_direction, commands)
    print(final_coordinates)  # Output: "Current Coordinates: x=1, y=1, z=1, Direction=W"
