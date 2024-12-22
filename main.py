from sql.queries import Database


# Exemplo de uso da classe Database
db = Database()
result = db.teste()
for row in result:
    print(row)
db.close()