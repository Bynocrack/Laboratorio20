salario_base = 3000
horas_extras = 10
pago_hora_extra = 20
bono = 500
afp = 12  
salud = 9  

salario_bruto = salario_base + (horas_extras * pago_hora_extra) + bono
descuentos_totales = (salario_base * afp / 100) + (salario_base * salud / 100)
salario_neto = salario_bruto - descuentos_totales

print("Salario Bruto:", salario_bruto)
print("Descuentos Totales:", descuentos_totales)
print("Salario Neto:", salario_neto)
