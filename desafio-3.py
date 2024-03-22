# Cálculo de distância

distance = int(input("Digite a distância que deseja percorer:\n"))

if distance < 200:
    result = distance * 0.50
    print(f"O valor é: {result}\n")
elif distance > 200:
    result = distance * 0.35
    print(f"O valor é: {result}\n")
    
# Cálculo de aumento salarial

remuneration = int(input("Digite seus vencimentos:\n"))

if remuneration > 1250.00:
    result1 = (remuneration * 0.10)
    result2 = (remuneration + result1)
    print(f"O aumento salarial será de: {result2}\n")
elif remuneration < 1250.00:
    result1 = (remuneration * 0.15)
    result2 = (remuneration + result1)
    print(f"O aumento salarial será de: {result2}\n")
    
    
    
    