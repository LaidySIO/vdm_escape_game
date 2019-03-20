# coding=utf-8
# Crée une reservation puis l'ajoute dans la base
from Reservation import Reservation
from AddReservationToSQL import addReservationToSQL


def generateReservation(collectionId, idSpectateur, idGame, date, heure, email):
    reservation = Reservation(
        collectionId,
        idSpectateur,
        idGame,
        date + ' ' + heure,
        email)
    reservation.toString()
    newReservation_id = addReservationToSQL(reservation)
    return newReservation_id

