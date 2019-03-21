# coding=utf-8
import MySQLdb
import pymongo
import os


# Fonction qui verifie si le nouveau spectateur est l'acheteur de la réservation
def isAcheteur(newSpecateur, newAcheteur):
    if newSpecateur['Nom'] == newAcheteur['Nom'] \
        and newSpecateur['Prenom'] == newAcheteur['Prenom'] \
            and newSpecateur['Age'] == newAcheteur['Age']:
                return True


# ##############################  SQL  ################################## #
def mysqlConnexion():
    # Connexion Laidy RDS
    db = MySQLdb.connect(host=os.environ['MYSQL_HOST'],
                                   user=os.environ['MYSQL_USER'],
                                   passwd=os.environ['MYSQL_PWD'],
                                   db=os.environ['MYSQL_DB'])
    return db


# ##############################  MONGO  ################################## #
# fonction de connexion à la base
def mongoClient():
    client = pymongo.MongoClient(os.environ['MONGO_CLIENT'])
    return client


# fonction recup' de la base
def mongoDB(client, db):
    db = client[db]
    return db
