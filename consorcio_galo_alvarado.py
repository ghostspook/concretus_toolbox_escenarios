import deep

ambiente = deep.nuevo_ambiente('input/plan_cuentas_concretus.xlsx')

deep.imprimir_arbol(ambiente)
if deep.validar_arbol(ambiente):
    print("Árbol OK")

# NOVIEMBRE 2021
ambiente = deep.cargar_escenario(ambiente, 'input/CONSORCIO GALO ALVARADO_NOVIEMBRE_2021.xlsx')

# OCTUBRE 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_NOVIEMBRE_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_NOVIEMBRE_2021', 'CONSORCIO GALO ALVARADO_NOVIEMBRE_2021 (delta)', 'CONSORCIO GALO ALVARADO_OCTUBRE_2021')

# SEPTIEMBRE 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_OCTUBRE_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_OCTUBRE_2021', 'CONSORCIO GALO ALVARADO_OCTUBRE_2021 (delta)', 'CONSORCIO GALO ALVARADO_SEPTIEMBRE_2021')

# AGOSTO 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_SEPTIEMBRE_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_SEPTIEMBRE_2021', 'CONSORCIO GALO ALVARADO_SEPTIEMBRE_2021 (delta)', 'CONSORCIO GALO ALVARADO_AGOSTO_2021')

# Diciembre 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_DICIEMBRE_2021 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_NOVIEMBRE_2021', 'CONSORCIO GALO ALVARADO_DICIEMBRE_2021 (delta)', 'CONSORCIO GALO ALVARADO_DICIEMBRE_2021')

# Enero 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_ENERO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_DICIEMBRE_2021', 'CONSORCIO GALO ALVARADO_ENERO_2022 (delta)', 'CONSORCIO GALO ALVARADO_ENERO_2022', acumular_resultados_ejercicio_anterior=True)

# Febrero 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_FEBRERO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_ENERO_2022', 'CONSORCIO GALO ALVARADO_FEBRERO_2022 (delta)', 'CONSORCIO GALO ALVARADO_FEBRERO_2022')

# Marzo 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_MARZO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_FEBRERO_2022', 'CONSORCIO GALO ALVARADO_MARZO_2022 (delta)', 'CONSORCIO GALO ALVARADO_MARZO_2022')

# Abril 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_ABRIL_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_MARZO_2022', 'CONSORCIO GALO ALVARADO_ABRIL_2022 (delta)', 'CONSORCIO GALO ALVARADO_ABRIL_2022')

# Mayo 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_MAYO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_ABRIL_2022', 'CONSORCIO GALO ALVARADO_MAYO_2022 (delta)', 'CONSORCIO GALO ALVARADO_MAYO_2022')

# Junio 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_JUNIO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_MAYO_2022', 'CONSORCIO GALO ALVARADO_JUNIO_2022 (delta)', 'CONSORCIO GALO ALVARADO_JUNIO_2022')

# Julio 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO GALO ALVARADO_JULIO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO GALO ALVARADO_JUNIO_2022', 'CONSORCIO GALO ALVARADO_JULIO_2022 (delta)', 'CONSORCIO GALO ALVARADO_JULIO_2022')

deep.validar_escenario(ambiente, 'CONSORCIO GALO ALVARADO_JULIO_2022', imprimir=True)

ambiente = deep.minimizar(ambiente)
ambiente.to_excel("output/CONSORCIO GALO ALVARADO_SEP_2021_JUL_2022.xlsx")
