nombres = ['ana','juan','sara','gloria']
edades = [20,45,52,15]
combinados = list(zip(nombres, edades))
print(combinados)

for nombre, edad in combinados:
    print(f'{nombre} tiene {edad} años')
    