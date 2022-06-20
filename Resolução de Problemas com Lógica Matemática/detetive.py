# trabalho realizado por 
# Gustavo Emiliano da Silva
# Marcos Gabriel Troiano
# Maria Júlia lazaroto
import time

pistaA = False
pistaB = False 
pistaC = False
pistaD = False 
pistaE = False 
pistaF = False
pistaG = False
pistaH = False
pistaI = False

listaPistas = []

def pedirInt(texto):
    while True:
        try:   
            resposta= int(input(texto))
            return resposta
        except: print("inválido")


def final():
    if pistaA == True and pistaB == True and pistaF == False:
        print("Você postou sobre Jonas e Cleiton serem um casal e eles realmente eram! Porém você ainda não sabe sobre a situação de Sheila e Mariana")
    if pistaI == True and pistaG == False:
        print("Você postou sobre Mariana e Sheila e elas eram um casal! Elas ficaram muito feliz com a postagem")
    if  pistaF == True:
        print("Você postou sobre Jonas ter terminado o relacionamento com Mariana e isso acabou estragando a real relação de amizade que eles tinham")    
    if pistaH == True and pistaG == True:
        print("Você postou que Cleiton e Mariana estão juntos, porém isso não era verdade e agora eles ficaram desconfortáveis com os olhares das pessoas e terminaram sua amizade")

print("Bem vindo ao nosso jogo detetive")
time.sleep(3)
print("\nÉ um belo dia normal, você tem uma página de fofocas da sua sala, e queria mais babados para postar, então foi atrás de conteúdo para sua página... Em sua sala havia um grupinho inseparável de 4 amigos, onde todos estavam em um relacionamento. A sala toda estava pechinchando e tentando descobrir quais eram os casais entre eles. Mas todos eles eram suspeitos, afinal, era nítido que todos eles eram bem próximos, porém eles não tinham nenhuma pista sobre o caso. Mas certo dia, resolvemos investigar sobre e então logo rumores surgiram...")
time.sleep(8)


entrada = pedirInt("\nAgora você está decidido a investigar sobre, digite 1 para ir até a entrada do colégio ou digite 2 para ir até outro bloco\n")

if entrada == 1:
    print("\nVocê observa de longe que Jonas e cleiton saíram juntos do colégio")
    time.sleep(2)
    pistaA = True
    
    rota1 = pedirInt("\nAgora onde deseja ir?\n1 - Corredor do bloco mais próximo\n2- Refeitório do campus\n")
    if rota1 == 1:
        print("\nVocê caminha até o bloco mais perto e então nota Sheila dando um beijo na bochecha de Mariana de despedida")
        pistaD = True
        time.sleep(2)
        print("\nVocê também notou que Sheila está usando o casado de Jonas ")
        pistaE = True

    elif rota1 == 2:
        print("\nVocê caminha até o refeitório e vê Mariana junta de Cleiton, ela está dividindo seu lanche com Cleiton")
        pistaH = True 
        time.sleep(2)
        print("\nEm sequida você Jonas se aproximando dos dois e então Cleiton e Jonas se separam de Mariana, seguindo eles você os vê entrando em uma sala vazia")
        pistaB = True

    fimrota1=pedirInt("\nO dia está terminando e o céu ja está escurecendo, você terá que fazer sua postagem agora se não a fofoca perderá o hype\n1- Investigar mais \n2- Postar a fofoca\n")
    if fimrota1 == 1:
        print("\nVocê observa mariana chorando ao sair do campus e de longe estava Jonas com uma cara de raiva")
        pistaF = True
        time.sleep(2)
        final()
    elif fimrota1 == 2:
        time.sleep(2)
        final()

if entrada ==2:
    print("\nVocê adentra ao bloco adjacente ao seu, nos corredores você vê Sheila e Mariana abraçadas")
    pistaC == True

    rota2 = pedirInt("\nVocê então segue as duas até que uma hora elas tomam rumos diferentes, quem você segue? \n1- Mariana \n2- Sheila\n")
    if rota2 == 1:
        print("\nAo seguir Sheila você se depara com ela se encontrando com Cleiton no refeitorio")
        pistaH = True
        time.sleep(2) 
        fimrota2 = pedirInt("\nQuer continuar seguindo os dois? \n1- Sim \n2- Não\n")
        if fimrota2 == 1:
            print("\nVocê observa que os dois vão embora juntos")
            pistaG = True
        elif fimrota2 == 2:
            print("\nVocê espera um pouco no refeitorio e vê Sheila passando com um cartão com um coração escrito com o nome 'Mariana'")
            pistaI = True
            time.sleep(2)
            ffimrota2 = pedirInt("\nDeseja ir até o portão de saída onde Mariana foi com Cleiton \n1- Sim \n2- Não\n")
            if ffimrota2 == 1:
                print("\nVocê observa que Mariana e Cleiton vão embora juntos e então decide postar sobre")
                pistaG = True
                time.sleep(2)
                final()
            elif ffimrota2 ==2:
                final()
