def calcular_engajamento_por_seguidores(curtidas, comentarios, compartilhamentos, seguidores):
    return (curtidas + comentarios + compartilhamentos) / seguidores * 100

def calcular_engajamento_por_alcance(curtidas, comentarios, compartilhamentos, alcance):
    return (curtidas + comentarios + compartilhamentos) / alcance * 100

def calcular_engajamento_por_impressoes(curtidas, comentarios, compartilhamentos, impressoes):
    return (curtidas + comentarios + compartilhamentos) / impressoes * 100

def main():
    curtidas = int(input("Digite o número de curtidas: "))
    comentarios = int(input("Digite o número de comentários: "))
    compartilhamentos = int(input("Digite o número de compartilhamentos: "))
    seguidores = int(input("Digite o número de seguidores: "))
    alcance = int(input("Digite o alcance da publicação: "))
    impressoes = int(input("Digite o número de impressões: "))

    print("\nMétricas de Engajamento:")
    print(f"Engajamento por seguidores: {calcular_engajamento_por_seguidores(curtidas, comentarios, compartilhamentos, seguidores):.2f}%")
    print(f"Engajamento por alcance: {calcular_engajamento_por_alcance(curtidas, comentarios, compartilhamentos, alcance):.2f}%")
    print(f"Engajamento por impressões: {calcular_engajamento_por_impressoes(curtidas, comentarios, compartilhamentos, impressoes):.2f}%")

if __name__ == "__main__":
    main()
