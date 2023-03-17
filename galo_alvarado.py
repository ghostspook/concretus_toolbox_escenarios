import deep

ambiente = deep.nuevo_ambiente('input/plan_cuentas_concretus.xlsx')

if deep.validar_arbol(ambiente):
    print("Árbol OK\n")
    # root = deep.obtener_arbol(ambiente)
    # deep.imprimir_arbol(ambiente, root)


ambiente = deep.cargar_escenario(ambiente, 'input/CONSORCIO GALO ALVARADO_NOVIEMBRE_2021.xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO GALO ALVARADO_NOVIEMBRE_2021', imprimir=True)

ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_DICIEMBRE_2021 (neto movimientos).xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO GALO ALVARADO_DICIEMBRE_2021 (neto movimientos)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_NOVIEMBRE_2021', 'CONSORCIO GALO ALVARADO_DICIEMBRE_2021 (neto movimientos)', 'CONSORCIO GALO ALVARADO_DICIEMBRE_2021')
deep.validar_escenario(ambiente, 'CONSORCIO GALO ALVARADO_DICIEMBRE_2021', imprimir=True)

# ambiente = deep.minimizar(ambiente)
# ambiente.to_excel("output/CONSORCIO GALO ALVARADO_DICIEMBRE_2021.xlsx")



# ----------------- 2022 -------------------



import deep

ambiente = deep.nuevo_ambiente('input/plan_cuentas_concretus.xlsx')

# if deep.validar_arbol(ambiente):
#     print("Árbol OK")
#     # root = deep.obtener_arbol(ambiente)
#     # deep.imprimir_arbol(ambiente, root)

# Parte de diciembre 2021
ambiente = deep.cargar_escenario(ambiente, 'input/CONSORCIO GALO ALVARADO_DICIEMBRE_2021.xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO GALO ALVARADO_DICIEMBRE_2021', imprimir=True)

# Enero 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_ENERO_2022 (delta).xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO GALO ALVARADO_ENERO_2022 (delta)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_DICIEMBRE_2021', 'CONSORCIO GALO ALVARADO_ENERO_2022 (delta)', 'CONSORCIO GALO ALVARADO_ENERO_2022', acumular_resultados_ejercicio_anterior=True)
# deep.validar_escenario(ambiente, 'CONSORCIO GALO ALVARADO_ENERO_2022', imprimir=True)

# Febrero 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_FEBRERO_2022 (delta).xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO GALO ALVARADO_FEBRERO_2022 (delta)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_ENERO_2022', 'CONSORCIO GALO ALVARADO_FEBRERO_2022 (delta)', 'CONSORCIO GALO ALVARADO_FEBRERO_2022')
# deep.validar_escenario(ambiente, 'CONSORCIO GALO ALVARADO_FEBRERO_2022', imprimir=True)
#
# # Marzo 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_MARZO_2022 (delta).xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO GALO ALVARADO_MARZO_2022 (delta)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_FEBRERO_2022', 'CONSORCIO GALO ALVARADO_MARZO_2022 (delta)', 'CONSORCIO GALO ALVARADO_MARZO_2022')
# deep.validar_escenario(ambiente, 'CONSORCIO GALO ALVARADO_MARZO_2022', imprimir=True)

# Abril 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_ABRIL_2022 (delta).xlsx')
deep.validar_escenario(ambiente, 'CONSORCIO GALO ALVARADO_ABRIL_2022 (delta)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_MARZO_2022', 'CONSORCIO GALO ALVARADO_ABRIL_2022 (delta)', 'CONSORCIO GALO ALVARADO_ABRIL_2022')
# deep.validar_escenario(ambiente, 'CONSORCIO GALO ALVARADO_ABRIL_2022', imprimir=True)

# Mayo 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_MAYO_2022 (delta).xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO GALO ALVARADO_MAYO_2022 (delta)', imprimir=True)
#
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_ABRIL_2022', 'CONSORCIO GALO ALVARADO_MAYO_2022 (delta)', 'CONSORCIO GALO ALVARADO_MAYO_2022')
deep.validar_escenario(ambiente, 'CONSORCIO GALO ALVARADO_MAYO_2022', imprimir=True)

# ambiente = deep.minimizar(ambiente)
# ambiente.to_excel("output/CONSORCIO GALO ALVARADO_2022.xlsx")