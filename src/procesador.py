import csv
from collections import defaultdict

class Analizador:
    def __init__(self, archivo_csv):
        """Inicializa la clase con la ruta al archivo CSV"""
        self.archivo_csv = archivo_csv
        self.datos = self._cargar_datos()

    def _cargar_datos(self):
        """Carga los datos del archivo CSV en una lista de diccionarios"""
        with open(self.archivo_csv, mode='r', encoding='latin-1') as archivo:  # Cambié 'utf-8' por 'latin-1'
            return [fila for fila in csv.DictReader(archivo)]

    def ventas_totales_por_provincia(self):
        """Retorna un diccionario con el total de ventas por provincia"""
        ventas_por_provincia = defaultdict(float)  # Usamos defaultdict para inicializar con 0.0 automáticamente
        for fila in self.datos:
            provincia = fila['PROVINCIA']
            if provincia == "ND":
                continue 
            ventas_por_provincia[provincia] += float(fila['TOTAL_VENTAS'])
        return dict(ventas_por_provincia)  # Convertimos de vuelta a un diccionario normal

    def ventas_por_provincia(self, nombre):
        """Retorna el total de ventas de una provincia determinada"""
        ventas_por_provincia = self.ventas_totales_por_provincia()
        nombre_normalizado = nombre.strip().upper()  # Convertir nombre a mayúsculas
        try:
            return ventas_por_provincia[nombre_normalizado]
        except KeyError:
            raise KeyError(f"La provincia '{nombre}' no se encuentra en los datos.")

    def exportaciones_totales_por_mes(self):
        """Retorna un diccionario con el total de exportaciones agrupadas por mes."""
        exportaciones_por_mes = defaultdict(float)
        for fila in self.datos:
            mes = fila['MES']
            exportaciones_por_mes[mes] += float(fila['EXPORTACIONES'] or 0.0)
        return dict(exportaciones_por_mes)

    def provincia_con_mayor_importacion(self):
        """Retorna la provincia con el mayor volumen de importaciones."""
        importaciones_por_provincia = defaultdict(float)
        for fila in self.datos:
            provincia = fila['PROVINCIA']
            if provincia == "ND":
                continue
            importaciones_por_provincia[provincia] += float(fila['IMPORTACIONES'] or 0.0)

        if not importaciones_por_provincia:
            raise ValueError("No hay datos de importaciones disponibles.")

        # Buscar la provincia con la mayor importación
        provincia_max = max(importaciones_por_provincia, key=importaciones_por_provincia.get)
        return provincia_max, importaciones_por_provincia[provincia_max]
    
    def porcentaje_ventas_tarifa_cero(self):
        """Calcula el promedio del porcentaje de ventas con tarifa 0% por provincia"""
        acumulados = {}
        conteos = {}

        for fila in self.datos:
            provincia = fila['PROVINCIA']
            if provincia == "ND":
                continue

            try:
                tarifa_0 = float(fila['VENTAS_NETAS_TARIFA_0'])
                total_ventas = float(fila['TOTAL_VENTAS'])
                if total_ventas == 0:
                    continue
                porcentaje = (tarifa_0 / total_ventas) * 100

                if provincia in acumulados:
                    acumulados[provincia] += porcentaje
                    conteos[provincia] += 1
                else:
                    acumulados[provincia] = porcentaje
                    conteos[provincia] = 1
            except ValueError:
                continue  # Si algún dato no es numérico

        # Calcular promedio por provincia
        promedios = {}
        for provincia in acumulados:
            promedios[provincia] = acumulados[provincia] / conteos[provincia]
        
        return promedios