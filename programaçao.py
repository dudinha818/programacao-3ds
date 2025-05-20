def calcular_engajamento(curtidas, comentarios, compartilhamentos, seguidores=None, alcance=None, impressoes=None):
    if seguidores:
        engajamento_seguidores = (curtidas + comentarios + compartilhamentos) / seguidores * 100
        print(f"Engajamento por seguidores: {engajamento_seguidores:.2f}%")

    if alcance:
        engajamento_alcance = (curtidas + comentarios + compartilhamentos) / alcance * 100
        print(f"Engajamento por alcance: {engajamento_alcance:.2f}%")

    if impressoes:
        engajamento_impressoes = (curtidas + comentarios + compartilhamentos) / impressoes * 100
        print(f"Engajamento por impressões: {engajamento_impressoes:.2f}%")

# Solicitar entrada do usuário
curtidas = int(input("Digite o número de curtidas: "))
comentarios = int(input("Digite o número de comentários: "))
compartilhamentos = int(input("Digite o número de compartilhamentos: "))

seguidores = input("Digite o número de seguidores (ou deixe em branco): ")
alcance = input("Digite o alcance (ou deixe em branco): ")
impressoes = input("Digite o número de impressões (ou deixe em branco): ")

# Converter entradas para inteiro se fornecidas
seguidores = int(seguidores) if seguidores else None
alcance = int(alcance) if alcance else None
impressoes = int(impressoes) if impressoes else None

# Calcular engajamento
calcular_engajamento(curtidas, comentarios, compartilhamentos, seguidores, alcance, impressoes)
