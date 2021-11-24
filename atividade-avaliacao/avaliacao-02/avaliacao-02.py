frases = [
    "I love you",
    "Bom dia",
    "Durma bem",
    "Tchau",
    "Como foi o seu dia",
    "Boa noite,beijos"
]

for frase in frases:
    mensagem = ""
    maior = ""
    i = 0
    a = frase.split(" ")

    while i < len(a):
        mensagem += str(len(a[i])) + "-"
        if len(a[i]) > len(maior):
            maior = a[i]

        i += 1

    mensagem = mensagem[-len(mensagem):-1]
    print("{:25s} {}".format(mensagem, maior))