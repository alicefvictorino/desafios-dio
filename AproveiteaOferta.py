teste = int(input())

for i in range(teste):
    garrafas_compradas, garrafas_vazias = map(int, input().split())
    total = (garrafas_compradas % garrafas_vazias) + (garrafas_compradas // garrafas_vazias)
    print(total)
