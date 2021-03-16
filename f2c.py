temp = input("Input the  temperature you like to convert. : ")
degree = int(temp[:-1])
degree = 25
C = int(round((degree - 32) * 5 / 9))

print("The temperature is", C, "degrees.")