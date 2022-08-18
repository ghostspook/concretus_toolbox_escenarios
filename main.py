import deep

ambiente = deep.nuevo_ambiente('input/plan_cuentas_concretus.xlsx')

if deep.validar_arbol(ambiente):
    print("Árbol OK")
    # root = deep.obtener_arbol(ambiente)
    # deep.imprimir_arbol(ambiente, root)


ambiente = deep.cargar_escenario(ambiente, 'input/SAENZ RONQUILLO_NOVIEMBRE_2021.xlsx')
# deep.validar_escenario(ambiente, 'SAENZ RONQUILLO_NOVIEMBRE_2021', imprimir=True)

ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ_NOVIEMBRE_2021 (delta).xlsx')
# deep.validar_escenario(ambiente, 'SAENZ_OCTUBRE_2021 (delta)', imprimir=True)

ambiente = deep.computar_reverso_acumulado(ambiente, 'SAENZ RONQUILLO_NOVIEMBRE_2021', 'SAENZ_NOVIEMBRE_2021 (delta)', 'SAENZ_OCTUBRE_2021')
# deep.validar_escenario(ambiente, 'SAENZ_NOVIEMBRE_2021', imprimir=True)

ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ_OCTUBRE_2021 (delta).xlsx')
# deep.validar_escenario(ambiente, 'SAENZ_OCTUBRE_2021 (delta)', imprimir=True)

ambiente = deep.computar_reverso_acumulado(ambiente, 'SAENZ_OCTUBRE_2021', 'SAENZ_OCTUBRE_2021 (delta)', 'SAENZ_SEPTIEMBRE_2021')
# deep.validar_escenario(ambiente, 'SAENZ_SEPTIEMBRE_2021', imprimir=True)

ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ_SEPTIEMBRE_2021 (delta).xlsx')
# deep.validar_escenario(ambiente, 'SAENZ_SEPTIEMBRE_2021 (delta)', imprimir=True)

ambiente = deep.computar_reverso_acumulado(ambiente, 'SAENZ_SEPTIEMBRE_2021', 'SAENZ_SEPTIEMBRE_2021 (delta)', 'SAENZ_AGOSTO_2021')
# deep.validar_escenario(ambiente, 'SAENZ_SEPTIEMBRE_2021', imprimir=True)

ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ_AGOSTO_2021 (delta).xlsx')
# deep.validar_escenario(ambiente, 'SAENZ_AGOSTO_2021 (delta)', imprimir=True)

ambiente = deep.computar_reverso_acumulado(ambiente, 'SAENZ_AGOSTO_2021', 'SAENZ_AGOSTO_2021 (delta)', 'SAENZ_JULIO_2021')
# deep.validar_escenario(ambiente, 'SAENZ_JULIO_2021', imprimir=True)

ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ_JULIO_2021 (delta).xlsx')
# deep.validar_escenario(ambiente, 'SAENZ_AGOSTO_2021 (delta)', imprimir=True)

ambiente = deep.computar_reverso_acumulado(ambiente, 'SAENZ_JULIO_2021', 'SAENZ_JULIO_2021 (delta)', 'SAENZ_JUNIO_2021')
# deep.validar_escenario(ambiente, 'SAENZ_JUNIO_2021', imprimir=True)

ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ_JUNIO_2021 (delta).xlsx')
# deep.validar_escenario(ambiente, 'SAENZ_AGOSTO_2021 (delta)', imprimir=True)

ambiente = deep.computar_reverso_acumulado(ambiente, 'SAENZ_JUNIO_2021', 'SAENZ_JUNIO_2021 (delta)', 'SAENZ_MAYO_2021')
# deep.validar_escenario(ambiente, 'SAENZ_JUNIO_2021', imprimir=True)

ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ_MAYO_2021 (delta).xlsx')
# deep.validar_escenario(ambiente, 'SAENZ_MAYO_2021 (delta)', imprimir=True)

ambiente = deep.computar_reverso_acumulado(ambiente, 'SAENZ_MAYO_2021', 'SAENZ_MAYO_2021 (delta)', 'SAENZ_ABRIL_2021')
# deep.validar_escenario(ambiente, 'SAENZ_ABRIL_2021', imprimir=True)

ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ_ABRIL_2021 (delta).xlsx')
# deep.validar_escenario(ambiente, 'SAENZ_MAYO_2021 (delta)', imprimir=True)

ambiente = deep.computar_reverso_acumulado(ambiente, 'SAENZ_ABRIL_2021', 'SAENZ_ABRIL_2021 (delta)', 'SAENZ_MARZO_2021')
# deep.validar_escenario(ambiente, 'SAENZ_ABRIL_2021', imprimir=True)

ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ_MARZO_2021 (delta).xlsx')
# deep.validar_escenario(ambiente, 'SAENZ_MAYO_2021 (delta)', imprimir=True)

ambiente = deep.computar_reverso_acumulado(ambiente, 'SAENZ_MARZO_2021', 'SAENZ_MARZO_2021 (delta)', 'SAENZ_FEBRERO_2021')
# deep.validar_escenario(ambiente, 'SAENZ_ABRIL_2021', imprimir=True)

ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ_FEBRERO_2021 (delta).xlsx')
# deep.validar_escenario(ambiente, 'SAENZ_MAYO_2021 (delta)', imprimir=True)

ambiente = deep.computar_reverso_acumulado(ambiente, 'SAENZ_FEBRERO_2021', 'SAENZ_FEBRERO_2021 (delta)', 'SAENZ_ENERO_2021')
# deep.validar_escenario(ambiente, 'SAENZ_ENERO_2021', imprimir=True)

# Diciembre 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ_DICIEMBRE_2021 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'SAENZ RONQUILLO_NOVIEMBRE_2021', 'SAENZ_DICIEMBRE_2021 (delta)', 'SAENZ_DICIEMBRE_2021')

# Enero 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ_ENERO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'SAENZ_DICIEMBRE_2021', 'SAENZ_ENERO_2022 (delta)', 'SAENZ_ENERO_2022', acumular_resultados_ejercicio_anterior=True)
# deep.validar_escenario(ambiente, 'SAENZ_ENERO_2022', imprimir=True)

# Febrero 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ_FEBRERO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'SAENZ_ENERO_2022', 'SAENZ_FEBRERO_2022 (delta)', 'SAENZ_FEBRERO_2022')

# Marzo 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ_MARZO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'SAENZ_FEBRERO_2022', 'SAENZ_MARZO_2022 (delta)', 'SAENZ_MARZO_2022')

# Abril 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ_ABRIL_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'SAENZ_MARZO_2022', 'SAENZ_ABRIL_2022 (delta)', 'SAENZ_ABRIL_2022')

# Mayo 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ_MAYO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'SAENZ_ABRIL_2022', 'SAENZ_MAYO_2022 (delta)', 'SAENZ_MAYO_2022')
deep.validar_escenario(ambiente, 'SAENZ_MAYO_2022', imprimir=True)

ambiente.to_excel("output/SAENZ_2021_2022.xlsx")
