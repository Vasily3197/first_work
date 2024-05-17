# Задача 1

# print("Система подсчёта штрафов в Германии (Для населённых пунктов)")

# def fines(*args):
    
#     if speeding in range(1,10):
#         return args[0]

#     elif speeding in range(11, 15):
#         return args[1]

#     elif speeding in range(16, 20):
#         return args[2]  
    
#     elif speeding in range(21, 25):
#         return args[3]
    
#     elif speeding in range(26, 30):
#         return args[4]
    
#     elif speeding in range(31, 40):
#         return args[5]

#     elif speeding in range(41,50):
#         return args[6] 

#     elif speeding in range(51,60):
#         return args[7]

#     elif speeding in range(61,70):
#         return args[8]
    
#     elif speeding > 70:
#         return args[9]
    
#     else:
#         print("Незначительное превышение")
#         return 0

# speeding = (int(input("\nВведите скорость машины: "))) - 50

# result = fines(30, 50, 70, 115, 180, 260, 400, 560, 700, 800)

# print("Штраф - {} евро".format(result))


# Задача 2

print("Система расчёта штрафов для РФ")

import random

def fines(*args):
    
    if speeding in range(20, 40):
        return args[0]

    elif speeding in range(40, 60):
        return args[1]

    elif speeding in range(60, 80):
        return args[2]  
    
    elif speeding > 80:
        return args[3]
    
    else:
        print("Незначительное превышение")
        return 0
    
def inspcam():

    if inspector_or_camera == 0:
        return "инспектором"
    else:
        return "камерой"

speeding = (int(input("\nВведите скорость машины: "))) - 60

inspector_or_camera = random.randint(0, 1)


result_fines = fines(500, 1000, 2000, 5000)
result_inspcam = inspcam()

if speeding >= 60 and inspector_or_camera == 0:
    print("Лишение водительского удостверения")

else:    
    print("Штраф в {} рублей выписан {}".format(result_fines, result_inspcam))


   
   


