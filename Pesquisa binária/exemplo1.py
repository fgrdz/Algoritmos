class PesquisaBinaria():

    def pesquisa_binaria(self, lista, item):
        baixo = 0 
        alto = len(lista) - 1

        while baixo <= alto:
            meio = (baixo + alto) // 2
            chute = lista[meio]
            # Found the item.
            if chute == item:
                return meio
            # The guess was too high.
            if chute > item:
                alto = meio - 1
            # The guess was too low.
            else:
                baixo = meio + 1

            # Item doesn't exist
        return None
    
if __name__ == "__main__":
    bs = PesquisaBinaria()
    my_list = [1, 3, 5, 7, 9, 11]

    print(bs.pesquisa_binaria(my_list, 3))
    print (bs.pesquisa_binaria(my_list, -1))
