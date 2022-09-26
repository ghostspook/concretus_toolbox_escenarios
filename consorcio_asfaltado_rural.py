import deep

ambiente = deep.nuevo_ambiente('input/plan_cuentas_concretus.xlsx')

deep.imprimir_arbol(ambiente)
if deep.validar_arbol(ambiente):
    print("Árbol OK")

# Vacío
ambiente = deep.cargar_escenario(ambiente, 'input/CONSORCIO ASFALTADO RURAL_VACIO.xlsx')

# Enero 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO ASFALTADO RURAL_ENERO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO ASFALTADO RURAL_VACIO', 'CONSORCIO ASFALTADO RURAL_ENERO_2022 (delta)', 'CONSORCIO ASFALTADO RURAL_ENERO_2022', acumular_resultados_ejercicio_anterior=True)

# Febrero 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO ASFALTADO RURAL_FEBRERO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO ASFALTADO RURAL_ENERO_2022', 'CONSORCIO ASFALTADO RURAL_FEBRERO_2022 (delta)', 'CONSORCIO ASFALTADO RURAL_FEBRERO_2022')

# Marzo 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO ASFALTADO RURAL_MARZO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO ASFALTADO RURAL_FEBRERO_2022', 'CONSORCIO ASFALTADO RURAL_MARZO_2022 (delta)', 'CONSORCIO ASFALTADO RURAL_MARZO_2022')

# Abril 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO ASFALTADO RURAL_ABRIL_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO ASFALTADO RURAL_MARZO_2022', 'CONSORCIO ASFALTADO RURAL_ABRIL_2022 (delta)', 'CONSORCIO ASFALTADO RURAL_ABRIL_2022')

# Mayo 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO ASFALTADO RURAL_MAYO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO ASFALTADO RURAL_ABRIL_2022', 'CONSORCIO ASFALTADO RURAL_MAYO_2022 (delta)', 'CONSORCIO ASFALTADO RURAL_MAYO_2022')

# Junio 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO ASFALTADO RURAL_JUNIO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO ASFALTADO RURAL_MAYO_2022', 'CONSORCIO ASFALTADO RURAL_JUNIO_2022 (delta)', 'CONSORCIO ASFALTADO RURAL_JUNIO_2022')

# Julio 2022
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO ASFALTADO RURAL_JULIO_2022 (delta).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO ASFALTADO RURAL_JUNIO_2022', 'CONSORCIO ASFALTADO RURAL_JULIO_2022 (delta)', 'CONSORCIO ASFALTADO RURAL_JULIO_2022')

deep.validar_escenario(ambiente, 'CONSORCIO ASFALTADO RURAL_JULIO_2022', imprimir=True)

ambiente = deep.minimizar(ambiente)
ambiente.to_excel("output/CONSORCIO ASFALTADO RURAL_ENE_2022_JUL_2022.xlsx")
