# Herramientas para generación de Escenarios

Conjunto de herramientas utilizadas para la generación de escenarios a partir de un escenario inicial y de "deltas"

# Funciones
## nuevo_ambiente
Carga un nuevo ambiente a partir de un plan de cuentas en EXCEL

## validar_arbol
Valida que el plan de cuentas del ambiente esté correcto:
1. Que no hayan "hojas sueltas" en el árbol. Es decir, que todas tengan hijos.
2. Que las "cuentas hijas" coincidan en su codificación con la del padre

## imprimir_arbol
Imprime el árbol del plan de cuentas

## cargar_escenario
Carga un escenario (no un delta) a partir de un archivo de EXCEL

## cambiar_signo
Permite cambiar el signo de todas las cuentas que empiecen con un número dado.
Por ejemplo, se puede cambiar el signo de todas las cuentas que empiecen con 5 (Costos y gastos).

## validar_escenario
Valida que el escenario cumpla con las siguientes condiciones:
1. Que se cumpla que **acitvo = pasivo + patrimonio**
2. Que coincidan los valores de las cuentas Utilidad y Resultados del Ejercicio
3. Que la suma de los montos en las cuentas hijas coincidan con el monto de las cuentas padre.

## cargar_netos_movimientos
A partir de un archivo de EXCEL, carga los netos de los movimientos y computa un delta que se añade al ambiente con el nombre especificado.

## computar_acumulado
Permite computar un escenario "hacia adelante" a partir de un escenario y un delta.
Por ejemplo computa **DICIEMBRE_2021** a partir de **NOVIEMBRE_2021** Y **DICIEMBRE_2021 (delta)**

## computar_reverso_acumulado
Permite computar un escenario "hacia atrás" a partir de un escenario y un delta.
Por ejemplo computa **OCTUBRE_2021** a partir de **NOVIEMBRE_2021** Y **NOVIEMBRE_2021 (delta)**

## minimizar
Elimina del ambiente todas las filas correspondientes a cuentas cuyos montos son iguales a 0 en todos los escenarios del ambiente.
Esta opción suele invocarse antes de guardar el ambiente en un archivo de EXCEL.

# Preguntas Frequentes
## ¿Qué es un escenario?
Un escenario está compuesto al menos de:
- Balance General
- Estado de Pérdidas y Ganancias

Para propósitos del proyecto CONCRETUS, cada escenario está asociado a una empresa, un año y un mes específicos.

## ¿Qué es un delta?
Se puede explicar el delta como la diferencia entre dos escenarios.
Por ejemplo, la diferencia entre el escenario "junio 2022" y "julio 2021" equivale al "julio 2022 (delta)".
Lo normal es obtener el delta a partir del auxiliar de movimientos. 

Las herramientas de este proyecto permiten "cargar" los montos netos sumarizados por cuenta obtenidos a partir del auxiliar de movimientos y generar así el delta correspondiente usando un algoritmo de recursividad hacia arriba en el árbol de cuentas.

## ¿Qué es un ambiente?
El ambiente consiste en una matriz. Es implementado utilizando un DataFrame.
El número de filas corresponde al número de cuentas del plan de cuentas.
La primera columna es el número de cuenta.
Las demás columnas representan, cada una, un escenario.
El encabezado de cada columna (excepto la primera) constituye el nombre del escenario.

Al ambiente se pueden añadir columnas en la forma de "deltas" o se puede computar nuevas columnas a partir de las columnas que ya existen.
Por ejemplo, a partir del escenario "noviembre 2021" se puede y del escenario "diciembre 2022 (delta)" se puede computar el escenario "diciembre 2022".