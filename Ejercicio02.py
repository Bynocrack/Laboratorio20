ingreso_mensual = float(input("Ingrese su ingreso mensual: "))

ingreso_anual = ingreso_mensual * 12 + ingreso_mensual * 2  

tramos = [
    (20000, 0.0),
    (50000, 0.10),
    (100000, 0.20),
    (float('inf'), 0.30)
]

impuesto_total = 0
impuesto_por_tramo = []
ingreso_restante = ingreso_anual
limite_inferior = 0

for limite_superior, tasa in tramos:
    if ingreso_anual > limite_inferior:
        base_tramo = min(ingreso_anual, limite_superior) - limite_inferior
        impuesto_tramo = base_tramo * tasa
        impuesto_por_tramo.append((limite_inferior, limite_superior, tasa, impuesto_tramo))
        impuesto_total += impuesto_tramo
    limite_inferior = limite_superior

print("\n--- Impuesto por tramo ---")
for li, ls, tasa, imp in impuesto_por_tramo:
    print(f"{li} - {ls}: {tasa*100:.0f}% → {imp:.2f}")

tasa_efectiva = (impuesto_total / ingreso_anual) * 100

print("\nTotal de impuestos:", round(impuesto_total,2))
print("Tasa efectiva real: {:.2f}%".format(tasa_efectiva))