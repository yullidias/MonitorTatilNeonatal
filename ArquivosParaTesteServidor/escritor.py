from servidor import Servidor
import  datetime, time, random
import sys

if( not(len(sys.argv) == 5 or len(sys.argv) == 6)):
	print "use: python escritor ip porta pontos_por_segundo (arquivo | InicioRand FimRand)"
	sys.exit(0)

s = Servidor(sys.argv[1], sys.argv[2])
print "Executando ..."	
if(len(sys.argv) == 5):
	while True:
		arq = open(sys.argv[4], 'r')
		texto = arq.readlines()
		for linha in texto:
			s.enviar(linha)
			time.sleep(1/float(sys.argv[3]))
		arq.close	
else:
	while True:
		i = random.randint(int(sys.argv[4]), int(sys.argv[5]))
		s.enviar(str(i))
		time.sleep(1/float(sys.argv[3]))	
