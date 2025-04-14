def line():
	A = float(input("Ingrese el coeficiente A:"))
	B = float(input("Ingrese el coeficiente de B:"))
	X1 = float(input("Ingrese el coeficiente de X1:"))
	X2 = float(input("Ingrese el coeficiente de X2:"))
	print(f"El coeficiente A de su ecuación de la recta es: {A}")
	print(f"El coeficiente B de su ecuación de la recta es: {B}")
	print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
	print(f"El coeficiente X2 de su ecuación de la recta es: {X2}")
	print("\nPara la siguiente ecuación:")
	print(f"\tY = {A}X + {B}")
	print(f"\nDados los siguientes puntos:")
	Y1 = A*X1+B
	Y2 = A*X2+B
	print(f"\tP1 ({X1}, {Y1})")
	print(f"\tP2 ({X2}, {Y2})")
	distancia = ((X1-X2)**2 + (Y1 - Y2)**2)**(1/2)
	print(f"\nLa distancia entre ellos es: {distancia}")
