import deep

ambiente = deep.nuevo_ambiente('input/plan_cuentas_concretus.xlsx')

if deep.validar_arbol(ambiente):
    print("Árbol OK")
    # root = deep.obtener_arbol(ambiente)
    # deep.imprimir_arbol(ambiente, root)


ambiente = deep.cargar_escenario(ambiente, 'input/CONSORCIO APP MILAGRO_NOVIEMBRE_2021.xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO APP MILAGRO_NOVIEMBRE_2021', imprimir=True)

ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO APP MILAGRO_DICIEMBRE_2021 (neto movimientos).xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO APP MILAGRO_DICIEMBRE_2021 (neto movimientos)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO APP MILAGRO_NOVIEMBRE_2021', 'CONSORCIO APP MILAGRO_DICIEMBRE_2021 (neto movimientos)', 'CONSORCIO APP MILAGRO_DICIEMBRE_2021')
deep.validar_escenario(ambiente, 'CONSORCIO APP MILAGRO_DICIEMBRE_2021', imprimir=True)

# ambiente = deep.minimizar(ambiente)
# ambiente.to_excel("output/CONSORCIO APP MILAGRO_2021.xlsx")


# ----------------- 2022 -------------------



import deep

ambiente = deep.nuevo_ambiente('input/plan_cuentas_concretus.xlsx')

if deep.validar_arbol(ambiente):
    print("Árbol OK")
    # root = deep.obtener_arbol(ambiente)
    # deep.imprimir_arbol(ambiente, root)

# Parte de diciembre 2021
ambiente = deep.cargar_escenario(ambiente, 'input/CONSORCIO APP MILAGRO_DICIEMBRE_2021.xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO APP MILAGRO_DICIEMBRE_2021', imprimir=True)

# Enero 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO APP MILAGRO_ENERO_2022 (delta).xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO APP MILAGRO_ENERO_2022 (delta)', imprimir=True)
#
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO APP MILAGRO_DICIEMBRE_2021', 'CONSORCIO APP MILAGRO_ENERO_2022 (delta)', 'CONSORCIO APP MILAGRO_ENERO_2022', acumular_resultados_ejercicio_anterior=True)
# deep.validar_escenario(ambiente, 'CONSORCIO APP MILAGRO_ENERO_2022', imprimir=True)

# Febrero 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO APP MILAGRO_FEBRERO_2022 (delta).xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO APP MILAGRO_FEBRERO_2022 (delta)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO APP MILAGRO_ENERO_2022', 'CONSORCIO APP MILAGRO_FEBRERO_2022 (delta)', 'CONSORCIO APP MILAGRO_FEBRERO_2022')
# deep.validar_escenario(ambiente, 'CONSORCIO APP MILAGRO_FEBRERO_2022', imprimir=True)
#
# # Marzo 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO APP MILAGRO_MARZO_2022 (delta).xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO APP MILAGRO_MARZO_2022 (delta)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO APP MILAGRO_FEBRERO_2022', 'CONSORCIO APP MILAGRO_MARZO_2022 (delta)', 'CONSORCIO APP MILAGRO_MARZO_2022')
# deep.validar_escenario(ambiente, 'CONSORCIO APP MILAGRO_MARZO_2022', imprimir=True)

# Abril 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO APP MILAGRO_ABRIL_2022 (delta).xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO APP MILAGRO_ABRIL_2022 (delta)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO APP MILAGRO_MARZO_2022', 'CONSORCIO APP MILAGRO_ABRIL_2022 (delta)', 'CONSORCIO APP MILAGRO_ABRIL_2022')
# deep.validar_escenario(ambiente, 'CONSORCIO APP MILAGRO_ABRIL_2022', imprimir=True)

# Mayo 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO APP MILAGRO_MAYO_2022 (delta).xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO APP MILAGRO_MAYO_2022 (delta)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO APP MILAGRO_ABRIL_2022', 'CONSORCIO APP MILAGRO_MAYO_2022 (delta)', 'CONSORCIO APP MILAGRO_MAYO_2022')
deep.validar_escenario(ambiente, 'CONSORCIO APP MILAGRO_MAYO_2022', imprimir=True)
# #
# ambiente = deep.minimizar(ambiente)
# ambiente.to_excel("output/CONSORCIO APP MILAGRO_2022.xlsx")