import csv
def leer_csv(ruta):
    datos=[]
    with open(ruta, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            datos.append(
                (
                    row['user'],
                    row['password'],
                    row['resultado']
                )
            )
    return datos