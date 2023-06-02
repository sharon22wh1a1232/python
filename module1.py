def area_square(s):
    area=pow(s,2)
    return area

def perimeter_square(s):
    perimeter=4*s
    return perimeter
s=int(input("enter side"))
print("area of square",area_square(s))
print("perimeter of square",perimeter_square(s))
