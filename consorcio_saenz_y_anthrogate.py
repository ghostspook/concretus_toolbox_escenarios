import deep

ambiente = deep.nuevo_ambiente('input/plan_cuentas_concretus.xlsx')

deep.imprimir_arbol(ambiente)
if deep.validar_arbol(ambiente):
    print("Árbol OK")

# NOVIEMBRE 2021
ambiente = deep.cargar_escenario(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_NOVIEMBRE_2021.xlsx')

# OCTUBRE 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_NOVIEMBRE_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_NOVIEMBRE_2021', 'CONSORCIO SAENZ Y ANTHROGATE_NOVIEMBRE_2021 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_OCTUBRE_2021')

# SEPTIEMBRE 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_OCTUBRE_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_OCTUBRE_2021', 'CONSORCIO SAENZ Y ANTHROGATE_OCTUBRE_2021 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_SEPTIEMBRE_2021')

# AGOSTO 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_SEPTIEMBRE_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_SEPTIEMBRE_2021', 'CONSORCIO SAENZ Y ANTHROGATE_SEPTIEMBRE_2021 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_AGOSTO_2021')

# JULIO 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_AGOSTO_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_AGOSTO_2021', 'CONSORCIO SAENZ Y ANTHROGATE_AGOSTO_2021 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_JULIO_2021')

# JUNIO 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_JULIO_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_JULIO_2021', 'CONSORCIO SAENZ Y ANTHROGATE_JULIO_2021 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_JUNIO_2021')

# MAYO 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_JUNIO_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_JUNIO_2021', 'CONSORCIO SAENZ Y ANTHROGATE_JUNIO_2021 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_MAYO_2021')

# ABRIL 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_MAYO_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_MAYO_2021', 'CONSORCIO SAENZ Y ANTHROGATE_MAYO_2021 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_ABRIL_2021')

# MARZO 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_ABRIL_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_ABRIL_2021', 'CONSORCIO SAENZ Y ANTHROGATE_ABRIL_2021 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_MARZO_2021')

# FEBRERO 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_MARZO_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_MARZO_2021', 'CONSORCIO SAENZ Y ANTHROGATE_MARZO_2021 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_FEBRERO_2021')

# ENERO 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_FEBRERO_2021 (delta).xlsx')
ambiente = deep.computar_reverso_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_FEBRERO_2021', 'CONSORCIO SAENZ Y ANTHROGATE_FEBRERO_2021 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_ENERO_2021')

# Diciembre 2021
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_DICIEMBRE_2021 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_NOVIEMBRE_2021', 'CONSORCIO SAENZ Y ANTHROGATE_DICIEMBRE_2021 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_DICIEMBRE_2021')

# Enero 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_ENERO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_DICIEMBRE_2021', 'CONSORCIO SAENZ Y ANTHROGATE_ENERO_2022 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_ENERO_2022', acumular_resultados_ejercicio_anterior=True)

# Febrero 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_FEBRERO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_ENERO_2022', 'CONSORCIO SAENZ Y ANTHROGATE_FEBRERO_2022 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_FEBRERO_2022')

# Marzo 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_MARZO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_FEBRERO_2022', 'CONSORCIO SAENZ Y ANTHROGATE_MARZO_2022 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_MARZO_2022')

# Abril 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_ABRIL_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_MARZO_2022', 'CONSORCIO SAENZ Y ANTHROGATE_ABRIL_2022 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_ABRIL_2022')

# Mayo 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_MAYO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_ABRIL_2022', 'CONSORCIO SAENZ Y ANTHROGATE_MAYO_2022 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_MAYO_2022')

# Junio 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_JUNIO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_MAYO_2022', 'CONSORCIO SAENZ Y ANTHROGATE_JUNIO_2022 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_JUNIO_2022')

# Julio 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO SAENZ Y ANTHROGATE_JULIO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_JUNIO_2022', 'CONSORCIO SAENZ Y ANTHROGATE_JULIO_2022 (delta)', 'CONSORCIO SAENZ Y ANTHROGATE_JULIO_2022')

deep.validar_escenario(ambiente, 'CONSORCIO SAENZ Y ANTHROGATE_JULIO_2022', imprimir=True)

ambiente = deep.minimizar(ambiente)
ambiente.to_excel("output/CONSORCIO SAENZ Y ANTHROGATE_ENE_2021_JUL_2022.xlsx")
