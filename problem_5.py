#Escreva uma função main que pergunte a distância que um passageiro 
#deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0.50 por 
#km para viagens de até 200 km, R$ 0.45 para viagens entre 200 e 400 km e para viagens 
#mais longas será cobrado R$ 0.35 por km.

def main(distancia):
    if distancia <= 200:
        return distancia*0.5
    elif distancia <= 400:
        return distancia*0.45
    else:
        return distancia*0.35