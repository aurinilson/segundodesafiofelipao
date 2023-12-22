class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "usou um ataque genérico"

        mensagem = f"O {self.tipo} atacou usando {ataque}"
        print(mensagem)


# Exemplo de uso
heroi_mago = Heroi(nome="Merlin", idade=100, tipo="mago")
heroi_mago.atacar()

heroi_guerreiro = Heroi(nome="Conan", idade=30, tipo="guerreiro")
heroi_guerreiro.atacar()