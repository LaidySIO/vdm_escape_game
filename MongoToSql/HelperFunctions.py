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
    db = MySQLdb.connect(host=os.environ['mysql_host'],
                                   user=os.environ['mysql_user'],
                                   passwd=os.environ['mysql_pwd'],
                                   db=os.environ['mysql_db'])
    return db


# ##############################  MONGO  ################################## #
# fonction de connexion à la base
def mongoClient():
    client = pymongo.MongoClient(os.environ['mongo_client'])
    return client


# fonction recup' de la base
def mongoDB(client, db):
    db = client[db]
    return db
