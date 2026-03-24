##Taller Agente
### Omar Eduardo Rojas
### 15/03/2026

from datetime import date
import datetime



# Primero definimos los perfiles por separado
perfil_invitado = {"perfil": "invitado", "password": "guest_ab!2" }
perfil_admin    = {"perfil": "administrador", "password": "hosts_ab12" }
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
    # valido si el usuario existe y si tiene la misma contraseña que digito
    if user_i in perfiles and perfiles[user_i]["password"] == pass_i:
        is_on_session = True
        current_user = user_i
        current_profile = perfiles[user_i]["perfil"]
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

while is_on_session:
    comando = input("Bot> ").lower()
    if comando == "1":
        palabra = input("Digita la palabra que deseas contar: ").lower()
        num_v = 0
        num_c = 0
        for l in palabra:
            if l in "aeiou":
                num_v += 1
            elif l in "bcdfghjklmnpqrstvwxyzñ":
                num_c += 1
        mensaje ="La palabra {} tiene {} vocales y {} consonantes. En total {} tiene {} letras".format(palabra,num_v,num_c,palabra, num_v+num_c)
        print(mensaje)
        
    elif comando == "2" and current_profile == "administrador":
        hoy=date.today()
        mensaje="La fecha actual es {}".format(hoy)
        print(mensaje)
    elif comando == "3":
        mensaje="pong"
        print(mensaje)
    elif comando == "4":
            entrada = input("Digite primer número: ").replace(",", ".")
            num_1 = float(entrada)

            entrada = input("Digite segundo numero: ").replace(",", ".")
            num_2 = float(entrada)

            operacion = input("+ para Suma; - para Resta ; * para producto o / para Divsvion): ")
                   
            if operacion == "+":
                mensaje= "El resultado de {} {} {} es {} ".format(num_1,operacion,num_2,num_1 + num_2)
                print(mensaje)

            elif operacion == "-":
                mensaje = "El resultado de {} {} {} es {} ".format(num_1,operacion,num_2,num_1 - num_2)
                print(mensaje)
            elif operacion == "*":
                mensaje = "El resultado de {} {} {} es {} ".format(num_1,operacion,num_2,num_1 * num_2)
                print(mensaje)
            elif operacion == "/":
                if num_2 == 0:
                    print("No se puede dividir entre {}".format(num_2))
                else:
                     mensaje = "El resultado de {} {}  {} es {} ".format(num_1,operacion,num_2,num_1 / num_2)
                     print(mensaje)
            else:
                mensaje = "El operador {}' no valido".format(operacion)
                print(mensaje)

    elif comando == "5":
        is_on_session = False
    
    else:
        mensaje = "El comando {} no es valido o nbo eres administrador".format(comando)
        print(mensaje)

    d_log={"timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
           "cmd": comando,
           "rol": current_profile,
           "descripcion": mensaje
           }    
    historial_chat.append(d_log)
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
                if len(historial_chat) <= 0:
                    print("No hay registros en el Log")
                else: 
                    print(historial_chat)
            elif comandoS == "2":
                estaSeguro = input("Esta seguro s/n?. Si seleciona s ya no podra ver o buscar nada en el historial. ").lower()
                if  estaSeguro == "s":
                    historial_chat.clear()
                    print("historial de chat eliminado.")
                elif estaSeguro == "n":
                    print("historial de chat no se eliminara.")
                else: 
                     mensaje = "{} no es valido, debes digira s o n".format(estaSeguro)
            elif comandoS == "3":
                if len(historial_chat) <= 0:
                    print(f"No hay registros en el Log")
                else: 
                    contadorCoincidencias = 0
                    coincidencias =[]
                    palabraS = input("Digita la palabra que deseas buscar en el historial del chat: ").lower()                
                    for d_log in historial_chat:
                        # .count() busca todas las repeticiones dentro del string
                        texto = d_log["descripcion"].lower()
                        busqueda = palabraS.lower()
                        cantidad_en_este_log = texto.count(busqueda)
                        contadorCoincidencias += cantidad_en_este_log
                        if cantidad_en_este_log > 0:
                            coincidencias.append(d_log)
                        else:
                            print(f"No se encontraron coincidencias de {palabraS} intenta de nuevo")            
                    print(f"Total coincidencias de {palabraS} : {contadorCoincidencias}")
                    print(f"En los siguientes chats {coincidencias}")
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

