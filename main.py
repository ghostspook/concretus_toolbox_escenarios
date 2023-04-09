import deep

ambiente = deep.nuevo_ambiente('input/plan_cuentas_concretus.xlsx')

deep.validar_arbol(ambiente)

ambiente = deep.cargar_escenario(ambiente, 'input/ALEXER_JULIO_2022.xlsx')

ambiente = deep.cargar_multiples_netos(ambiente, 'input/ALEXER_DELTAS_DESDE_AGOSTO_2022.xlsx')

ambiente = deep.computar_acumulado(ambiente, 'ALEXER_JULIO_2022', 'ALEXER_AGOSTO_2022_DELTA', 'ALEXER_AGOSTO_2022')
ambiente = deep.computar_acumulado(ambiente, 'ALEXER_AGOSTO_2022', 'ALEXER_SEPTIEMBRE_2022_DELTA', 'ALEXER_SEPTIEMBRE_2022')
ambiente = deep.computar_acumulado(ambiente, 'ALEXER_SEPTIEMBRE_2022', 'ALEXER_OCTUBRE_2022_DELTA', 'ALEXER_OCTUBRE_2022')
ambiente = deep.computar_acumulado(ambiente, 'ALEXER_OCTUBRE_2022', 'ALEXER_NOVIEMBRE_2022_DELTA', 'ALEXER_NOVIEMBRE_2022')
ambiente = deep.computar_acumulado(ambiente, 'ALEXER_NOVIEMBRE_2022', 'ALEXER_DICIEMBRE_2022_DELTA', 'ALEXER_DICIEMBRE_2022')
ambiente = deep.computar_acumulado(ambiente, 'ALEXER_DICIEMBRE_2022', 'ALEXER_ENERO_2023_DELTA', 'ALEXER_ENERO_2023', acumular_resultados_ejercicio_anterior=True)

ambiente = deep.validar_escenario(ambiente, 'ALEXER_AGOSTO_2022_DELTA', imprimir=True)
#
# ambiente.to_excel("output/ALEXER.xlsx")