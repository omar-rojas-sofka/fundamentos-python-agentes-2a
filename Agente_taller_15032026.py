##Taller Agente
### Omar Eduardo Rojas
### 15/03/2026

from datetime import date
import datetime
from decimal import DivisionByZero


### FUNCIONES
## operacion(para la calculadora)
def operacion(num1: int, num2: int, signo: str):
    if signo == '+':
        resultado = num1 + num2
    elif signo == '-':
        resultado = num1 - num2
    elif signo == '*':
        resultado = num1 * num2
    elif signo =='/':
        try:
            resultado = num1 / num2
        except ZeroDivisionError as e:
            # resultado = "Error!! No se puede dividir por cero(0)"
            resultado=f"Se ha producido una excepción: {e}"
        return resultado
    return resultado

## contarPalabras para devolver consonantes y vocales
def contarPalabras(palabra: str):
    numVocales: int = 0 
    numConsonantes: int = 0
    
    for l in palabra:
        if l in "aeiou":
            numVocales += 1
        elif l in "bcdfghjklmnpqrstvwxyzñ":
            numConsonantes += 1
    # Devolvemos ambos valores
    return numVocales, numConsonantes

## fechaActual para validar la fecha de acuerdo al rol
def fechaActual(rol: str):
    if rol == "invitado":
        raise PermissionError("Privilegios insuficientes AAAAAA.")
    return f"La fecha actual es {date.today()}"

### gestionar la busqueda del historial
def gestionar_historial(memoria: list, opcion: str, palabra: str = ""):
    if not memoria:
        return "El historial está vacío."
    if opcion == "1":
        return memoria
        # for log in memoria:
        #     return f"[{log['timestamp']}] {log['rol']} -> {log['cmd']}: {log['descripcion']}"
    elif opcion == "2":
        memoria.clear() # Modifica la lista original por referencia
        return "Historial borrado exitosamente."
    elif opcion == "3":
        encontrados = [log for log in memoria if palabra in log['descripcion'].lower() or palabra in log['cmd']]
        if encontrados:
            for item in encontrados:
                return f"[{item['timestamp']}] Coincidencia: {item['descripcion']}"
        else:
            return f"No se encontraron registros con: {palabra}"

def crear_log(log: dict,cmd: str, rol: str, mensaje: str):
    log={"timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
         "cmd": cmd,
         "rol": rol,
         "descripcion": mensaje
         } 
    return log

def validar_usuario(user: str, password: str, perfiles: list):
    if user in perfiles and perfiles[user]["password"] == password:
        return True
    else:
        return False
    
def obtener_usuario(user: str, password: str, perfiles: list):
    if user in perfiles and perfiles[user]["password"] == password:
        return user, perfiles[user_i]["perfil"]
    

# Primero definimos los perfiles por separado
perfil_invitado = {"perfil": "invitado", "password": "gu" }
perfil_admin    = {"perfil": "administrador", "password": "ad" }
historial_chat=[]
# Luego los guardamos en un diccionario
perfiles= {
    "invitado": perfil_invitado,
    "administrador":    perfil_admin
}

#Voy a agrtegar un header para que no se tan plano la comunicación
print("**************************************** AUTH_BOT **********************")

#variables para validar
num_attemps = 0
total_attemps = 3
current_profile = ""
current_user = ""
is_on_session = False
user_input = ""

#ciclo para autenticar
while num_attemps < 3:
    user_i = input("USUARIO: ").lower()
    pass_i = input("CONTRAEÑA: ")
    user_input = user_i
    if(validar_usuario(user_i,pass_i,perfiles)):
        is_on_session = True
        current_user , current_profile = obtener_usuario(user_i,pass_i,perfiles)
        # aca voy a usar lo visto en la primera sesion con el print format
        #print("Tu nombre es: {}, mucho gusto. Naciste en {} y tu eddad es {}".format(nombre_persona,annio, edad) )
        print("Bienvenido {} tu rol es {}".format(current_user,current_profile))
        break
    else:
        num_attemps += 1        
        if num_attemps > 4:
            missing_attemps = total_attemps - num_attemps
            print("Usuario y/o contraseña incorrectos")
            print("Solo le quedan {} intentos".format(missing_attemps))
if is_on_session == False:
    print("Ha bloqueado al usuario {} se cerrara el agente".format(user_input))
    exit()  

print("**************************************** BOT  Opciones:**********************")
print("""1. Contar:   Cuenta las vocales y consonantes de una palabra(ejemplo: Omar  Total vocales(2) Total consonantes(2) Total letras (4))
         2. Fecha Actual: Si el usuario logueado tiene rol admbnistrador muestra la fecha actual
         3. Ping:  Mostrara un texto "pong"
         4. Calculadora basica: Operaciones basicas(Suma, Resta, Producto o Division)
         5. Salir: Sale del agente
      """)

mensaje=""
is_on_session = True

datos_log = {}

while is_on_session:
    comando = input("Bot> ").lower()
    if comando == "1":
        palabra = input("Digita la palabra que deseas contar: ").lower()
        num_v, num_c = contarPalabras(palabra)
        mensaje ="La palabra {} tiene {} vocales y {} consonantes. En total {} tiene {} letras".format(palabra,num_v,num_c,palabra, num_v+num_c)
        print("tyt")
        historial_chat.append(crear_log(datos_log, comando,current_profile, mensaje))
        print(historial_chat)
        print("aca")
        print(mensaje)
    elif comando == "2":        
        try:
            mensaje = fechaActual(current_profile)
            print("tyt")
            historial_chat.append(crear_log(datos_log, comando,current_profile, mensaje))
            print(historial_chat)
            print("aca")
            print(mensaje)
        except PermissionError as e:
            print(f"Error detectado: {e}")
            
    elif comando == "3":
        mensaje="pong"
        historial_chat.append(crear_log(datos_log, comando,current_profile, mensaje))
        print(mensaje)
    elif comando == "4":
            entrada = input("Digite primer número: ").replace(",", ".")
            num_1 = float(entrada)

            entrada = input("Digite segundo numero: ").replace(",", ".")
            num_2 = float(entrada)

            operador = input("+ para Suma; - para Resta ; * para producto o / para Divsvion): ")
            resultado = operacion(num_1,num_2, operador)
            mensaje = f"El resultado de {num_1} {operador} {num_2} es {resultado}"
            historial_chat.append(crear_log(datos_log, comando,current_profile, mensaje))
            print(mensaje)
    elif comando == "5":
        is_on_session = False
    
    else:
        mensaje = "El comando {} no es valido o nbo eres administrador".format(comando)
        print(mensaje)
    opcionBusqueda = input("Bot> Deseas buscar algo de la conversacion S/N?").lower()
    
    busqueda = True
    contadorCoincidencias = 0
    while busqueda:
        if opcionBusqueda == "s":
            print("""1. historial all: Te muestra todo el historial del chat
                     2. historial clear: Borra todo el historial del chat
                     3. busqueda en historial:  Busca una palabra en todo el historial del chat
                     4. Salir: Sale de la busqueda
            """)
            comandoS = input("Bot-Search> ").lower()
            if comandoS == "1":
                print(gestionar_historial(historial_chat,comandoS))
            elif comandoS == "2":
                estaSeguro = input("Esta seguro s/n?. Si seleciona s ya no podra ver o buscar nada en el historial. ").lower()
                if  estaSeguro == "s":
                    print(gestionar_historial(historial_chat,comandoS))
                elif estaSeguro == "n":
                    print("historial de chat no se eliminara.")
                else: 
                     mensaje = "{} no es valido, debes digira s o n".format(estaSeguro)
            elif comandoS == "3":
                palabraS = input("Digita la palabra que deseas buscar en el historial del chat: ").lower()                
                print(gestionar_historial(historial_chat,comandoS,palabraS))
            else:
                busqueda = False
        elif opcionBusqueda == "n":
            busqueda = False
        else:
            mensaje = f"{opcionBusqueda} no es valido, debes digira s o n"
            busqueda = False


    # historial  all
    # historial clear
    # historial   Digite una palabra
    # Total coincidencias: 2
    # {lkjlk}
    # {hjkhjkh}

    # Si no existe:
    # Total de concidencias :0
    # No se encontraron registros

