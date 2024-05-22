# import sys
# import json

# def main():
#     # Obtener los parámetros pasados al script
#     parametros = sys.argv[1:]

#     # Crear un diccionario con los parámetros
#     data = {
#         "parametros_recibidos: ": parametros
#     }

#     # Imprimir el diccionario como JSON en la salida estándar
#     # print(json.dumps(data))
#     print("parametros_recibidos: ")
#     if len(sys.argv) > 1:
#         print(f"Argumentos recibidos: {sys.argv[1:]}")

# if __name__ == "__main__":
#     main()
import sys

def generar_archivo_txt(nombre_archivo, parametros):
    with open(nombre_archivo, 'w') as archivo:
        for parametro in parametros:
            archivo.write(parametro + '\n')

if __name__ == "__main__":
    # Nombre del archivo de texto
    nombre_archivo = "archivo_generado.txt"

    # Obtener los parámetros de la línea de comandos
    parametros = sys.argv[1:]

    # Verificar si se proporcionaron parámetros
    if not parametros:
        print("Error: Debes proporcionar al menos un parámetro.")
        sys.exit(1)

    # Generar el archivo de texto con los parámetros
    generar_archivo_txt(nombre_archivo, parametros)

    print(f"Archivo '{nombre_archivo}' generado exitosamente.")
