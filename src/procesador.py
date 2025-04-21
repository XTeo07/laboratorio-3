import csv

class Analizador:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.datos = []
        self._leer_csv()

    def _leer_csv(self):
        """Lee el archivo CSV y convierte 'TOTAL_VENTAS' a flotante."""
        try:
            # Cambiar la codificación de 'utf-8' a 'ISO-8859-1' o 'latin1'
            with open(self.archivo_csv, newline='', encoding='ISO-8859-1') as csvfile:
                lector = csv.DictReader(csvfile)
                for fila in lector:
                    try:
                        # Convierte TOTAL_VENTAS a flotante
                        fila['TOTAL_VENTAS'] = float(fila['TOTAL_VENTAS'])
                        self.datos.append(fila)
                    except ValueError:
                        # Si ocurre un error al convertir, muestra el error
                        print(f"Error al convertir TOTAL_VENTAS: {fila['TOTAL_VENTAS']}")
        except FileNotFoundError:
            print(f"No se encontró el archivo: {self.archivo_csv}")

    def ventas_totales_por_provincia(self):
        """Devuelve un diccionario con las ventas totales por provincia."""
        ventas_por_provincia = {}
        for fila in self.datos:
            provincia = fila['PROVINCIA']
            ventas = fila['TOTAL_VENTAS']
            # Sumar ventas por provincia
            if provincia in ventas_por_provincia:
                ventas_por_provincia[provincia] += ventas
            else:
                ventas_por_provincia[provincia] = ventas
        
        # Mostrar las ventas por provincia para depuración
        if ventas_por_provincia:
            print("Ventas por provincia (debido a depuración):")
            for provincia, total in ventas_por_provincia.items():
                print(f"{provincia}: ${total:,.2f}")
        else:
            print("No se encontraron ventas para sumar.")
        
        return ventas_por_provincia

    def ventas_por_provincia(self, nombre):
        """Devuelve el total de ventas de una provincia específica."""
        total = 0
        for fila in self.datos:
            if fila['PROVINCIA'].lower() == nombre.lower():
                total += fila['TOTAL_VENTAS']
        
        return total
    

