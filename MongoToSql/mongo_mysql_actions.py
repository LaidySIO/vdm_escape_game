# coding=utf-8
from GameDTO import generateGame
from ReservationDTO import generateReservation
from ReservationSpectateurDTO import generateReservationSpectateur
from SpectateurDTO import generateSpectateur
from HelperFunctions import isAcheteur, mongoClient, mongoDB
from bson.objectid import ObjectId

mongoClient = mongoClient()
db = mongoDB(mongoClient, "vdm_escape")
myTest = db['reservations']


def getReservation(document_id):
        document = myTest.find_one({"_id": ObjectId(document_id)})
        # On récupère l'acheteur puis on init l'id de l'acheteur à null
        newAcheteur = document['Acheteur']
        newAcheteur_id = None
        # On récupère les games puis l'ajoute dans la base
        newGame = document['Game']
        newGame_id = generateGame(newGame, document_id)
        # On récupère les spectateurs puis on les ajoute dans la base
        reservation = document['Reservation']
        listSpectateurs = []
        for spectateur in reservation:
        	newSpectateur_id = generateSpectateur(spectateur['Spectateur'], document_id)
        	listSpectateurs.append({'newSpectateur_id': newSpectateur_id, 'tarif': spectateur['Tarif']})
        	if isAcheteur(spectateur['Spectateur'], newAcheteur):
                	newAcheteur_id = newSpectateur_id
	# On ajoute la réservation dans la base
        newReservation_id = generateReservation(
                document_id,
                newAcheteur_id,
                newGame_id,
                document['Game']['Jour'],
                document['Game']['Horaire'],
                document['Acheteur']['Email']
        )
        # On ajoute la réservation_spectateur dans la base
	if newReservation_id > 1:
        	generateReservationSpectateur(
                	document_id,
                	newReservation_id,
                	listSpectateurs)
        	myTest.update_one({"_id": ObjectId(document_id)}, { "$set": { "status": "Done" } })
        	mongoClient.close()
	else:
		myTest.update_one({"_id": ObjectId(document_id)}, { "$set": { "status": "Error" } })
        return True


# TODO Stocker l'id de la collection  change['documentKey']['_id'] ??
# Exemple affichage "horizontal"
# print(dumps(change, sort_keys=True, indent=4))

