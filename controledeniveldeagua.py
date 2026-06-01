import time
# 1. Importar a biblioteca colorama
from colorama import Fore, Style, init

# Inicializa o colorama para garantir compatibilidade no terminal
init()

# 2. Lista para armazenar as situações do reservatório (Índice 0 = Nível 1, etc.)
situacoes_reservatorio = [
    "Muito baixo (crítico)",  # Nível 1
    "Baixo",                 # Nível 2
    "Médio",                 # Nível 3
    "Alto",                  # Nível 4
    "Muito alto (alerta)"    # Nível 5
]

# 3. Função responsável por definir a cor da mensagem conforme o nível
def obter_cor_por_nivel(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# 4. Função para exibir a situação atual no terminal com a cor correspondente
def exibir_status_reservatorio(nivel):
    if 1 <= nivel <= 5:
        mensagem = situacoes_reservatorio[nivel - 1]
        cor = obter_cor_por_nivel(nivel)
        
        # Exibe a mensagem colorida
        print(f"Status do Reservatório [Nível {nivel}]: {cor}{mensagem}")
        
        # 5. Restaura o estilo padrão do terminal após a exibição
        print(Style.RESET_ALL)
    else:
        print(f"{Fore.RED}Erro: Nível {nivel} inválido.{Style.RESET_ALL}")

# --- SIMULAÇÃO DO SISTEMA ---
print("=== INICIANDO SIMULAÇÃO DE MONITORAMENTO DE ÁGUA ===\n")

# Executa a simulação passando por todos os níveis de 1 a 5
for nivel_atual in range(1, 6):
    exibir_status_reservatorio(nivel_atual)
    time.sleep(0.5) # Pausa de meio segundo entre os níveis

print("=== FIM DA SIMULAÇÃO ===")
