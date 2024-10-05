# Escritura de archivo de texto

# crear un archivo llamado 'my_notes.txt' en modo escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Primera nota: Repasar los conceptos de programación.\n")
    file.write("Segunda nota: Leer sobre gamificación en educación.\n")
    file.write("Tercera nota: Preparar la clase sobre parónimos y homófonos.\n")

# Lectura de archivo de texto usando readline()

# Abrimos el archivo 'my_notes.txt' en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Usaremos readline() para leer línea por línea
    line = file.readline()  # Leemos la primera línea
    while line:  # Continuamos leyendo hasta que no haya más líneas
        print(line.strip())  # Imprimimos la línea
        line = file.readline()  # Leemos la siguiente línea

# El archivo se cierra automáticamente gracias al uso de 'with'
