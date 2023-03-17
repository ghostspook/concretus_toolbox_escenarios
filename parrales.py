import deep

ambiente = deep.nuevo_ambiente('input/plan_cuentas_concretus.xlsx')

if deep.validar_arbol(ambiente):
    print("Árbol OK")
    # root = deep.obtener_arbol(ambiente)
    # deep.imprimir_arbol(ambiente, root)


ambiente = deep.cargar_escenario(ambiente, 'input/NARCISA PARRALES_NOVIEMBRE_2021.xlsx')
# deep.validar_escenario(ambiente, 'NARCISA PARRALES_NOVIEMBRE_2021', imprimir=True)

ambiente = deep.cargar_netos_movimientos(ambiente, 'input/NARCISA PARRALES_DICIEMBRE_2021 (neto movimientos).xlsx')
# deep.validar_escenario(ambiente, 'NARCISA PARRALES_DICIEMBRE_2021 (neto movimientos)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'NARCISA PARRALES_NOVIEMBRE_2021', 'NARCISA PARRALES_DICIEMBRE_2021 (neto movimientos)', 'NARCISA PARRALES_DICIEMBRE_2021')
deep.validar_escenario(ambiente, 'NARCISA PARRALES_DICIEMBRE_2021', imprimir=True)

# ambiente = deep.minimizar(ambiente)
# ambiente.to_excel("output/NARCISA PARRALES_DICIEMBRE_2021.xlsx")
# print(ambiente['SAENZ RONQUILLO_DICIEMBRE_2021'])



# ----------------- 2022 -------------------


import deep

ambiente = deep.nuevo_ambiente('input/plan_cuentas_concretus.xlsx')

if deep.validar_arbol(ambiente):
    print("Árbol OK")
    # root = deep.obtener_arbol(ambiente)
    # deep.imprimir_arbol(ambiente, root)

# Parte de diciembre 2021
ambiente = deep.cargar_escenario(ambiente, 'input/NARCISA PARRALES_DICIEMBRE_2021.xlsx')
# deep.validar_escenario(ambiente, 'NARCISA PARRALES_DICIEMBRE_2021', imprimir=True)

# Enero 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/NARCISA PARRALES_ENERO_2022 (delta).xlsx')
ambiente.at['2105010101', 'NARCISA PARRALES_ENERO_2022 (delta)'] -= 12.83 # Ajuste requerido por error en movimiento
# deep.validar_escenario(ambiente, 'NARCISA PARRALES_ENERO_2022 (delta)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'NARCISA PARRALES_DICIEMBRE_2021', 'NARCISA PARRALES_ENERO_2022 (delta)', 'NARCISA PARRALES_ENERO_2022', acumular_resultados_ejercicio_anterior=True)
# deep.validar_escenario(ambiente, 'NARCISA PARRALES_ENERO_2022', imprimir=True)

# Febrero 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/NARCISA PARRALES_FEBRERO_2022 (delta).xlsx')
# deep.validar_escenario(ambiente, 'NARCISA PARRALES_FEBRERO_2022 (delta)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'NARCISA PARRALES_ENERO_2022', 'NARCISA PARRALES_FEBRERO_2022 (delta)', 'NARCISA PARRALES_FEBRERO_2022')
# deep.validar_escenario(ambiente, 'NARCISA PARRALES_FEBRERO_2022', imprimir=True)

# Marzo 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/NARCISA PARRALES_MARZO_2022 (delta).xlsx')
# deep.validar_escenario(ambiente, 'NARCISA PARRALES_MARZO_2022 (delta)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'NARCISA PARRALES_FEBRERO_2022', 'NARCISA PARRALES_MARZO_2022 (delta)', 'NARCISA PARRALES_MARZO_2022')
# deep.validar_escenario(ambiente, 'NARCISA PARRALES_MARZO_2022', imprimir=True)

# Abril 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/NARCISA PARRALES_ABRIL_2022 (delta).xlsx')
# deep.validar_escenario(ambiente, 'NARCISA PARRALES_ABRIL_2022 (delta)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'NARCISA PARRALES_MARZO_2022', 'NARCISA PARRALES_ABRIL_2022 (delta)', 'NARCISA PARRALES_ABRIL_2022')
# deep.validar_escenario(ambiente, 'NARCISA PARRALES_ABRIL_2022', imprimir=True)

# Mayo 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/NARCISA PARRALES_MAYO_2022 (delta).xlsx')
# deep.validar_escenario(ambiente, 'NARCISA PARRALES_MAYO_2022 (delta)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'NARCISA PARRALES_ABRIL_2022', 'NARCISA PARRALES_MAYO_2022 (delta)', 'NARCISA PARRALES_MAYO_2022')
deep.validar_escenario(ambiente, 'NARCISA PARRALES_MAYO_2022', imprimir=True)
#
# ambiente = deep.minimizar(ambiente)
# ambiente.to_excel("output/NARCISA PARRALES_2022.xlsx")