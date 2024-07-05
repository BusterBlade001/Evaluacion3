import csv
import os
import random

# Definición de la lista de equipos
equipos = [
    "Los Genios de la garrafa",
    "Los Compiladores Despiertos",
    "Código Borracho",
    "Los programadores perezosos",
    "Ctrl+Alt+Derrota"
]

# Función para limpiar la pantalla (depende del sistema operativo)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para generar un ID aleatorio de 6 dígitos
def generar_id():
    return random.randint(100000, 999999)

# Función para validar la edad ingresada
def validar_edad(edad):
    try:
        edad = int(edad)
        return edad > 0
    except ValueError:
        return False

# Función para registrar un consumo de café
def registrar_consumo(consumos):
    clear_screen()
    print("~~~ Registrar Consumo ~~~")
    id_consumo = generar_id()
    jugador = input("Nombre del jugador: ")
    edad = input("Edad del jugador: ")
    while not validar_edad(edad):
        print("La edad debe ser un número mayor a cero.")
        edad = input("Edad del jugador: ")
    edad = int(edad)
    equipo = input("Equipo al que pertenece: ")
    viernes = int(input("Tazas consumidas el viernes: "))
    sabado = int(input("Tazas consumidas el sábado: "))
    domingo = int(input("Tazas consumidas el domingo: "))
    
    # Validar que el total de tazas sea al menos 3
    total_tazas = viernes + sabado + domingo
    if total_tazas < 3:
        print("Error: Debe consumir al menos 3 tazas en total durante los 3 días.")
        input("Presione Enter para continuar...")
        return
    
    consumos.append([id_consumo, jugador, edad, equipo, viernes, sabado, domingo])
    print("Consumo registrado exitosamente.")
    input("Presione Enter para continuar...")

# Función para listar todos los consumos
def listar_consumos(consumos):
    clear_screen()
    print("~~~ Listar Consumos ~~~")
    if not consumos:
        print("No hay consumos registrados.")
    else:
        print("ID consumo\tJugador\t\tEdad\tEquipo\t\tViernes\tSábado\tDomingo")
        for consumo in consumos:
            print(f"{consumo[0]}\t\t{consumo[1]}\t\t{consumo[2]}\t{consumo[3]}\t\t{consumo[4]}\t{consumo[5]}\t{consumo[6]}")
    input("Presione Enter para continuar...")

# Función para imprimir hoja de consumo en CSV
def imprimir_hoja_consumo(consumos):
    clear_screen()
    print("~~~ Imprimir Hoja de Consumo ~~~")
    print("Equipos disponibles:")
    for index, equipo in enumerate(equipos, start=1):
        print(f"{index}. {equipo}")
    try:
        opcion = int(input("Seleccione el número de equipo para imprimir su hoja de consumo: "))
        equipo_seleccionado = equipos[opcion - 1]
        
        filename = f"hoja_consumo_{equipo_seleccionado}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID consumo", "Jugador", "Edad", "Equipo", "Viernes", "Sábado", "Domingo"])
            for consumo in consumos:
                if consumo[3] == equipo_seleccionado:
                    writer.writerow(consumo)
        
        print(f"Se ha generado el archivo {filename} correctamente.")
    except (IndexError, ValueError):
        print("Opción inválida.")
    input("Presione Enter para continuar...")

# Función para buscar un consumo por ID
def buscar_consumo(consumos):
    clear_screen()
    print("~~~ Buscar Consumo por ID ~~~")
    id_buscar = input("Ingrese el ID del consumo a buscar: ")
    encontrado = False
    for consumo in consumos:
        if str(consumo[0]) == id_buscar:
            encontrado = True
            print("ID consumo\tJugador\t\tEdad\tEquipo\t\tViernes\tSábado\tDomingo")
            print(f"{consumo[0]}\t\t{consumo[1]}\t\t{consumo[2]}\t{consumo[3]}\t\t{consumo[4]}\t{consumo[5]}\t{consumo[6]}")
            break
    if not encontrado:
        print("No se encontró un consumo con ese ID.")
    input("Presione Enter para continuar...")

# Función principal del programa
def main():
    consumos = []
    while True:
        clear_screen()
        print("~~~ Bienvenido al sistema de registro de consumos de café ~~~")
        print("1. Registrar consumo")
        print("2. Listar todos los consumos")
        print("3. Imprimir hoja de consumo")
        print("4. Buscar un consumo por ID")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_consumo(consumos)
        elif opcion == '2':
            listar_consumos(consumos)
        elif opcion == '3':
            imprimir_hoja_consumo(consumos)
        elif opcion == '4':
            buscar_consumo(consumos)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
    
    print("Gracias por utilizar el sistema de registro de consumos.")

if __name__ == "__main__":
    main()
