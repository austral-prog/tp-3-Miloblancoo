def check_vowels():
    # Código a implementar utilizando input.
    nombre = input("Ingrese nombre: ").lower()
    print (nombre)

    print ("")

    print (f"{"contiene a:"} {"a" in nombre}")
    print (f"{"contiene e:"} {"e" in nombre}")
    print (f"{"contiene i:"} {"i" in nombre}")
    print (f"{"contiene o:"} {"o" in nombre}")
    print (f"{"contiene u:"} {"u" in nombre}")


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
