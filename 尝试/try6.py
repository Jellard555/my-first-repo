#BMI = 体重 / （身高**2）
#weight = float(input("体重 kg :"))
#height = float(input("升高 m :"))
#BMI = weight / (height**2)
#print(f"你的BMI值为:{BMI}")
def calculate_BMI(weight,height):
    BMI = weight / (height**2)
    if BMI <= 18.5:
        cata = "weak"
    elif  BMI <= 25:
        cata = "normal"
    elif  BMI <= 30:
        cata = "fat"
    else:
        cata = "fat fat"
    print(f'ningdBMIzlwei:{cata}')
    return BMI


catagory2 = calculate_BMI(1.6,65)
catagory1 = calculate_BMI(1.8,65)
catagory3 = calculate_BMI(1.7,65)
summary = [catagory1,catagory2,catagory3]
total = sum(summary)
count = len(summary)
average = total/count
print(f"zonpjw:{average}")