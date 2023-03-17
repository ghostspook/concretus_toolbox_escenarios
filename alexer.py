import deep

ambiente = deep.nuevo_ambiente('input/plan_cuentas_concretus.xlsx')

if deep.validar_arbol(ambiente):
    print("Árbol OK\n")
    # root = deep.obtener_arbol(ambiente)
    # deep.imprimir_arbol(ambiente, root)


ambiente = deep.cargar_escenario(ambiente, 'input/ALEXER_NOVIEMBRE_2021.xlsx')
deep.validar_escenario(ambiente, 'ALEXER_NOVIEMBRE_2021', imprimir=True)

# ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CARLOS PENA_DICIEMBRE_2021 (neto movimientos).xlsx')
# deep.validar_escenario(ambiente, 'CARLOS PENA_DICIEMBRE_2021 (neto movimientos)', imprimir=True)

# ambiente = deep.computar_acumulado(ambiente, 'CARLOS PENA_NOVIEMBRE_2021', 'CARLOS PENA_DICIEMBRE_2021 (neto movimientos)', 'CARLOS PENA_DICIEMBRE_2021')
# deep.validar_escenario(ambiente, 'CARLOS PENA_DICIEMBRE_2021', imprimir=True)

ambiente = deep.minimizar(ambiente)
ambiente.to_excel("output/ALEXER_NOVIEMBRE_2021.xlsx")
