from tinydb import TinyDB, Query



def insertDB(db):
    # creating default game catalogue with just game name and genre
    db.insert({'name':'Call of Duty','genre':'Action','price':'100'})

def browseCatalogue(db):

    #read from db and print output to terminal
    query = Query()
    Catalogue = db.search(query.name == 'Call of Duty')

    print("Game Name:",Catalogue[0]['name'])
    print("Game genre:", Catalogue[0]['genre'])
    print("Game Price:", Catalogue[0]['price']) 

if __name__ == '__main__':
    db = TinyDB('catalogue.json')
    insertDB(db)
    browseCatalogue(db)