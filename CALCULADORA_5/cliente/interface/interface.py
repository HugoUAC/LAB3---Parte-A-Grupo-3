import socket
import json
import cliente
# PORT e SERVER ADDRESS

class Interface:
	#def __init__(self, maq:object):
	def __init__(self):
		#self.m:object = maq
		self.connection = socket.socket()
		self.connection.connect((cliente.SERVER_ADDRESS,cliente.PORT))

###
	# ----- enviar e receber strings ----- #
	def receive_str(self,connect, n_bytes: int) -> str:
		"""
		:param n_bytes: The number of bytes to read from the current connection
		:return: The next string read from the current connection
		"""
		data = connect.recv(n_bytes)
		return data.decode()

	def send_str(self,connect, value: str) -> None:

		connect.send(value.encode())

	def send_int(self,connect:socket.socket, value: int, n_bytes: int) -> None:

		connect.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

	def receive_int(self,connect: socket.socket, n_bytes: int) -> int:

		data = connect.recv(n_bytes)
		return int.from_bytes(data, byteorder='big', signed=True)


	#TODO
	# Implement a method that sends and object and returns an object.
	# ...
	def send_object(self,connection, obj):
		"""1º: envia tamanho, 2º: envia dados."""
		data = json.dumps(obj).encode('utf-8')
		size = len(data)
		self.send_int(connection, size, cliente.INT_SIZE)         # Envio do tamanho
		connection.send(data)              		# Envio do objeto

	def receive_object(self,connection):
		"""1º: lê tamanho, 2º: lê dados."""
		size = self.receive_int(connection, cliente.INT_SIZE)  	# Recebe o tamanho
		data = connection.recv(size)       			# Recebe o objeto
		return json.loads(data.decode('utf-8'))
	###


	def execute(self):
		res = ""
		while res!="0":
			print("Qual é o cálculo que quer efetuar? + - ")
			print("Sair: 0")
			res:str = input()
			print("Preciso que introduza dois valores:")
			x:int = int(input("x="))
			y:int = int(input("y="))

			#x:float = float(input("x="))
			#y:float = float(input("y="))
			if res =="+":
				self.send_str(self.connection,cliente.ADD_OP)
				self.send_int(self.connection,x, cliente.INT_SIZE)
				self.send_int(self.connection,y, cliente.INT_SIZE)
				res = self.receive_int(self.connection,cliente.INT_SIZE)
				print("O resultado da soma é:",res)

	#res = self.m.execute("+"+" "+str(x)+" "+str(y))
				#print("O valor da operação somar é:", res)
			# elif res =="/":
			# 	s:object = dividir.Dividir(x,y)
			# 	res = s.executar()
			# 	if type(res)==str:
			# 		print (res)
			# else:
			# 		print("O valor da operação divisão é:",res)
			#

			elif res =="-":
				self.send_str(self.connection,cliente.SUB_OP)
				self.send_int(self.connection,x, cliente.INT_SIZE)
				self.send_int(self.connection,y, cliente.INT_SIZE)
				res = self.receive_int(self.connection,cliente.INT_SIZE)
				print("O resultado da subtração é:",res)

			elif res =="-":
				self.send_str(self.connection,cliente.SUB_OP)
				self.send_int(self.connection,x, cliente.INT_SIZE)
				self.send_int(self.connection,y, cliente.INT_SIZE)
				res = self.receive_int(self.connection,cliente.INT_SIZE)
				print("O resultado da subtração é:",res)
