import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Gerador de Senhas Seguras")
    length = int(input("Digite o comprimento da senha (padrão 12): ") or 12)
    password = generate_password(length)
    print("Senha gerada:", password)

if __name__ == "__main__":
    main()
