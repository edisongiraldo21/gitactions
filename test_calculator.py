import unittest
from calculator import sumar


class TestCalculadora(unittest.TestCase):
    """Pruebas unitarias para la función sumar."""

    def test_sumar_positivos(self):
        """Test suma de números positivos."""
        self.assertEqual(sumar(3, 5), 9)

    def test_sumar_negativos(self):
        """Test suma de números negativos."""
        self.assertEqual(sumar(-2, -4), -6)

    def test_sumar_mixto(self):
        """Test suma con números positivos y negativos."""
        self.assertEqual(sumar(-3, 7), 4)

    def test_sumar_decimales(self):
        """Test suma con números decimales."""
        self.assertAlmostEqual(sumar(2.5, 3.2), 5.7)

    def test_sumar_cero(self):
        """Test suma con cero."""
        self.assertEqual(sumar(0, 5), 5)
        self.assertEqual(sumar(5, 0), 5)


if __name__ == "__main__":
    unittest.main()
