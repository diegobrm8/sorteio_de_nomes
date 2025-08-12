class Paciente:

    def __init__(self, nome, idade, sexo, cpf, telefone):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.telefone = telefone

    def exibir_info(self):
        print(
            f'Nome: {self.nome}, Idade:{self.idade}, Sexo:{self.sexo}, cpf:{self.cpf}, Telefone:{self.telefone}')


class Cadastro_paciente:
    def __init__(self):
        self.pacientes = []

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)
        print(f'paciente {paciente.nome} cadastrado com sucesso!')

    def buscar_paciente_por_CPF(self, cpf):
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                return paciente
        return None

    def listar_pacientes(self):
        cabecalho = '\033[32mPacientes Cadastrados:\033[m'
        print(cabecalho.center(50, ' '))
        for paciente in self.pacientes:
            paciente.exibir_info()


if __name__ == "__main__":
    cadastro = Cadastro_paciente()

    paciente1 = Paciente("Maria", 30, "M", "12345678901", "123-456-7890")
    paciente2 = Paciente("Jane", 25, "F", "98765432101", "987-654-3210")

    cadastro.adicionar_paciente(paciente1)
    cadastro.adicionar_paciente(paciente2)

    cadastro.listar_pacientes()

    paciente_busca = cadastro.buscar_paciente_por_CPF("12345678901")
    if paciente_busca:
        print("\nInformações do paciente buscado:")
        paciente_busca.exibir_info()
    else:
        print("\nPaciente não encontrado.")
