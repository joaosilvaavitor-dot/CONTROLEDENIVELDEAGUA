
# para trocar uma lampada, preciso de uma lampada igual ou semelhante

tenho_lampada_igual = False
tenho_lampada_semelhante = False

posso_trocar_lampada = tenho_lampada_igual or tenho_lampada_semelhante 

print(posso_trocar_lampada)

# SE a resposta for verdadeira, mostra a mensagem de troca
# SENÃO, mostra a mensagem de impossível trocar

if(posso_trocar_lampada == True):
    print("Posso trocar a lampada")
    print("segundo comando do if")
else:
    print("Você não pode trocar a lampada")
    print("segundo comando do else")

print('Fim do programa')

