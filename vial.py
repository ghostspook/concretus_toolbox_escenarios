import deep

ambiente = deep.nuevo_ambiente('input/plan_cuentas_concretus.xlsx')

if deep.validar_arbol(ambiente):
    print("Árbol OK\n")
    # root = deep.obtener_arbol(ambiente)
    # deep.imprimir_arbol(ambiente, root)


ambiente = deep.cargar_escenario(ambiente, 'input/CONSORCIO VIAL_NOVIEMBRE_2021.xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO VIAL_NOVIEMBRE_2021', imprimir=True)

ambiente = deep.cargar_netos_movimientos(ambiente, 'input/CONSORCIO VIAL_DICIEMBRE_2021 (delta).xlsx')
# deep.validar_escenario(ambiente, 'CONSORCIO VIAL_DICIEMBRE_2021 (delta)', imprimir=True)

ambiente = deep.computar_acumulado(ambiente, 'CONSORCIO VIAL_NOVIEMBRE_2021', 'CONSORCIO VIAL_DICIEMBRE_2021 (delta)', 'CONSORCIO VIAL_DICIEMBRE_2021')
deep.validar_escenario(ambiente, 'CONSORCIO VIAL_DICIEMBRE_2021', imprimir=True)

# ambiente = deep.minimizar(ambiente)
# ambiente.to_excel("output/CONSORCIO VIAL_2021.xlsx")