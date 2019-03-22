# coding=utf-8
from HelperFunctions import mysqlConnexion
import datetime

# On crée la base et la table si elles n'existent pas
def createIfNotExist():
    db = mysqlConnexion()
    cur = db.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS vdmdb")

    cur.execute("CREATE TABLE IF NOT EXISTS reservation ("
                "id int auto_increment primary key,"
                "id_acheteur int(11) not null,"
                "id_game int(11) not null,"
                "dateheure datetime not null,"
		"date_prise_reservation datetime not null,"
                "email varchar(50) not null)")
    db.close()


def addReservationToSQL(reservation):
    db = mysqlConnexion()
    query = "insert into reservation (id_acheteur, id_game, dateheure, date_prise_reservation, email) " \
            "values('%d', '%d', '%s', '%s', '%s')" % (reservation.idSpectateur, reservation.idGame, reservation.dateHeure, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), reservation.email)
    print(query)
    try:
	if "'" in reservation.email:
		reservation.email = "ERROR"
    	cur = db.cursor()
    	cur.execute(query)
    	reservation_id = db.insert_id()
    	db.commit()
    except:
	print("Faild to add reservation")
	reservation_id = -1
	reservation.email = "ERROR"
 	cur = db.cursor()
        cur.execute(query)
        reservation_id = db.insert_id()
        db.commit()
    finally:
	db.close()

    return reservation_id


createIfNotExist()
