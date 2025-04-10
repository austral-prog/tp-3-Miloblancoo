def check_vowels():
    # Código a implementar utilizando input.
    nombre = input("Ingrese nombre: ").lower()
    
    print ( "contiene a:", "a" in nombre or "A" in nombre)
    print ( "contiene e:", "e" in nombre or "E" in nombre)
    print ( "contiene i:", "i" in nombre or "I" in nombre)
    print ( "contiene o:", "o" in nombre or "O" in nombre)
    print ( "contiene u:", "u" in nombre or "U" in nombre)


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
