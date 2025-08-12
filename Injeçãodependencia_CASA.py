class Casa:  
    def __init__(self) -> None:
        self._endereço = 'rua dos Limoeiros'
        
    
    def acender_luzes(self) -> None:
        print('Estou Ascendendo as Luses')
        
    def get_endereco(self) -> str:
        return self._endereço
    

class Pessoa:
    
    def __init__(self, nome: str, local: any) -> None:
        self._local = local
        self._nome = nome  
        
    def entrar_no_local(self) -> None:
        self._local.acender_luzes()
        
    def apresentar_local(self) -> None:
        endereco = self._local.get_endereco()
        print(endereco)
        
        
casa_fulano = Casa()
ana = Pessoa('Ana', casa_fulano)
    
ana.entrar_no_local()
ana.apresentar_local()

