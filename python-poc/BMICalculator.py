def calculateBMI(body_hight, body_weight):
    return body_weight/(pow(body_hight,2))

weight = float(input('Enter weight in Kgs : '))
height = float(input('Enter hight in meters : '))
print(calculateBMI(height,weight))