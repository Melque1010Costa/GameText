from time import sleep
import sys
import random
import os





'''Jogo produzido por Melquezedeque Costa Bezerra.Aluno de Ciências da computação -UFMA 2020_2.

Bem vindo ao Infecting. O Infecting é um jogo onde o jogador é uma patógeno que tenta infectar um hospedeiro,evoluir e matar o hospedeiro,até dizimar todo o mundo.
Esse jogo tem intuito de fazer com que você aprenda sobre diversas áreas do conhecimento e se divirta tornando-se a doença mais letal do mundo.
Bom Jogo e boa sorte.'''

def  linha(txt):
    print("☼"*120)
    print(txt)
    print("☼"*120)

def timereverso():
  for s in range(0, 5):
    sys.stdout.write("\r{}".format(s))
    sys.stdout.flush()
    sleep(1)


def anime_text(texto):
   for animi in list(texto):
     print(animi,end='')
     sys.stdout.flush()
     sleep(0.02)

def cor_pergunta(pergunta):
   print(f"\033[4;30;41m{pergunta}\033[m")
def cor_trama(trama):
   print(f"\033[7;33;40m{trama}\033[m")


nome = input("\033[1;40m Digite seu nome para começar o jogo:\033[m\n\n>>>")
nome= nome.capitalize()
if nome != "":

  anime_text(f"\n       \033[1;40m Olá ,{nome}.\nSeja bem vindo ao Infecting!\033[m\n \n ")
  sleep(2)
else:
    anime_text(f"\n\n\t  Olá,jogador Sem Nome.\nSeja bem vindo ao Infecting!\n\n")
#Jogador iniciante ou veterano?
resposta=input(f"\033[1;40m\n\n{nome}, Você precisa de tuturial sobre o Infecting\n\nSim ou Não?\033[m\n\n>>>")
os.system('clear') or None

resposta=resposta.lower()

if resposta == "não":
    print("Então vamos começar! ")
if resposta == "sim" or resposta == "s" :

   tutor = anime_text("\n\n\033[1;34mO Infecting é um game text onde você é um patógeno que precisa evoluir por meio de algumas perguntas \nde conhecimentos gerais  por fim causar doenças até o obito do hospedeiro no nivel 1, um cidade no nivel 2, e um estado no nivel 3 você está preparado?\n\n\033[m")

inicio = input("Aperte ENTER para começar!?\n\n....")
timereverso()
os.system('clear') or None



#nivel a escolher.
nivel = anime_text("\033[1;33;40m\tEntre os niveis:\033[m\n\n \033[1;34;40m1 - Jovem Gafanhoto\t\033[m\n\n \033[1;32;40m2 - Digno de Valhalla\033[m \n\n \033[1;33;40m3- Detentor de todo conhecimento\t\033[m\n\n") 
nivel = int(input("\n\033[1;32;40mVocê escolhe o 1, 2 ou 3 ?\t\033[m\n\n>>"))
if  nivel==404:
  nivel="EXODIA"
os.system('clear') or None


nome_virus = input("\033[1;32;40mQual nome terá seu Patógeno?\n\n>>>\033[m" )
nome_hospedeiro = input("\n\033[1;32;40mQual nome terá seu hospedeiro?\n\n>>>\033[m")

os.system('clear') or None

explicação = anime_text("\n\n\033[1;32mVocê vai ter 5 perguntas,que fará,você,patógeno evoluir e levar o hospedeiro ao obito,destruir uma cidade,um estado ou quem sabe o mundo.\nCaso contrario você será destruido!\033[m\n\n")
sleep(4)
explicação2=anime_text("\033[7;35;47m Agora vamos para as perguntas;\nresponta a letra correspondende\n a alternativa que acha certa:\nMarque 1,2,3 ou 4 referente a resposta certa!\nSeu jogo vai começar em 5segundos")
print(f"\nEntão vamos lá {nome_virus}!\033[m\n")
sleep(6)
os.system('clear') or None

 #Perguntas nivel 1:

if nivel==1:
 
  cout = 0
  pergunn = [0,1,2,3,4,5,6]
  random.shuffle(pergunn)

  for i in range(0,5):
    pergun=pergunn[i]
    if pergun == 0:
      p1txt=cor_pergunta("\nQual o menor e o maior país do mundo?\n1- Vaticano e Rússia\n2- Nauru e China\n3- Mônaco e Canadá\n4- Malta e Estados Unidos\n\nA resposta é:\n\n")
      p1=int(input())
      if p1 == 1:
        cout = cout+1
        print("Resposta certa")
        print("Aperte enter para proxima.")
        caso=input()
        sleep(2)
        os.system('clear') or None
      else:
        i = 8

      


    if pergun == 1:

      pt2tx=cor_pergunta("\n Quais os 4 primeiros numeros do valor de pi ?\n\n1) 3,158\n2) 3,141\n3) 3,148\n4) 3,14\nA resposta é:\n\n")
      p2=int(input())
      if p2 == 2:
        cout = cout+1
        print("Resposta certa")
        print("Aperte enter para proxima.")
        sleep(1)
        caso=input()
        os.system('clear') or None
      else:
        i = 8
        

    if pergun==2:

      pt3tx=cor_pergunta("\n Qual a derivada da função:\nf(x)=7x²+1x+x³ ?\n\n1) 7x+1+1\n2) 14x+x+3x²\n3) 17+1x+3x²\n4) 14x+1+3x²\n\nA resposta é:\n\n")
      p3=int(input())
      if p3==4:
        cout=cout+1
        print("Certa resposta")
        print("Aperte enter para proxima.")
        sleep(1)
        caso=input()

        os.system('clear') or None
      else:
        i=8
      
    

    if pergun == 3:

      p4tx=cor_pergunta("\n Qual a linguagem de programação que lembra uma cobra?\n1) c#\n2) c++\n3) anaconda\n4) python\n\nA resposta é:\n\n")
      p4=int(input())
      if p4 == 4:
        cout=cout+1
        print("Certa resposta")
        print("Aperte enter para proxima.")
        sleep(1)
        caso=input()
        os.system('clear') or None
      else:
        i=8
    
      
    if pergun == 4:

      p5tx=cor_pergunta("\n Qual o número mínimo de jogadores numa partida de futebol?\n\n1) 7\n2) 10\n3) 9\n4) 5\n\nA resposta é:\n\n")
      p5=int(input())
      if p5==1:
        cout=cout+1
        print("Você acertou")
        print("Aperte enter para proxima.") 
        sleep(1)
        caso=input()
        os.system('clear') or None
      else:
        i=8

   
    if pergun == 5:

      p6tx=cor_pergunta("\nO que a palavra legend significa em português?\n\n1- Legenda\n2- Lendario\n3- História\n4- Lenda\n\nA resposta é:\n\n")
      p6=int(input())
      if p6==4:
        cout=cout+1
        print("Você acertou")
        print("Aperte enter para proxima.") 
        sleep(1)
        caso=input()
        os.system('clear') or None
      else:
        i=8

    if pergun == 6:

      p7tx=cor_pergunta("\nQuanto tempo a luz do Sol demora para chegar à Terra?\n1- 12 minutos\n2- segundos\n3- 12 horas\n4- 8 minutos\n\nA resposta é:\n\n")
      p7=int(input())
      if p7==4:
        cout=cout+1
        print("Você acertou")
        print("Aperte enter para proxima.") 
        sleep(1)
        caso=input()
        os.system('clear') or None
      else:
        i=8
    

    elif i==8:
      derrota=["Você morreu!\nGAME OVER!","Você foi destruido!\n GAME OVER!","Que derrota feia.\nGame OVER!"]
      print(random.choice(derrota))
      break
    
    

    
    
    
    
    #evoluções conforme for acertanto
    if cout==1:
      cor_trama(f"\n O {nome_hospedeiro} fez um frango e não limpou você foi ingerido. \n Você passou da primeira parte,virou um microbio.\n Agora continue acertando as questões para evoluir.\n\n")
    if cout==2:
      cor_trama(f"\n O {nome_hospedeiro} ainda não sabe de sua existencia {nome_virus} \nvocê ja está a 3 meses dentro do seu hopedeiro\nvocê agora é um poderoso virus\n\n")
    if cout==3:
      cor_trama(f"\n O {nome_hospedeiro} está sendo encaminhado pra UTI\n você acaba de pararisitar todo a região da celulas estomacais do {nome_hospedeiro}.\nContinue acertando,você está tão perto de acabar com ele! \n\n")
    if cout==4:
      cor_trama(f"\n O {nome_hospedeiro} foi encaminhado para cirugia,você está totalmente poderoso\n se na cirugia que vão fazer não tiraram você\n acredito que o {nome_hospedeiro} não vai passe dessa!\n\n")

    


  #fim de game,vencendo mundo 1
  if i != 8:

    fim=anime_text(f"\n\033[4;32m Parabéns ,você venceu  {nome_virus}\n, o {nome_hospedeiro} teve uma morte terrivel.\n Você é um virus capaz de destruir todo o sistema digestivo,\ncausando sagramentos internos e desregularização no controle fecal,\n levando o o contaminado expelir fezes por diversos lugares sem controle até morrer,literalmente 'todo cagado'.\nAgora você está para virar uma epidemia\n\033[m")
    

    sleep(3)
    nivel12=anime_text("\n\nVocê quer ir pro nivel 2?.\nLá você vai poder infectar uma cidade toda.vocês aceita ou vai amarelar?\nSe for amarelar so digitar qualquer tecla,\n mas caso seja corajosso digite  enter e seu proximo nivel começa em 10sgundos!")
    nivel123=input()
    sleep(4)

    if nivel123!="":
    
      derrota=anime_text("\n\nObrigado por jogar o Infecting!!\n\n")
    else:
      nivel=2
      
      sleep(3)
     
#nivel 2-Medium
if nivel==2:
  print("Bem vindo ao nível 2!")
  if nivel==2 :
    nome_cidade=input("\n\nAgora você vai infectar uma cidade\n qual nome que você escolhe pra essa cidade?\n>>")


  cout1 = 0
  pergunn = [0,1,2,3,4,5,6]
  random.shuffle(pergunn)

  for j in range(0,5):
    pergun=pergunn[j]

    if pergun == 0:
      cor_pergunta("\nQuais as duas datas que são comemoradas\n em novembro?\n1) Independência do Brasil e Dia da Bandeira.\n2) Proclamação da República e Dia Nacional da Consciência Negra.\n3) Dia do Médico e Dia de São Lucas.\n4) Dia de Finados e Dia Nacional do Livro.\n\nA resposta é:\n\n")
      p1=int(input())
      if p1 == 4:
        cout1 = cout1+1
        print("Resposta certa")
        print("Aperte enter para proxima.")
        caso=input()
        sleep(1)
        os.system('clear') or None
      else:
        j = 8

    


    if pergun == 1:


      pt2tx=cor_pergunta("\nQuem pintou 'Quernica'?\n1) Paul Cézanne\n2) Pablo Picasso\n3) Diego Rivera\n4) Tarsila do Amaral\n\nA resposta é:\n\n")
      p2=int(input())
      if p2 == 2:
        cout1 = cout1+1
        print("Resposta certa")
        print("Aperte enter para proxima.")
        sleep(1)
        caso=input()
        os.system('clear') or None
      else:
        j = 8
        

    if pergun==2:

      cor_pergunta("\n Qual a tradução da frase “Fabiano cogió su saco antes de salir”?\n1- Fabiano coseu seu paletó antes de sair\n2- Fabiano fechou o saco antes de sair\n3- Fabiano pegou seu paletó antes de sair\n4- Fabiano cortou o saco antes de cair\nA resposta é:\n\n")
      p3=int(input())
      if p3==3:
        cout1=cout1+1
        print("Certa resposta")
        print("Aperte enter para proxima.")
        sleep(1)
        caso=input()
        os.system('clear') or None
      else:
        j=8
      
    

    if pergun == 3:

      cor_pergunta("\nEm que período da pré-história o fogo foi descoberto?\n1) Neolítico\n2) Paleolítico\n3) Idade dos Metais\n4) Período da Pedra Polida\nA resposta é:\n\n")
      p4=int(input())
      if p4 == 2:
        cout1=cout1+1
        print("Certa resposta")
        print("Aperte enter para proxima.")
        sleep(1)
        caso=input()
        os.system('clear') or None
      else:
        j = 8
    
      
    if pergun == 4:

      cor_trama("\n It is six twenty ou twenty past six. Que horas são em inglês?\n1) 12:06\n2) 6:20\n3) 2:20\n4) 6:02\nA resposta é:\n\n")
      p5=int(input())
      if p5==2:
        cout1=cout1+1
        print("Você acertou!")
        print("Aperte enter para proxima.") 
        sleep(1)
        caso=input()
        os.system('clear') or None
      else:
        j = 8
      
    if pergun == 5:

      cor_trama("\n Qual a montanha mais alta do Brasil?\n\n1- Pico da Neblina\n2- Pico Paraná\n3- Monte Roraima\n4- Pico Maior de Friburgo\nA resposta é:\n\n")
      p6=int(input())
      if p6==1:
        cout1=cout1+1
        print("Você acertou!")
        print("Aperte enter para proxima.") 
        sleep(1)
        caso=input()
        os.system('clear') or None
      else:
        j = 8

    if pergun == 6:

      cor_trama("\n Qual destes países é transcontinental?\n\n1- Rússia\n2- Filipinas\n3- Istambul\n4- Groenlândia\nA resposta é:\n\n")
      p7=int(input())
      if p7==1:
        cout1=cout1+1
        print("Você acertou!")
        print("Aperte enter para proxima.") 
        sleep(1)
        caso=input()
        os.system('clear') or None
      else:
        j = 8



    elif j==8:
      derrota=["Você morreu!\nGAME OVER!","Você foi destruido!\n GAME OVER!","Que derrota feia.\nGame OVER!","Você é fraco,lhe falta ódio.\n GAME OVER"]
      print(random.choice(derrota))
      break

    
    
    
    
    #evoluções de interações conforme for acertanto
    if cout1==1:
      cor_trama(f" \n Os medicos ainda não sabem da sua existencia\n despejaram o {nome_hospedeiro} para uma ala errada do IML e você acaba de contaminar todo um setor do IML.\nContinue a acertar e evoluir!!\n\n")
    if cout1==2:
      cor_trama(f"\n O {nome_virus} ja foi detectado após contaminar um total de 100 funcionarios no IML\n você tem que se expalhar mais rapido para não ser destruido .\nContinue acertando as perguntas antes que você seja destruido.\n\n")
    if cout1==3:
      cor_trama(f"\n Ja faz 4 meses que o virus {nome_virus} está a solta em {nome_cidade},\n e ja tem um total contaminação de 40% de toda população de {nome_cidade}.\nVocê está fora do controle,continue acertando as questões.\n\n")
    if cout1==4:
      cor_trama(f"\n {nome_cidade} Está em alerta MAXIMO!\n. Foi mandado uma equipe para acabar com o virus {nome_virus}\n.Se eles chegarem antes de você contaminar os ultimos 20 % que faltam da população de {nome_cidade}... será seu fim\n.Responda rapido a proxima pergunta:\n\n")

    


  #fim de game,vencendo
  if j != 8:

    nivel21=anime_text(f"\n\033[1;95mToda a equipe que foi mandada pra destruir o {nome_virus} foi totalmente contaminada e dizimada\n.O virus {nome_virus} evoluiu para uma pandemia e agora que é capaz de matar os infectados de um forma horrenda.\nA relatos de que virão pessoas serem contaminadas e em 2 dias elas começaram a literalmente a explodir expelindo fezes para todos os lados.\nA {nome_cidade} foi 100% contaminada,\nvocê venceu essa etapa ,PARABÉNS.. \033[c\n")

    sleep(6)
    nivel2=anime_text("\n\033[1;95mVocê quer ir pro nivel 3?,\nlá você vai poder infectar todo um estado ou talvez até um continente ,será se você consegue,ou vai dessistir?\nNão vai ser facíl,acho que vocÊ não consegue..\n\033[m")
    sleep(5)
    linha("\nSe quiser ir ao nivel 3 aguarde 10 segundos que seu nivel 3 vai começar,caso contrario aperte qualquer tecla.\n")
    if nivel2!="":
      nivel=3
      sleep(8)
      os.system('clear') or None

    else:
      print("Obrigado por Jogar o Infeceting!")

#nivel 3-Detentor
if nivel==3:
  print("\nBem vindo ao nivel 3\n")
  sleep(2)
  nome_cidade=input("\nDigite o nome da cidade que ira infecta dessa vez.\n\n")
  nome_estado=input("\n\nAgora você vai infectar uma estado.\nQual nome que você escolhe pra esse estado?\n\n")
  print("O seu nivel 3 ja vai começar...")
  sleep(3)
  os.system('clear') or None
  cout2 = 0
  pergunn1 = [0,1,2,3,4,5,6]
  random.shuffle(pergunn1)

  for k in range(0,5):
    pergun1=pergunn1[k]


    #perguntas relacionadas ao nivel 3:
    if pergun1 == 0:
      cor_pergunta("\n Em que ordem surgiram os modelos atômicos?\n\n1- Thomson, Dalton / Rutherford, Rutherford-Bohr\n2- Rutherford-Bohr / Rutherford / Thomson / Dalton\n3- Dalton / Rutherford-Bohr / Thomson / Rutherford\n4- Dalton / Thomson / Rutherford / Rutherford-Bohr\nA resposta é:\n\n")
      p1=int(input())
      if p1 == 4:

        cout2 = cout2+1
        print("Resposta certa!")
        print("Aperte qualquer enter para proxima.")
        sleep(1)
        caso=input()
        os.system('clear') or None

      else:
        k = 8

      


    if pergun1 == 1:

      p2txt=cor_pergunta("\n Qual o tema do famoso discurso Eu Tenho um Sonho, de Martin Luther King?\n\n1- Igualdade das raças\n2- Justiça para os menos favorecidos\n3- Prêmio Nobel da Paz\n4- Luta contra o Apartheid:\nA resposta é:\n\n")
      p2=int(input())
      if p2 == 1:
        cout2 = cout2+1
        print("Resposta certa!")
        print("Aperte qualquer enter para proxima.")
        caso=input()
        sleep(1)
        os.system('clear') or None
      else:
        k = 8
        

    if pergun1==2:

      p3tx=cor_pergunta("\nCalcular a derivada segunda da função\nf(x) = x² + 10x – 9.\n\n1- f”(x) = x\n2- f”(x) = 2\n3- f”(x) = x²\n4- f”(x) = 0:\nA resposta é:\n\n")
      p3=int(input())
      if p3 == 2:
        cout2=cout2+1
        print("Certa resposta")
        print("Aperte qualquer enter para proxima.")
        caso=input()
        sleep(1)
        os.system('clear') or None
      else:
        k= 8
      
    

    if pergun1 == 3:

      p4txrt=cor_pergunta("\nEm qual das orações abaixo a palavra foi empregada incorretamente?\n\n1- Mais uma vez, portou-se mal.\n2- É um homem mal.\n3- Mal falou nele, o fulano apareceu.\n4- É um mau vendedor.\nA resposta é:\n\n")
      p4=int(input())
      if p4==4:
        cout2=cout2+1
        print("Certa resposta!")
        print("Aperte  enter para proxima.")
        caso=input()
        sleep(1)
        os.system('clear') or None
      else:
        k = 8
    
      
    if pergun1 == 4:

      p5txt=cor_pergunta("\nQual foi o recurso utilizado inicialmente pelo\n homem para explicar a origem das coisas?\n1- A Filosofia\n2- A Mitologia\n3- A Matemática\n4- A Biologia\nA resposta é:\n\n")
      p5=int(input())
      if p5==2:
        cout2=cout2+1
        print("Você acertou")
        print("Aperte qualquer enter para proxima.") 
        caso=input()
        sleep(1)
        os.system('clear') or None
      else:
        k = 8

    if pergun1 == 5:

      p6txt=cor_pergunta("\nQuais os planetas do sistema solar?\n\n1- Terra, Vênus, Saturno, Urano, Júpiter, Marte, Netuno, Mercúrio\n2- Júpiter, Marte, Mercúrio, Netuno, Plutão, Saturno, Terra, Urano, Vênus\n3- Vênus, Saturno, Urano, Júpiter, Marte, Netuno, Mercúrio\n4- Júpiter, Marte, Mercúrio, Netuno, Plutão, Saturno, Sol, Terra, Urano, Vênus\nA resposta é:\n\n")
      p6=int(input())
      if p6==1:

        sleep(1)
        cout2=cout2+1
        print("Você acertou")
        caso=input()
        print("Aperte qualquer enter para proxima.") 
        os.system('clear') or None
      else:
        k = 8

    if pergun1 == 6:

      p7txt=cor_pergunta("\nQuem amamentou os gêmeos Rômulo e Remo?\n\n1- uma cabra\n2- uma vaca\n3- uma ovelha\n4- uma loba\nA resposta é:\n\n")
      p7=int(input())
      if p7==4:
        cout2=cout2+1
        print("Você acertou")
        print("Aperte qualquer enter para proxima.") 
        caso=input()
        sleep(1)
        os.system('clear') or None
      else:
        k = 8

    elif k==8:
      derrota=["Você morreu!\nGAME OVER!","Você foi destruido!\n GAME OVER!","Que derrota feia.\nGame OVER!","Você nunca entrarar em Valhalla\n GAME OVER!!","Lher falta ódio,boa sorte proxima vez\nGAME OVER!!"]
      print(random.choice(derrota))
      break
    

    
    
    
    
    #evoluções conforme for acertanto
    if cout2 == 1:
      cor_trama(f"\n A ONU está a 3 meses sem atualizar o seu portal, acreditamos que eles estão em sigilo MAXIMO para evitar escandalos.\nA boatos que por conta da grande evolução do {nome_virus}a ONU ,os serviçoes de saúde do {nome_estado} e até a OMS (Organização mundial de saúde)\nnão sabem o que fazer para conter o {nome_virus}  na agora\n conhecida a cidade fantasma de {nome_cidade}.\nMas foi detectado um caso em uma cidade visinha no estado de {nome_estado}...Será o inicio de uma Pandemia?\n")
    if cout2 == 2:
      cor_trama(f"\n Ouve uma visita ao {nome_estado}, onde representantes da OMS juntamente com  diretor geral se reuniram para estudarem como iram lidar para isolar o {nome_virus}.\nEntretanto,durante a visitação o diretor geral Tedros Adhanom foi contaminado pelo {nome_virus} e veio a obito a 3 dias pós contaminação.\nTodo as cidades visinhas do {nome_estado} registraram diversos casos isolados.\nO {nome_virus} agora foi registrado como um pandemia estatal.\nMuito bom,parabéns,continue assim.")
    if cout2 == 3:
      cor_trama(f"\n O estado {nome_estado} contem exatas 48 cidades onde a 1 ano da descoberta do {nome_virus} pelo paciente 0 {nome_hospedeiro}\n existem até o momento 35 cidades com casos confirmados onde na {nome_cidade} já não é mais habitavel .\ncontinue assim; \n")
    if cout2 == 4:
      cor_trama(f"O {nome_virus} atualmente agora em categoria kiter(categoria maxima de periculosidade de virus) \nfoi o responsavel pela contaminação total do estado {nome_estado}.\nCom um total de 700.000 contaminados onde 49 % foram pacientes fatais.\nA OMS não se pronunciou ainda depois de ser decretado o {nome_estado} um estado inapropriado para para moradia e determinou o {nome_virus} a posivel maior pandemia que o mundo ja enfrentou.\nContinue a evoluir.")


  #fim de game,vencendo
  if k != 8:
    

    nivel21=anime_text(f"Parabéns,vocÊ venceu o Infeceting!!\n\n\nPorem o {nome_virus} não pode parar aenas no estado {nome_estado}. \n {nome_virus} você aceita o desafio de se tornar a maior pandemia de todo mundo? ??\n\nSe não aceita digite qualquer coisa,casso você seja corajosso\n espere 10 segundos que seu NIVEL EXODIA vai começar.")
    

    sleep(16)
    nivel="EXODIA"
    

if nivel=="EXODIA":
  os.system('clear') or None
  print("\n\033[7;30mBem vindo ao nivel nivel EXODIA!\nAqui, cada questão é mais do que qualquer uma dos nivéis anteriores\n cada resposta certá será um continente contaminado.\nVamos acabar com o mundo\033[m")
  print("Seu nivel nive EXODIA ja vai começar")
  os.system('clear') or None
  cout4 = 0
  pergunn4 = [0,1,2,3,4,5,6]
  random.shuffle(pergunn4)

  for z in range(0,5):
    pergun14=pergunn4[z]


    #perguntas relacionadas ao nivel EXODIA:
    if pergun14== 0:
      cor_pergunta("\n O que mede a Escala Mercalli?\n\n1- A intensidade dos ventos\n2- A intensidade sísmica de acordo com os danos provocados\n3- A resistência dos minerais\n4- A magnitude de um terremoto\nA resposta é:\n\n")
      p1=int(input()) 
      if p1 == 2:

        cout4 = cout4+1
        print("Resposta certa!")
        print("Aperte qualquer enter para proxima.")
        sleep(1)
        caso=input()
        os.system('clear') or None

      else:
        z = 8

      


    if pergun14 == 1:

      p2txt=cor_pergunta("\n Carlos e Ana saíram de casa para trabalhar partindo do mesmo ponto, a garagem do prédio onde moram.\n Após 1 min, percorrendo um trajeto perpendicular, eles estavam a 13 m de distância um do outro.\nSe o carro de Carlos fez 7 m a mais que o de Ana durante esse tempo, a que distância eles estavam da garagem?\n\n 1- Carlos estava a 10 m da garagem e Ana estava a 5 m.2- Carlos estava a 14 m da garagem e Ana estava a 7 m.\n3- Carlos estava a 12 m da garagem e Ana estava a 5 m.\n4- Carlos estava a 13 m da garagem e Ana estava a 6 m.\nA resposta é:\n\n")
      
      p2=int(input())
      if p2 == 3:
        cout4 = cout4+1
        print("Resposta certa!")
        print("Aperte qualquer enter para proxima.")
        caso=input()
        sleep(1)
        os.system('clear') or None
      else:
        z = 8
        

    if pergun14==2:


      p3tx=cor_pergunta("\nTem-se uma amostra gasosa formada por um dos seguintes compostos:\n CH4; C2H4; C2H6; C3H6 ou C3H8. Se 22 g \n dessa amostra ocupam o volume de 24,6 L à pressão de 0,5 atm e temperatura de 27 °C (Dado: R = 0,082 L .atm.K–1.mol–1), conclui-se que se trata do gás:\n\n1- etano.\n2- metano.\n3- propano.\n4- propeno.\n\nA resposta é:\n\n")
      p3=int(input())
      if p3==3:
        cout4=cout4+1
        print("Certa resposta")
        print("Aperte qualquer enter para proxima.")
        caso=input()
        sleep(1)
        os.system('clear') or None
      else:
        z= 8
      
    

    if pergun14 == 3:

      p4txrt=cor_pergunta("\nLaura tem de resolver uma equação do 2º grau no “para casa”, mas percebe que, ao copiar do quadro para o caderno, esqueceu-se de copiar o coeficiente de x. Para resolver a equação, registrou-a da seguinte maneira:\n 4x2 + ax + 9 = 0. Como ela sabia que a equação tinha uma única solução, e esta era positiva, conseguiu determinar o valor de a, que é:\n\n1- – 13\n2- – 12\n3- 12\n4- 13\n\n")
      p4=int(input())
      if p4==2:
        cout4=cout4+1
        print("Certa resposta!")
        print("Aperte qualquer enter para proxima.")
        caso=input()
        sleep(1)
        os.system('clear') or None
      else:
        z = 8
    
      
    if pergun14 == 4:

      p5txt=cor_pergunta("\n Um homem apresenta o genótipo Aa Bb CC dd e sua esposa, o genótipo aa Bb cc Dd. Qual é a probabilidade desse casal ter um filho do sexo masculino e portador dos genes bb?\n\n1- 1/4\n2- 1/8\n3- 1/2\n4- 3/64\nA resposta é:\n\n")
      p5=int(input())
      if p5==2:
        cout4=cout4+1
        print("Você acertou")
        print("Aperte qualquer enter para proxima.") 
        sleep(1)
        caso=input()
        os.system('clear') or None
      else:
        z = 8

    if pergun14 == 5:

      p6txt=cor_pergunta("\nExistem cinco reinos que dividem os seres vivos: Monera, Protista, Plantae, Fungi e Animalia. Os vírus não estão incluídos em nenhum desses grupos, pois não são considerados seres vivos já que:\n\n\n1- São seres extremamente pequenos.\n2- Nunca foram estudados em laboratório.\n3- São considerados apenas partículas infecciosas.\n4- Têm o tempo de vida muito curto.\nA resposta é:\n\n")
      p6=int(input())
      if p6==3:
        cout4=cout4+1
        print("Você acertou")
        print("Aperte qualquer enter para proxima.") 
        sleep(1)
        caso=input()
        os.system('clear') or None
      else:
        z = 8
    if pergun14 == 6:

      p7txt=cor_pergunta("\n Assinale a alternativa que corretamente preenche as lacunas I, II e III das frases a seguir:\n\nHe __________(I) me a favor 2 months ago.\n\nThey __________(II) an attempt to escape.\n\nI __________(III) an important decision last night.\n\n1- did – made – made\n2- made – did – made\n3- did – made – did\n4- made – made – made\nA resposta é:\n\n")
      p7=int(input())
      if p7==1:
        cout4=cout4+1
        print("Você acertou")
        print("Aperte qualquer enter para proxima.") 
        caso=input()
        sleep(1)
        os.system('clear') or None
      else:
        z = 8


    if z==8:
      derrota=["Você morreu!\nGAME OVER!","Você foi destruido!\n GAME OVER!","Que derrota feia.\nGame OVER!","Você nunca entrarar em Valhalla\n GAME OVER!!","Lher falta ódio,boa sorte proxima vez\nGAME OVER!!"]
      print(random.choice(derrota))
      break
    

    
    
    
    
    #evoluções conforme for acertanto
    if cout4 == 1:
      cor_trama(f"\n O {nome_virus} acaba de infectar o continente Áfricano!\n")
    if cout4 == 2:
      cor_trama(f"\n O {nome_virus} contaminou todo o continente Assiatico!\n Já foram 2 continentes contaminandos em mais de 2 anos da pandemia do {nome_virus} \ne ja tem o total de 3bilhões de contaminandos em todo o mundo!")
    if cout4 == 3:
      cor_trama(f"\n100% da Oceania e 90% da Antártica está contaminada.\n O numero de mortos está na casa de 2 bilhões de mortos pelo {nome_virus}.\nEstá tendo diversas guerras civis por comida e agua ...a humanidade está caminhando para o fim... \n")
    if cout4 == 4:
      cor_trama(f"O {nome_virus} contaminou todo continente Euroupeu,chegando na marca de 4bilhões de mortos em todo mundo\nAumentou o grupo de fanaticos religiosos,que matam qualquer um que não aceitam seguir com eles\nQue deus que eles estão servindo?!.A humaninada está no fim...talvez esse seja o final da raça humana!")


  #fim de game,vencendo
  if z != 8:
    anime_text(f"\033[1;31mDepois de 3 anos do virus {nome_virus} vim a existir e causar suas primeiras vitimas\nninguem num imaginou que iriamos chegar nesse ponto.\nO virus contaminou o continente americano por completo e toda a população foi dizimada.\n8Bilhões de mortos...\033[m\n\n\n")
    sleep(2)

    nivel21=anime_text("\n\033[1;33mParabéns,vocÊ zerou o Infecting!!\n\n\033[m")

    sleep(10)
    print("Talvez exista novas vidas em outros planetas para infectar....\n\n.")
    parte2=input("Você aceita conhecer o Infecting space?\nsim ou não??\n\n")
    if parte2=="sim":
      os.system('clear') or None
      timereverso()
      os.system('clear') or None
      print("Nivel espacial Em Breve!!\nObrigado por Jogar!!\n")
