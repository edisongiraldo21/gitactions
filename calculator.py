def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b


if __name__ == "__main__":
    # Ejemplo de uso
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = sumar(num1, num2)
    print(f"Resultado: {resultado}")
