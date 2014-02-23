
def enum(**enums):
    return type('Enum', (), enums)

# Movement Directions
Directions = enum(RIGHT=1, LEFT=2, UP=3, DOWN=4)
