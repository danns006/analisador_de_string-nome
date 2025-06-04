# A analise de nome

#Este projeto simples em Python pede ao usuário que digite seu nome e, com base nisso, exibe várias informações

nome = input("Digite seu nome: ").strip()

if not nome:
    print("Você não digitou um nome valido.")

else:
    print(f"\nAnalise do nome: {nome}.")
    print(f"Seu nome ao contrario é {nome[::-1]}.")
    print(f"Seu nome tem {len(nome)} Letras.")
    print(f"Seu nome tem {nome.count(' ')} espaços.")
    print(f"Seu nome em Letras maiusculas: {nome.upper()}.")
    print(f"Seu nome em letras minusculas: {nome.lower()}.")
    print(f"Seu nome contem espaços: {'Sim' if ' ' in nome else 'não'}.")
    print(f"Seu nome começa com a letra: {nome[0]}.")
    print(f"Seu nome termina com a letra: {nome[-1]}.")
    print(f"seu nome tem {len(nome.replace(' ',''))} letras")

