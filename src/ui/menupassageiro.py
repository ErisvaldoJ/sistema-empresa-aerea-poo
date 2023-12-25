from voo.voo import Voo
from voo.passageiro import Passageiro
from voo.reserva import Reserva
from utilities.organizadorcsv import OrganizadorCSV

class MenuPassageiro:
    def __init__(self, organizador, nome, cpf, telefone):
        self.organizador = organizador
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def exibir_menu(self):
        while True:
            print("\n1. Ver voos disponíveis")
            print("2. Fazer uma reserva")
            print("3. Ver suas reservas")
            print("4. Cancelar uma reserva")
            print("5. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.visualizar_voos()
            elif escolha == '2':
                self.fazer_reserva()
            elif escolha == '3':
                self.visualizar_reservas()
            elif escolha == '4':
                self.cancelar_reserva()
            elif escolha == '5':
                break
            else:
                print("Opção inválida. Tente novamente.")

    def visualizar_voos(self):
        voos = self.organizador.carregarVoos()
        if voos:
            print("\nVoos disponíveis:")
            for voo in voos:
                print(f"Código: {voo['codigo']}, Tipo: {voo['tipo']}, Data: {voo['data']}, Partida: {voo['partida']}, Destino: {voo['destino']}, Avião: {voo['aviao']}, Assentos: {voo['assentosTotais']}")
        else:
            print(f"Não há voos disponíveis.")

    def fazer_reserva(self):
        cpf = self.cpf
        voo_codigo = input("Digite o código do voo: ")
        voo_info = self.organizador.obterVooPorCodigo(voo_codigo)
        passageiros = self.organizador.carregarPassageiros()
        passageiro_encontrado = next((passageiro for passageiro in passageiros if passageiro['cpf'] == cpf), None)
        if passageiro_encontrado and voo_info:
            voo = Voo(voo_info['codigo'], voo_info['tipo'], voo_info['data'], voo_info['partida'], voo_info['destino'], voo_info['aviao'], voo_info['assentosTotais'])
            reserva = Reserva(passageiro_encontrado, voo)
            self.organizador.salvarReservaPassageiro(reserva)
            print(f"Reserva para o voo {voo_codigo} cadastrada com sucesso.")
        elif not voo_info:
            print(f"Voo {voo_codigo} não encontrado.")
        else:
            print(f"Não foi possível realizar a reserva.")

    def visualizar_reservas(self):
        cpf = self.cpf
        reservas = self.organizador.carregarReservas()
        if any(reserva['cpf'] == cpf for reserva in reservas):
            print("\nReservas:")
            for reserva in reservas:
                if reserva['cpf'] == cpf:
                    print(f"Codigo do voo: {reserva['voo']}, ID: {reserva['id']}")
        else:
            print(f"Você não possui reservas.")

    def cancelar_reserva(self):
        # consertar erro de não cancelar reserva
        cpf = self.cpf
        reservas = self.organizador.carregarReservas()
        if any(reserva['cpf'] == cpf for reserva in reservas):
            id_reserva = input("Digite o ID da reserva: ")
            for reserva in reservas.copy():
                if reserva['cpf'] == cpf and reserva['id'] == id_reserva:
                    reservas.remove(reserva)
                    self.organizador.salvarReservas(reservas)
                    print(f"Reserva {id_reserva} cancelada com sucesso.")
                    break
            else:
                print(f"Reserva {id_reserva} não encontrada.")
        else:
            print(f"Você não possui reservas.")