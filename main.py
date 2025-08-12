import vendas.calcula_preco
import vendas.formata.preço
preco = 49.90
preco_comaumento = vendas.calcula_preco.aumento(valor=preco, porcentagem= 20, formata=True)
print(preco_comaumento)

preco_comdesconto = vendas.calcula_preco.reducao(valor=preco, porcentagem=20, formata=True)
print(preco_comdesconto)
