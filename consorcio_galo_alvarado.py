import deep

ambiente = deep.nuevo_ambiente('input/plan_cuentas_concretus.xlsx')

# deep.imprimir_arbol(ambiente)
if deep.validar_arbol(ambiente):
    print("Árbol OK")

# NOVIEMBRE 2021
ambiente = deep.cargar_escenario(ambiente, 'input/CONSORCIO GALO ALVARADO_NOVIEMBRE_2021.xlsx')
ambiente = deep.cambiar_signo(ambiente, 'CONSORCIO GALO ALVARADO_NOVIEMBRE_2021', '2')
ambiente = deep.cambiar_signo(ambiente, 'CONSORCIO GALO ALVARADO_NOVIEMBRE_2021', '3')
ambiente = deep.cambiar_signo(ambiente, 'CONSORCIO GALO ALVARADO_NOVIEMBRE_2021', '5')

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

deep.validar_escenario(ambiente, 'CONSORCIO GALO ALVARADO_DICIEMBRE_2021', imprimir=True)

ambiente = deep.minimizar(ambiente)
ambiente.to_excel("output/tmp_CONSORCIO GALO ALVARADO_SEP_2021_DIC_2021.xlsx")
