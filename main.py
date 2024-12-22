# from sql.queries import Database


# # Exemplo de uso da classe Database
# db = Database()
# result = db.teste()
# for row in result:
#     print(row)
# db.close()


class AlgumaCoisa:
    def __enter__(self):
        print('Entrou no with')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print('Saiu do with')
        return True
    
with AlgumaCoisa() as ac:
    print('Dentro do with')