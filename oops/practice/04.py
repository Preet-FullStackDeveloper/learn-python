# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class Vector2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show2d(self):
        print(f'Vector2D({self.i}, {self.j})')

class Vector3D(Vector2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show3d(self):
        print(f'Vector3D({self.i}, {self.j}, {self.k})')

# Example usage
v2d = Vector2D(1, 2)
v2d.show2d()
v3d = Vector3D(4, 5, 3)
v3d.show3d()
v3d.show2d()
