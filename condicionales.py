# ==================================
#       Contador de minutos 
# ==================================

#inpunt
print("============================")
print("Bienvenido al contador de minutos ")
print("=============================")
cant_minutos = input("Digite la cantidad de minutos: ")
cant_minutos = int(cant_minutos)
print("=====================================")

# Processing 
print("==================================")
print("Calculando el valor de la llamada...")
if cant_minutos <= 3:
    valor_llamada = 300
else:
    valor_llamada = 300 + 50 * (cant_minutos - 3)
print("===================================")

# Output
print("====================================")
print("El valor de la llamada es: " + str(valor_llamada) + " COP")
print("====================================")
