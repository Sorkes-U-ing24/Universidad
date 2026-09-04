# Cesar Gonzalez Ochoa
# AL07322002
# 04/09/2026
# Tabla pitagorica

# El rpograma se encarga de mostrar primeramente una tabla pitagorica atraves de una funcion en la que la desarolla a traves de una matriz
# sin que esta este definida previamente, para despues con una segunda funcion con return mostrar el valor de la tabla pitagorica buscando 
# en la  primera funcion el valor correspondiente sin usar operadores de (*)

#Creacion de tabla

tabla=[]
for i in range(1,11):
    fila=[]
    for j in range(1,11):
        fila.append(i*j)
    tabla.append(fila)
    
#Primera funcion
def imprimir_tabla(lgk):
    print("\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t")
    print("_"*83)
    for i in range(len(lgk)):
        print(f"{i+1} |\t", end="")
        for j in range(len(lgk[i])):
            print(f"{lgk[i][j]}", end="\t")
        print("")           
imprimir_tabla(tabla)

