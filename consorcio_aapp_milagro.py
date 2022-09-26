import deep

ambiente = deep.nuevo_ambiente('input/plan_cuentas_concretus.xlsx')

deep.imprimir_arbol(ambiente)
if deep.validar_arbol(ambiente):
    print("Árbol OK")

# NOVIEMBRE 2021
ambiente = deep.cargar_escenario(ambiente, 'input/CONSORCIO AAPP MILAGRO_NOVIEMBRE_2021.xlsx')

# OCTUBRE 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO AAPP MILAGRO_NOVIEMBRE_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO AAPP MILAGRO_NOVIEMBRE_2021', 'CONSORCIO AAPP MILAGRO_NOVIEMBRE_2021 (delta)', 'CONSORCIO AAPP MILAGRO_OCTUBRE_2021')

# SEPTIEMBRE 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO AAPP MILAGRO_OCTUBRE_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO AAPP MILAGRO_OCTUBRE_2021', 'CONSORCIO AAPP MILAGRO_OCTUBRE_2021 (delta)', 'CONSORCIO AAPP MILAGRO_SEPTIEMBRE_2021')

# AGOSTO 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO AAPP MILAGRO_SEPTIEMBRE_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO AAPP MILAGRO_SEPTIEMBRE_2021', 'CONSORCIO AAPP MILAGRO_SEPTIEMBRE_2021 (delta)', 'CONSORCIO AAPP MILAGRO_AGOSTO_2021')

# JULIO 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO AAPP MILAGRO_AGOSTO_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO AAPP MILAGRO_AGOSTO_2021', 'CONSORCIO AAPP MILAGRO_AGOSTO_2021 (delta)', 'CONSORCIO AAPP MILAGRO_JULIO_2021')

# JUNIO 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO AAPP MILAGRO_JULIO_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO AAPP MILAGRO_JULIO_2021', 'CONSORCIO AAPP MILAGRO_JULIO_2021 (delta)', 'CONSORCIO AAPP MILAGRO_JUNIO_2021')

# MAYO 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO AAPP MILAGRO_JUNIO_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO AAPP MILAGRO_JUNIO_2021', 'CONSORCIO AAPP MILAGRO_JUNIO_2021 (delta)', 'CONSORCIO AAPP MILAGRO_MAYO_2021')

# Diciembre 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO AAPP MILAGRO_DICIEMBRE_2021 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO AAPP MILAGRO_NOVIEMBRE_2021', 'CONSORCIO AAPP MILAGRO_DICIEMBRE_2021 (delta)', 'CONSORCIO AAPP MILAGRO_DICIEMBRE_2021')

# Enero 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO AAPP MILAGRO_ENERO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO AAPP MILAGRO_DICIEMBRE_2021', 'CONSORCIO AAPP MILAGRO_ENERO_2022 (delta)', 'CONSORCIO AAPP MILAGRO_ENERO_2022', acumular_resultados_ejercicio_anterior=True)

# Febrero 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO AAPP MILAGRO_FEBRERO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO AAPP MILAGRO_ENERO_2022', 'CONSORCIO AAPP MILAGRO_FEBRERO_2022 (delta)', 'CONSORCIO AAPP MILAGRO_FEBRERO_2022')

# Marzo 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO AAPP MILAGRO_MARZO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO AAPP MILAGRO_FEBRERO_2022', 'CONSORCIO AAPP MILAGRO_MARZO_2022 (delta)', 'CONSORCIO AAPP MILAGRO_MARZO_2022')

# Abril 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO AAPP MILAGRO_ABRIL_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO AAPP MILAGRO_MARZO_2022', 'CONSORCIO AAPP MILAGRO_ABRIL_2022 (delta)', 'CONSORCIO AAPP MILAGRO_ABRIL_2022')

# Mayo 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO AAPP MILAGRO_MAYO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO AAPP MILAGRO_ABRIL_2022', 'CONSORCIO AAPP MILAGRO_MAYO_2022 (delta)', 'CONSORCIO AAPP MILAGRO_MAYO_2022')

# Junio 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO AAPP MILAGRO_JUNIO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO AAPP MILAGRO_MAYO_2022', 'CONSORCIO AAPP MILAGRO_JUNIO_2022 (delta)', 'CONSORCIO AAPP MILAGRO_JUNIO_2022')

# Julio 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO AAPP MILAGRO_JULIO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO AAPP MILAGRO_JUNIO_2022', 'CONSORCIO AAPP MILAGRO_JULIO_2022 (delta)', 'CONSORCIO AAPP MILAGRO_JULIO_2022')

deep.validar_escenario(ambiente, 'CONSORCIO AAPP MILAGRO_JULIO_2022', imprimir=True)

# ambiente = deep.minimizar(ambiente)
# ambiente.to_excel("output/CONSORCIO AAPP MILAGRO_JUN_2021_JUL_2022.xlsx")
