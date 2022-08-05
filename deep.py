import pandas

def abrir_plan_cuentas():
    df = pandas.read_excel('input/plan_cuentas_concretus.xlsx')
    return df

def nuevo_ambiente():
    print ('Creando ambiente ...')

    df = abrir_plan_cuentas()
    df['cu_codigo'] = df['cu_codigo'].astype(str)
    FORMAT = ['cu_codigo', 'cu_nombre', 'cu_nivel', 'cu_cuenta_padre']
    result = df[FORMAT].set_index('cu_codigo')
    result['cu_cuenta_padre'] = result['cu_cuenta_padre'].astype(str)
    imprimir_columnas(result)
    return result

def cargar_escenario(ambiente: pandas.DataFrame, filename: str):
    print ('Cargando escenario ...')

    df = pandas.read_excel(filename)
    columna_codigo_cuenta = df.keys()[0]
    df[columna_codigo_cuenta] = df[columna_codigo_cuenta].astype(str)
    df = df.set_index(columna_codigo_cuenta)
    resultado = ambiente.copy()
    column_names = df.keys()
    new_column_name = column_names[len(column_names) - 1]
    resultado[new_column_name] = 0
    for index_codigo_cuenta, row in df.iterrows():
        monto = row[new_column_name]
        if (index_codigo_cuenta in resultado.index):
            resultado.at[index_codigo_cuenta, new_column_name] = monto
        else:
            print('Código no consta en el plan de cuentas', index_codigo_cuenta)
    imprimir_columnas(resultado)
    return resultado

def cargar_netos_movimientos(ambiente: pandas.DataFrame, filename: str):
    print ('Cargando montos netos de movimientos ...')

    df = pandas.read_excel(filename)
    columna_codigo_cuenta = df.keys()[0]
    df[columna_codigo_cuenta] = df[columna_codigo_cuenta].astype(str)
    df = df.set_index(columna_codigo_cuenta)
    resultado = ambiente.copy()
    new_column_name = df.keys()[0]
    resultado[new_column_name] = 0
    for index_codigo_cuenta, row in df.iterrows():
        saldo = row[new_column_name]
        # Validar saldo es un número
        try:
            a = int(saldo)
        except:
            saldo = 0
        # resultado.at[index_codigo_cuenta, new_column_name] = saldo
        if (index_codigo_cuenta in resultado.index):
            actualizar_monto_recursivamente(resultado, index_codigo_cuenta, new_column_name, saldo)
        else:
            print ('Código no consta en el plan de cuentas', index_codigo_cuenta, '. Monto: ', saldo)
    total_ingresos = resultado.at['4', new_column_name] # (-)
    total_gastos = resultado.at['5', new_column_name] # (+)
    utilidad = total_ingresos + total_gastos
    resultado.at['49', new_column_name] = utilidad
    actualizar_monto_recursivamente(resultado, '3701', new_column_name, utilidad)
    imprimir_columnas(resultado)
    return resultado

def actualizar_monto_recursivamente(resultado, codigo_cuenta, columna_montos, nuevo_saldo):
    monto_actual = resultado.at[codigo_cuenta, columna_montos]
    resultado.at[codigo_cuenta, columna_montos] = monto_actual + nuevo_saldo
    codigo_cuenta_padre = resultado.at[codigo_cuenta, 'cu_cuenta_padre']
    if ((codigo_cuenta_padre != '0') & (codigo_cuenta_padre != '')):
        actualizar_monto_recursivamente(resultado, codigo_cuenta_padre, columna_montos, nuevo_saldo)

def computar_acumulado(ambiente: pandas.DataFrame, columna_escenario_inicial: str, columna_neto_movimientos: str, columna_resultado: str):
    print ('Calculando resultado acumulado ...')

    resultado = ambiente.copy()
    resultado[columna_resultado] = 0
    for index_codigo_cuenta, row in resultado.iterrows():
        valor_escenario_inicial = row[columna_escenario_inicial]
        neto_movimientos = row[columna_neto_movimientos]
        if ((index_codigo_cuenta[0] == '4') | (index_codigo_cuenta[0] == '5')):
            resultado.at[index_codigo_cuenta, columna_resultado] = valor_escenario_inicial - neto_movimientos
        else:
            resultado.at[index_codigo_cuenta, columna_resultado] = valor_escenario_inicial + neto_movimientos
    imprimir_columnas(resultado)
    return resultado
def imprimir_columnas(df: pandas.DataFrame):
    print("Columnas:")
    for col in df.columns:
        print('- ', col)
    print("\n")