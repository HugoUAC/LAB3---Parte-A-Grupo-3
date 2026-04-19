from dados.dados import Dados
from servidor.maquina.processa_cliente import ProcessaCliente
from servidor.operacoes.somar import Somar
from servidor.operacoes.dividir import Dividir
import servidor
import json
import socket

class Maquina:
	def __init__(self):
		self.sum = Somar()
		self.div = Dividir()
		self.dados = Dados()
		self.s = socket.socket()
		self.s.bind(('', servidor.PORT))

	# ---------------------- interaction with sockets ------------------------------
	def receive_int(self,connection, n_bytes: int) -> int:
		"""
		:param n_bytes: The number of bytes to read from the current connection
		:return: The next integer read from the current connection
		"""
		data = connection.recv(n_bytes)
		return int.from_bytes(data, byteorder='big', signed=True)

	def send_int(self,connection, value: int, n_bytes: int) -> None:
		"""
		:param value: The integer value to be sent to the current connection
		:param n_bytes: The number of bytes to send
		"""
		connection.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

	def receive_str(self,connection, n_bytes: int) -> str:
		"""
		:param n_bytes: The number of bytes to read from the current connection
		:return: The next string read from the current connection
		"""
		data = connection.recv(n_bytes)
		return data.decode()

	def send_str(self,connection, value: str) -> None:
		"""
		:param value: The string value to send to the current connection
		"""
		connection.connection.send(value.encode())

	#TODO
	# Implement a method that sends and object and returns an object.
	# ...
	def send_object(self,connection, obj):
		"""1º: envia tamanho, 2º: envia dados."""
		data = json.dumps(obj).encode('utf-8')
		size = len(data)
		self.send_int(connection, size, servidor.INT_SIZE)         # Envio do tamanho
		connection.send(data)              		     # Envio do objeto

	def receive_object(self,connection):
		"""1º: lê tamanho, 2º: lê dados."""
		size = self.receive_int(connection, servidor.INT_SIZE)  	# Recebe o tamanho
		data = connection.recv(size)       			# Recebe o objeto
		return json.loads(data.decode('utf-8'))


	# def __init__(cliente.interface.Interface:object interface):
	# 	self.interface:object = interface
	# 	self.somar:object  = servidor.operacoes.somar.Somar()
	# 	self.dividir:object = servidor.operacoes.dividir.Dividir()
	# def exec():
	# 	res = self.interface.exec()
    # 		if res =="+":
    #     	s:object = somar.Somar(x,y)
    #     	res = s.executar(x,y)
    #     	interacao.resultado(res)
    #     print("O valor da operação somar é:", res)
    # elif res =="/":
    #     s:object = dividir.Dividir(x,y)
    #     res = s.executar()
    #     if type(res)==str:
    #         print (res)
    #     else:
    #         print("O valor da operação divisão é:",res)

	#def execute(self,command:str):
	def execute(self):
		self.s.listen(5)
		print("Waiting for clients on port " + str(servidor.PORT))
		try:
			while True:
				print("On accept...")
				connection, address = self.s.accept()
				print("Client " + str(address) + " connected")
				ProcessaCliente(connection, address, self.dados).start()
		except KeyboardInterrupt:
			print("Stopping...")
		finally:
			self.s.close()
			print("Server stopped")

#c = command.split()
		# Get the operator
	#	if c[0] =="+":
			#Call operator
	#		res = self.sum.execute(float(c[1]),float(c[2]))
	#	return res