import math


class Point:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    @staticmethod
    def Calc_Distance(p1, p2):
        a = abs(p1.x - p2.x)
        b = abs(p1.y - p2.y)
        return round(math.sqrt(a*a + b*b), 3)


class Box:

    def __init__(self, x, y, z, v):
        self.UpperLeft = x
        self.UpperRight = y
        self.BottomLeft = z
        self.BottomRight = v
        self.Width = round(Point.Calc_Distance(x, y))
        self.Height = round(Point.Calc_Distance(x, z))

    #TODO
    def Get_Width():
        pass
    #TODO
    def Get_Height():
        pass
    

    def CalculatePerimeter(self, Width, Height):
        return (2 * Width) + (2 * Height)

    def CalculateArea(self, Width, Height):
        return (Width * Height)
    #TODO
    def show_info(self,Width,Height,CalculatePerimeter):
        pass
        #return f'Box: {self.Width}, {self.Height}\nPerimeter: {self.CalculatePerimeter(self.Width,self.Height)}\nArea: {self.CalculateArea(self.Width,self.Height)}'


if __name__ == '__main__':

    boxes = []
    input_string = input()

    while not input_string == 'end':
        points_list = input_string.split(' | ')
        points_object_list = []
        for point in points_list:
            point = point.split(":")
            points_object_list.append(Point(point[0], point[1]))

        box = Box(x=points_object_list[0], y=points_object_list[1],
                  z=points_object_list[2], v=points_object_list[3])
        boxes.append(box)
        input_string = input()

    for box in boxes:
        print(f'Box: {box.Width}, {box.Height}')
        print(f'Perimeter: {box.CalculatePerimeter(box.Width,box.Height)}')
        print(f'Area: {box.CalculateArea(box.Width,box.Height)}')

        #TODO
        #print(box.show_info)
