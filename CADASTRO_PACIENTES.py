class Paciente:
    def __init__(self, nome, sexo, idade, telefone):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.telefone = telefone

    def exibir_info(self):
        print(f'Nome: {self.nome}, Sexo: {self.sexo}, Idade: {self.idade}, Telefone: {self.telefone}')


class CadastroPacientes:
    def __init__(self):
        self.pacientes = []

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)
        print(f'Paciente {paciente.nome} adicionado com sucesso.')

    def buscar_paciente_por_cpf(self, cpf):
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                return paciente
        return None

    def listar_pacientes(self):
        if not self.pacientes:
            print('Não há pacientes cadastrados.')
        else:
            for paciente in self.pacientes:
                paciente.exibir_info()


cadastro_pacientes = CadastroPacientes()

paciente1 = Paciente('João', 'M', 35, '123456789')
paciente2 = Paciente('Maria', 'F', 28, '987654321')
cadastro_pacientes.adicionar_paciente(paciente1)
cadastro_pacientes.adicionar_paciente(paciente2)
cadastro_pacientes.listar_pacientes()