import sqlite3

def selectAllData():
    connector = sqlite3.connect('supplier.db')
    cursor = connector.cursor()
    cursor.execute('SELECT * FROM supplier')

    data = cursor.fetchall()
    connector.close()
    return data

def insertSqlValue(sup_id, name,area, city, email, phone1, phone2, link):
    connector = sqlite3.connect('supplier.db')
    cursor = connector.cursor()
    supplier = [sup_id,name, area, city, email, phone1, phone2, link]
    insert = 'INSERT INTO supplier VALUES (?,?,?,?,?,?,?,?)'
    cursor.execute(insert, supplier)
    connector.commit()
    connector.close()

def searchSqlArea(area):
    connector = sqlite3.connect('supplier.db')
    cursor = connector.cursor()

    select = 'SELECT * FROM supplier WHERE area = ?'
    cursor.execute(select, [area])
    data = cursor.fetchall()
    connector.close()
    return data

def searchSqlName(name):
    connector = sqlite3.connect('supplier.db')
    cursor = connector.cursor()

    select = 'SELECT id,name,area,city,email,phone1,phone2,link FROM supplier WHERE name = ?'
    cursor.execute(select, [name])
    data = cursor.fetchall()
    connector.close()
    return data

def deleteSupplier(name):
    connector = sqlite3.connect('supplier.db')
    cursor = connector.cursor()

    delete = "DELETE FROM supplier WHERE name = ?"
    cursor.execute(delete,[name])
    connector.commit()
    connector.close()

def searchListNames():
    connector = sqlite3.connect('supplier.db')
    cursor = connector.cursor() 

    search = "SELECT name FROM supplier"
    cursor.execute(search)
    names = cursor.fetchall()
    connector.close()
    return names

def searchListAreas():
    connector = sqlite3.connect('supplier.db')
    cursor = connector.cursor() 

    search = "SELECT area FROM supplier"
    cursor.execute(search)
    areas = cursor.fetchall()
    connector.close()
    return areas

def createAreaList(areas):
    areaList = []
    for area in areas:
        area = list(area)
        areaList.append(area[0])
    return areaList

def createNameList(names):
    nameList = []
    for name in names:
        name = list(name)
        nameList.append(name[0])
    return nameList

def updateData(data):
    connector = sqlite3.connect('supplier.db')
    cursor = connector.cursor()

    update = 'UPDATE supplier SET id = ?, name = ?, area = ?, city = ?, email = ?, phone1 = ?, phone2 = ?, link = ? WHERE name = ?'
    cursor.execute(update, data)
    data = cursor.fetchall()
    connector.commit()
    connector.close()

def sampleTest():
    connector = sqlite3.connect('supplier.db')
    cursor = connector.cursor()

    # sup_id,name, area, city, email, phone1, phone2, link
    supplier = [['001', 'Renato','TI', 'Hortolandia-SP','renato@gmail.com','19984754626', '1938457644', 'www.link.com'],['002', 'Cristiane','Logistica', 'Hortolandia-SP','Cris@gmail.com','19984754626', '1938457644', 'www.link.com'],['003', 'Emilly','TI', 'Hortolandia-SP','Emilly@gmail.com','19984754626', '1938457644', 'www.link.com']]
    insert = 'INSERT INTO supplier VALUES (?,?,?,?,?,?,?,?)'

    for i in supplier:
        cursor.execute(insert, i)
        connector.commit()
    connector.close()

def delete():
    connector = sqlite3.connect('supplier.db')
    cursor = connector.cursor()

    delete = "DELETE FROM supplier"
    cursor.execute(delete)
    connector.commit()
    connector.close()

def updateTestSamples():
    delete()
    sampleTest()
    data = selectAllData()
    print(data)

#updateTestSamples()