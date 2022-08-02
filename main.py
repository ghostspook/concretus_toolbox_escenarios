import deep

ambiente = deep.nuevo_ambiente()

ambiente = deep.cargar_escenario(ambiente, 'input/SAENZ RONQUILLO_NOVIEMBRE_2021.xlsx')
ambiente = deep.cargar_netos_movimientos(ambiente, 'input/SAENZ RONQUILLO_DICIEMBRE_2021_(netos_movimientos).xlsx')
ambiente = deep.computar_acumulado(ambiente, 'SAENZ RONQUILLO_NOVIEMBRE_2021', 'SAENZ RONQUILLO_DICIEMBRE_2021 (netos movimientos)', 'SAENZ RONQUILLO_DICIEMBRE_2021')

ambiente.to_excel("output/ambiente.xlsx")
# print(ambiente['SAENZ RONQUILLO_DICIEMBRE_2021'])
