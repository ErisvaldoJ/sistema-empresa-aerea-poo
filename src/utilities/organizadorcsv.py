import csv

class OrganizadorCSV:
    """Classe para organizar as informações em arquivos CSV.
    Atributos:
        arquivo_passageiros (str): nome do arquivo CSV de passageiros
        arquivo_reservas (str): nome do arquivo CSV de reservas
        arquivo_voos (str): nome do arquivo CSV de voos
    
        O nome dos arquivos são definidos no construtor, e podem ser alterados
        """
    def __init__(self):
        self.arquivo_passageiros = "passageiros.csv"
        self.arquivo_reservas = "reservas.csv"
        self.arquivo_voos = "voos.csv"

    def salvarPassageiro(self, passageiro):
        """Salva informações do passageiro em um arquivo CSV.
            Recebe um objeto de Passageiro como parâmetro."""
        with open(self.arquivo_passageiros, mode='a', newline='', encoding='utf-8') as file:
            cabecalhos = ['nome', 'cpf', 'telefone']
            escrever_csv = csv.DictWriter(file, fieldnames=cabecalhos)

            if file.tell() == 0:  # escreve o cabeçalho se o arquivo estiver vazio
                escrever_csv.writeheader()

            escrever_csv.writerow({'nome': passageiro.nome, 'cpf': passageiro.get_cpf(), 'telefone': passageiro.telefone})

    def carregarPassageiros(self):
        """Carrega informações de passageiros do arquivo CSV.
            Retorna uma lista de dicionários com as informações do csv."""
        passageiros = []
        try:
            with open(self.arquivo_passageiros, mode='r', encoding='utf-8') as file:
                ler_csv = csv.DictReader(file)
                for coluna in ler_csv:
                    passageiros.append({
                        'nome': coluna['nome'],
                        'cpf': coluna['cpf'],
                        'telefone': coluna['telefone']
                    })
        except FileNotFoundError:
            pass
        return passageiros

    def salvarReservaPassageiro(self, reserva):
        """Salva informações da reserva em um arquivo CSV.
            Recebe um objeto de Reserva como parâmetro.
            As verificações para o assento e voo devem ser feitas no menu."""
        with open(self.arquivo_reservas, mode='a', newline='', encoding='utf-8') as file:
            cabecalhos = ['cpf', 'voo', 'assento']
            escrever_csv = csv.DictWriter(file, fieldnames=cabecalhos)

            if file.tell() == 0:  # escreve o cabeçalho se o arquivo estiver vazio
                escrever_csv.writeheader()

            escrever_csv.writerow({
                'cpf': reserva.get_passageiro()['cpf'], # agora pega o cpf pela chave nao pelo metodo
                'voo': reserva.get_voo(),
                'assento': reserva.get_assento()
            })

    def carregarReservas(self):
        """Carrega informações de reservas do arquivo CSV.
            Retorna uma lista de dicionários com as informações do csv."""
        reservas = []
        try:
            with open(self.arquivo_reservas, mode='r', encoding='utf-8') as file:
                ler_csv = csv.DictReader(file)
                for coluna in ler_csv:
                    reservas.append({
                        'cpf': coluna['cpf'],
                        'voo': coluna['voo'],
                        'assento': int(coluna['assento'])
                    })
        except FileNotFoundError:
            pass
        return reservas

    def removerReserva(self, assento):
        """Remove uma reserva com base no ID (assento) do arquivo CSV.
            Retorna True se a reserva foi removida e False caso contrário
            assim podemos usar um if para verificar se a reserva foi removida.
            O ID agora é o assento."""
        reservas = []
        removida = False
        try:
            with open(self.arquivo_reservas, mode='r', encoding='utf-8') as file:
                ler_csv = csv.DictReader(file)
                cabecalhos = ler_csv.fieldnames
                for coluna in ler_csv:
                    if coluna['assento'] != str(assento):
                        reservas.append(coluna) 
                    else:
                        removida = True

            with open(self.arquivo_reservas, mode='w', newline='') as file:
                ler_csv = csv.DictWriter(file, fieldnames=cabecalhos)
                ler_csv.writeheader()
                ler_csv.writerows(reservas)

            return removida
        except FileNotFoundError:
            pass  

    def removerPassageiro(self, cpf):
        """Remove um passageiro com base no CPF do arquivo CSV.
            Não possui retorno, apenas remove o passageiro do arquivo CSV."""
        passageiros = []
        with open(self.arquivo_passageiros, mode='r', encoding='utf-8') as file:
            ler_csv = csv.DictReader(file)
            cabecalhos = ler_csv.fieldnames
            for row in ler_csv:
                if row['cpf'] != cpf:
                    passageiros.append(row)

        with open(self.arquivo_passageiros, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=cabecalhos)
            writer.writeheader()
            writer.writerows(passageiros)

    def salvarVoo(self, voo):
        """Salva informações do voo em um arquivo CSV.
            Recebe um objeto de Voo como parâmetro."""
        with open(self.arquivo_voos, mode='a', newline='', encoding='utf-8') as file:
            cabecalhos = ['codigo', 'tipo', 'data', 'partida', 'destino', 'aviao', 'assentosTotais']
            escrever_csv = csv.DictWriter(file, fieldnames=cabecalhos)

            if file.tell() == 0:
                escrever_csv.writeheader()

            escrever_csv.writerow({
                'codigo': voo.get_codigoVoo(),
                'tipo': voo.get_tipoVoo(),
                'data': voo.get_data(),
                'partida': voo.get_partida(),
                'destino': voo.get_destino(),
                'aviao': voo.get_aviao(),
                'assentosTotais': voo.get_assentos()
            })
    
    def carregarVoos(self):
        """Carrega informações de voos do arquivo CSV.
            Retorna uma lista de dicionários com as informações do csv."""
        voos = []
        try:
            with open(self.arquivo_voos, mode='r', encoding='utf-8') as file:
                ler_csv = csv.DictReader(file)
                for coluna in ler_csv:
                    voos.append({
                        'codigo': coluna['codigo'],
                        'tipo': coluna['tipo'],
                        'data': coluna['data'],
                        'partida': coluna['partida'],
                        'destino': coluna['destino'],
                        'aviao': coluna['aviao'],
                        'assentosTotais': coluna['assentosTotais']
                    })
        except FileNotFoundError:
            pass
        return voos
    
    def obterVooPorCodigo(self, codigo):
        """Carrega informações de um voo específico do arquivo CSV.
            Se encontrar o voo, retorna ele."""
        voos = self.carregarVoos()
        for voo in voos:
            if voo['codigo'] == codigo:
                return voo
        return None