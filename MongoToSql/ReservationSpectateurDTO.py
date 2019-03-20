# coding=utf-8
# Crée une reservation-spectateur puis l'ajoute dans la base
from ReservationSpectateur import ReservationSpectateur
from AddReservationSpectateurToSQL import addReservationSpectateurToSQL


def generateReservationSpectateur(collectionId, idReservation, listSpectateurs):
    for sepctateur in listSpectateurs:
        # print(sepctateur)
        reservation_spectateur = ReservationSpectateur(
            collectionId,
            idReservation,
            sepctateur['newSpectateur_id'],
            sepctateur['tarif'])
        reservation_spectateur.toString()
        addReservationSpectateurToSQL(reservation_spectateur)
