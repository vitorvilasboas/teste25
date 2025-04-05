class Funcionario:
    def __init__(self, nome, idade, cargo, salario, departamento, mae):
        Funcionario.setor = "CORES"
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario
        self.departamento = departamento
        self.nome_da_mae = mae

# Instanciando um objeto da classe Funcionario
func1 = Funcionario(
    nome="João Silva",
    idade=30,
    cargo="Analista de Sistemas",
    salario=5000.00,
    departamento="TI"
    mae="Maria Silva"
)

func2 = Funcionario(
    nome="Noriosmenilson",
    idade=5,
    cargo="Oreia Seca",
    salario=311.00,
    departamento="Biblioteca"    
    mae="Joelma do Ximbinha"
)

# Exibindo três atributos do objeto
print(f"Nome: {funcionario.nome}")
print(f"Idade: {funcionario.idade}")
print(f"Cargo: {funcionario.cargo}")