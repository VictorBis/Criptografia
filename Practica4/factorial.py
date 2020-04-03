def factorial(n):
	
	'''
    Calcula el factorial de un numero
    Se calcula el factorial reduciendo la multiplicacion en factoriales a la mitad

    Para mas informacion acerca del algoritmo, consultar:
    https://sites.google.com/site/examath/research/factorials
	'''
	if n == 1 or n == 0:
		return 1

	is_odd = False
	upto_n = n
	
	if n & 1 == 1:
		upto_n -= 1
		is_odd = True

	next_sum = upto_n
	next_multi = upto_n
	factorial = 1
	
	while next_sum >= 2:
		factorial *= next_multi
		next_sum -= 2
		next_multi += next_sum

	if is_odd:
		factorial *= n

	return factorial
