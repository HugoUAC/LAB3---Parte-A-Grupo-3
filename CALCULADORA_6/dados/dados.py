import threading
import time
class Dados:
    def __init__(self):
        self.operacoes = {}
        self.lock = threading.Lock()
    def registar_oper(self, oper: str, a: int, b: int, result: int, client: tuple, timestamp: float = None):
        if timestamp is None:
            timestamp = time.time()
        registo = [a, b, result, client, timestamp]
        with self.lock:
            if oper not in self.operacoes:
                self.operacoes[oper] = []
            self.operacoes[oper].append(registo)
    
        print(self.operacoes)