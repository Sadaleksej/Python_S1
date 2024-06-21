a = int(input("Enter 1-st side of triangle: "))
b = int(input("Enter 2-nd side of triangle: "))
c = int(input("Enter 3-rd side of triangle: "))

if a >= (b + c) or b >= (a + c) or c >= (b + a):
    print("triangle doesn't exist!")

elif a == b == c:
    print("equilateral triangle!")

elif a == b or a == c or c == b:
    print("isosceles triangle!")
