#constantes 
MINIMO_APROBADO = 6.0
TOTAL_ESTUDIANTES = 15

#listas
nombres = []
notas = []

#datos
for i in range(TOTAL_ESTUDIANTES):
    nombre = input(f"nombre del estudiante {i+1}:")
    while True:
        nota = float(input(f"nota de {nombre}:"))
        if 0.0 <= nota <= 10.0:
            break
        else: 
            print("nota invalida, ingresa un valor entre 0.0 y 10.0")

#calcular promedio
promedio = sum(notas) / TOTAL_ESTUDIANTES
print(promedio)

#asignar letra
for i in range(TOTAL_ESTUDIANTES):
    nombre = []
    nota = 0  # o usar el valor real de la nota

    estado = "aprobado" if nota >= 6.0 else "reprobado"

    if nota >= 9.0:
        letra = "A"
    elif nota >= 8.0:
        letra = "B"
    elif nota >= 7.0:
        letra = "C"
    elif nota >= 6.0:
        letra = "D"
    else:
        letra = "F"

print(f"{nombre} ({nota:.1f}) = {estado} ({letra})")


aprobados = 0
reprobados = 0
for nota in notas:
        if nota >= MINIMO_APROBADO:
            aprobado += 1
        else:
            reprobados += 1

print(f"aprobados: {aprobados}")
print(f"reprobados {reprobados}")

print("\n* reporte final* ")
print("alumno\tnota\testado\tletra")
for i in range(TOTAL_ESTUDIANTES):
    notas = []
    nombre = []

    #aprobado/reprobado
    if nota >= MINIMO_APROBADO:
        estado ="aprobado"
else:
        estado = "reprobado"

#asigar letra

if nota >= 9.0:
    letra = "A"
elif nota >= 8.0:
    letra = "b"
elif nota >= 7.0:
    letra = "c"
elif nota >= 6.0:
    letra = "d"
else:
    letra ="f"
    # fila
    print(f"{nombre}\t{nota:.1f}\t {estado}\t{letra}")

    #mostrar
    print(f"\npromedio del grupo: {promedio:.2f}")
    print(F"aprobados: {aprobados} - reprobados: {reprobados}")

    #inicia con el primer estudiante
    mejor_nota = []
    peor_nota = []
    mejor_nombre = []
    peor_nombre = []

    #segundo estudiante
    for i in range(1, TOTAL_ESTUDIANTES):
        nota = []
        nombre = []

        if nota > mejor_nota:
            mejor_nota = nota 
            mejor_nombre = nombre

            if nota < peor_nota:
                peor_nota = nota
                peor_nombre = nombre

                print(f"mejor calificacion: {mejor_nombre } con {mejor_nota:.1f} ")
                print(f"peor calificacion: {peor_nombre} con {peor_nota:.1f}")

                porcentaje_aprobados = (aprobados / TOTAL_ESTUDIANTES) * 100
                print(f"porcentaje de aprobacion: {porcentaje_aprobados:.1f}%")
