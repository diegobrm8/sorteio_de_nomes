class StringUtils:

    @staticmethod
    def e_palindrome(word):
        return word == word[::-1]

    @staticmethod
    def tem_vogal(word):
        vogais = "aeiou"
        return any(caractere.lower() in vogais for caractere in palavra)

    @staticmethod
    def tem_numeros(word):
        return any(caractere.isdigit() for caractere in palavra)

    @staticmethod
    def contar_letras(word):
        return len(palavra)

    @staticmethod
    def contar_vogais(word):
        vogais = 'aeiou'
        return sum(caractere.lower() in vogais for caractere in palavra)

    @staticmethod
    def contar_consoantes(word):
        vogais = "aeiou"
        return sum(caractere.isalpha() and caractere.lower() not in vogais for caractere in palavra)

    @staticmethod
    def substituir_vogais(word, substituicao):
        vogais = 'aeiou'
        return ''.join(substituicao if caractere.lower() in vogais else caractere for caractere in palavra)


palavra = "paralelep1pedo"

print(StringUtils.e_palindrome(palavra))
print(StringUtils.tem_vogal(palavra))
print(StringUtils.tem_numeros(palavra))
print(StringUtils.contar_letras(palavra))
print(StringUtils.contar_vogais(palavra))
print(StringUtils.contar_consoantes(palavra))
print(StringUtils.substituir_vogais(palavra, '*'))
