
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = (dx**2 + dy**2)**0.5
        return distance

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# Пример использования
point1 = Point(1, 2)
point2 = Point(4, 6)

# Получение координат
print("Координаты точки 1:", point1.get_coordinates())

# Установка новых координат
point1.set_coordinates(3, 5)
print("Новые координаты точки 1:", point1.get_coordinates())

# Расстояние между точками
distance = point1.distance_to(point2)
print("Расстояние между точками 1 и 2:", distance)

# Перемещение точки
point1.move(2, -1)
print("Новые координаты точки 1 после перемещения:", point1.get_coordinates())
