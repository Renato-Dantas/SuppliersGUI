import sqlite3
import os
os.remove('supplier.db') if os.path.exists('supplier.db') else None

#Criando o banco de dados

conector = sqlite3.connect('supplier.db')
cursor = conector.cursor()

create_tab = 'CREATE TABLE supplier'\
'({} INTEGER, '\
'{} VARCHAR NOT NULL, '\
'{} VARCHAR NOT NULL, '\
'{} TEXT NOT NULL, '\
'{} VARCHAR, '\
'{} INTEGER NOT NULL, '\
'{} INTEGER, '\
'{} TEXT NOT NULL)'.format('id', 'name','area','city','email','phone1', 'phone2','link')

cursor.execute(create_tab)
insert = 'INSERT INTO supplier VALUES("000001","Renato","Ballistic","Hortolandia-SP","renatodantas@outlook.com.br",19984152347,38457644,"https://renato-dantas.medium.com/")'

cursor.execute(insert)

conector.commit()

cursor.execute('SELECT * FROM supplier')
data = cursor.fetchall()



for linha in data:
    print(linha)

conector.close()