# Código ruim
class Relatorio:
    def gravar_relatorio(self):
        print("Gerando um relátorio...")
    def enviar_email(self):
        print("Enviando e-mail...")

 # Código bom ( Fácil interpretação)   
class GeradorRelatorio:
    def gravar_relatorio(self):
        print("Gerando um relátorio...")

class EnviadorEmail:       
    def enviar_email(self):
        print("Enviando e-mail...")   
