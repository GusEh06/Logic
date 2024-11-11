"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

def esAnagrama(palabra1: str, palabra2: str):
    return True if ''.join(sorted(palabra1.lower())) == ''.join(sorted(palabra2.lower())) else False

palabra1 = input("Ingresa la primera palabra para evaluar si es un Anagrama\n$ ")
palabra2 = input("Ingresa la segunda palabra\n$ ")

if esAnagrama(palabra1, palabra2):
    print(f"{palabra1} es un Anagrama de {palabra2}")
else:
    print("Ambas palabras NO son Anagramas")