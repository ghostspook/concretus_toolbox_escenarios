import deep

ambiente = deep.nuevo_ambiente()

ambiente = deep.cargar_saldos_sabana(ambiente, 'input/SAENZ RONQUILLO_DICIEMBRE_2021.xlsx')
ambiente.to_excel("output/ambiente.xlsx")
# print(ambiente['SAENZ RONQUILLO_DICIEMBRE_2021'])
