# python3 controle_notas.py
nome = input ("Digite o seu nome: ")
pergunta = int (input ("digite uma nota: "))
pergunta2 = input ("deseja digitar outra nota? ")

while pergunta2 == 'sim':
    pergunta = int (input ("digite uma nota: "))
    pergunta2 = input ("deseja digitar outra nota? ")