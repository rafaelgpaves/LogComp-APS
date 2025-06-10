class SymbolTable:
    def __init__(self):
        self.st = {}
        self.parent_st = None

    def create(self, chave, tipo):
        if chave in self.st:
            raise Exception(f"Variável \"{chave}\" já declarada")
        if tipo == "int":
            self.st[chave] = (tipo, 0, False)
        elif tipo == "bool":
            self.st[chave] = (tipo, False, False)
        self.st[chave] = (tipo, "", False)

    def getter(self, chave):
        st = self.st
        valor = st.get(chave)
        if valor is not None:
            return valor
        elif self.parent_st is not None:
            return self.parent_st.getter(chave)

        raise Exception(f"Variável \"{chave}\" não declarada")

    def setter(self, chave, valor):
        st = self.st
        if chave in st:
            if valor[0] != st[chave][0]:
                raise Exception(f"Variável \"{chave}\" possui tipo {st[chave][0]}; tipo recebido: {valor[0]}")
            st[chave] = (valor[0], valor[1], valor[2])
            return
        elif self.parent_st is not None:
            self.parent_st.setter(chave, valor)
            return
        raise Exception(f"Variável \"{chave}\" não declarada")
    