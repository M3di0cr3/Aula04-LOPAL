# python3 controle_notas.py
nome = input ("Digite o seu nome: ")
pergunta = input ("deseja digitar uma nota? ")
nota = 0

while pergunta == 'sim':
    pergunta2 = 0
    pergunta2 = int (input ("digite uma nota: "))
    nota = nota + pergunta2
    pergunta = input ("deseja digitar outra nota? ")
    
print (f"Sua média é: {}")