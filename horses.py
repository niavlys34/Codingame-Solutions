n = int(input())

pis = list()

for i in range(n):
    pis.append(int(input()))
    
pis.sort()

gap = float('inf')
last_pi = 0

for pi in pis:
    if (pi - last_pi) < gap:
        gap = pi - last_pi
    # Supposons qu'il n'y aura jamais 2 puissances égales
    #  (ce n'est pas précisé dans la consigne)
    # 1 étant l'écart le plus faible, on peu s'arrêter et
    # éviter de continuer la boucle pour rien...
    if gap == 1: break
    last_pi = pi

print(gap)
