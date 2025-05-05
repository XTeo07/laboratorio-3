import unittest
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("data/sri_ventas_2024.csv")

    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)

    def test_ventas_totales_todaslas_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        total_provincias = len(resumen)
        self.assertEqual(total_provincias, 24)

    def test_ventas_totales_mayores_5k(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertTrue(all(float(v) > 5000 for v in resumen.values()))

    def test_ventas_por_provincias_inexistente(self):
        with self.assertRaises(KeyError):
            self.analizador.ventas_por_provincia("Calderon")

    def test_ventas_por_provincia_mayusculas_minusculas(self):
        """Prueba que la búsqueda no sea sensible a mayúsculas o minúsculas"""
        # Asegurarse de que "quito" y "QUITO" devuelvan el mismo resultado
        resultado_mayusculas = self.analizador.ventas_por_provincia("PICHINCHA")
        resultado_minusculas = self.analizador.ventas_por_provincia("pichincha")
        self.assertEqual(resultado_mayusculas, resultado_minusculas)

    def test_exportaciones_totales_por_mes(self):
        exportaciones = self.analizador.exportaciones_totales_por_mes()
        self.assertIsInstance(exportaciones, dict)
        self.assertTrue(all(float(v) >= 0 for v in exportaciones.values()))

    def test_provincia_con_mayor_importacion(self):
        provincia, valor = self.analizador.provincia_con_mayor_importacion()
        self.assertIsInstance(provincia, str)
        self.assertIsInstance(valor, float)
        self.assertTrue(valor > 0)
        
    def test_porcentaje_ventas_tarifa_cero_formato(self):
        """Verifica que la función retorne un diccionario con valores numéricos válidos"""
        resultado = self.analizador.porcentaje_ventas_tarifa_cero()
        self.assertIsInstance(resultado, dict)

        for provincia, porcentaje in resultado.items():
            self.assertIsInstance(provincia, str)
            self.assertIsInstance(porcentaje, float)
            self.assertGreaterEqual(porcentaje, 0)
            self.assertLessEqual(porcentaje, 100)

    