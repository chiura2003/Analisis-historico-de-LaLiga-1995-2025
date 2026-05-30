import unittest
import pandas as pd
from src.exercises.ex6 import fun_total_goals

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
         Ejecuta un conjunto de instrucciones
         una única vez antes de ejecutar los test

         6-ES-Testing_matenimiento_y_despliegue
        """

        cls.df = pd.DataFrame({
            "FTHG": [3, 4, 3],
            "FTAG": [0, 0, 2]
        })

    def test_home_goals(self):
        """
        Comprueba que la suma de goles locales es correcta.
        """

        # Obtenemos únicamente los goles locales
        home_goals, _, _ = fun_total_goals(self.df)

        self.assertEqual(home_goals, 10)

    def test_away_goals(self):
        """
        Comprueba que la suma de goles visitantes es correcta.
        """
        _, away_goals, _ = fun_total_goals(self.df)

        self.assertEqual(away_goals, 2)

    def test_total_goals(self):
        """
        Comprueba que la suma total de goles es correcta.
        """

        # Obtenemos únicamente los goles totales
        _, _, total_goals = fun_total_goals(self.df)

        # Verificamos que el resultado esperado es 9
        self.assertEqual(total_goals, 12)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, exit=False)

