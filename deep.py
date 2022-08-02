import pandas

def abrir_plan_cuentas():
    df = pandas.read_excel('input/plan_cuentas_concretus.xlsx')
    return df

def nuevo_ambiente():
    df = abrir_plan_cuentas()
    df['cu_codigo'] = df['cu_codigo'].astype(str)
    FORMAT = ['cu_codigo', 'cu_nombre', 'cu_nivel', 'cu_cuenta_padre']
    result = df[FORMAT].set_index('cu_codigo')
    result['cu_cuenta_padre'] = result['cu_cuenta_padre'].astype(str)
    return result

def cargar_saldos_sabana(ambiente: pandas.DataFrame, filename: str):
    df = pandas.read_excel(filename)
    columna_codigo_cuenta = df.keys()[0]
    df[columna_codigo_cuenta] = df[columna_codigo_cuenta].astype(str)
    df = df.set_index(columna_codigo_cuenta)
    resultado = ambiente.copy()
    new_column_name = df.keys()[0]
    resultado[new_column_name] = 0
    for index_codigo_cuenta, row in df.iterrows():
        saldo = row[new_column_name]
        # resultado.at[index_codigo_cuenta, new_column_name] = saldo
        if (index_codigo_cuenta in resultado.index):
            actualizar_monto_recursivamente(resultado, index_codigo_cuenta, new_column_name, saldo)
        else:
            print ('Código no consta en el plan de cuentas', index_codigo_cuenta)
    return resultado

def actualizar_monto_recursivamente(resultado, codigo_cuenta, columna_montos, nuevo_saldo):
    monto_actual = resultado.at[codigo_cuenta, columna_montos]
    resultado.at[codigo_cuenta, columna_montos] = monto_actual + nuevo_saldo
    codigo_cuenta_padre = resultado.at[codigo_cuenta, 'cu_cuenta_padre']
    if ((codigo_cuenta_padre != '0') & (codigo_cuenta_padre != '')):
        actualizar_monto_recursivamente(resultado, codigo_cuenta_padre, columna_montos, nuevo_saldo)
