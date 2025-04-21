from src.procesador import Analizador

def main():
    archivo = "data/sri_ventas_2024.csv"
    analizador = Analizador(archivo)

    # Mostrar ventas totales por provincia
    print("Ventas totales por provincia:")
    resumen = analizador.ventas_totales_por_provincia()
    if resumen:
        for prov, total in resumen.items():
            print(f"\t{prov}: ${total:,.2f}")
    else:
        print("No se pudieron obtener ventas por provincia.")

    # Solicitar el nombre de una provincia y mostrar ventas específicas
    print("\nCompras para una provincia")
    provincia = input("\tIngrese el nombre de una provincia: ")
    ventas = analizador.ventas_por_provincia(provincia)
    
    if ventas > 0:
        print(f"\tVentas de {provincia}: ${ventas:,.2f}")
    else:
        print(f"\tNo se encontraron ventas para la provincia: {provincia}")

if __name__ == "__main__":
    main()


