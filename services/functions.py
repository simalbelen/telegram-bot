import string
import random

def generate_pass(text):
    texto = text.split(" ")
    if(len(texto) == 1): #Caso default sin parámetros
        length = 16
    elif(len(texto) == 2):
        length = int(texto[1])
    else:
        return "Error, demasiados parámetros introducidos"

    characters = list(string.ascii_letters + string.digits) #+ "!@#$%^&*()")
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    passw = "".join(password)
    return passw

def roll_dice(text): 
    texto = text.split(" ")
    if(len(texto) == 1): # Caso sin parámetros -> valor default 1d20
        roll = "1d20"
    elif(len(texto) == 2): # Caso con parámetros
        roll = texto[1]
    else:
        return "Error, demasiados parámetros introducidos"

    x = roll.split("d")
    if (len(x)!=2):
        return "Error en el formato"
    try:
        dice_number = int(x[0])
        face_number = int(x[1])
    except:
        return "Error en el formato"
    value = 0
    response = ""
    for i in range(dice_number):
        aux = random.randint(1,face_number)
        value += aux
        response = response + "d{} = {}\n".format(str(i + 1), aux)

    return "{}Total: {}".format(response, value)