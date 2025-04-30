from src.procesador import Analizador

def main():
    archivo = "data/sri_ventas_2024.csv"
    analizador = Analizador(archivo)

    # Ventas totales por provincia
    print("Ventas totales por provincia:")
    resumen = analizador.ventas_totales_por_provincia()
    for prov, total in resumen.items():
        print(f"\t{prov}: ${total:.2f}")

    # Consultar ventas de una provincia específica
    print("\nVentas para una provincia específica")
    provincia = input("\tIngrese el nombre de una provincia: ")
    try:
        ventas = analizador.ventas_por_provincia(provincia)
        print(f"\tVentas de {provincia}: ${ventas:,.2f}")
    except KeyError as e:
        print(e)

    # Exportaciones totales por mes
    print("\nExportaciones totales por mes:")
    exportaciones = analizador.exportaciones_totales_por_mes()
    for mes, total in exportaciones.items():
        print(f"\t{mes}: ${total:.2f}")

    # Provincia con mayor volumen de importaciones
    print("\nProvincia con mayor volumen de importaciones:")
    provincia_importadora, total_importaciones = analizador.provincia_con_mayor_importacion()
    print(f"\tProvincia: {provincia_importadora} con ${total_importaciones:,.2f} en importaciones")

if __name__ == "__main__":
    main()
