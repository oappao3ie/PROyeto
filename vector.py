
def lerp(a, b, x):
    return a + x * (b-a)

class Vector3():
    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):

        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def lerp(self, other, w):

        return Vector3(lerp(self.x, other.x, w), lerp(self.y, other.y, w), lerp(self.z, other.z, w))