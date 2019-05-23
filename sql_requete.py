import pymysql


class Database:

    def __init__(self, db, user, mdp):
        self.db = db
        self.user = user
        self.mdp = mdp
        with pymysql.connect(host='localhost',
                                 user=self.user,
                                 password=self.mdp,
                                 db=self.db,
                                 charset='utf8mb4') as connexion:
            self.connexion = connexion


    def creation_table(self, dictionnaire):
        # sql = "CREATE TABLE IF NOT EXISTS Valeurs_foncieres(transaction_id INT AUTO_INCREMENT PRIMARY KEY," ...
        pass

    def requete(self):
        sql = "SELECT * FROM student_coord"
        self.connexion.execute(sql)
        return self.connexion.fetchall()


# exemple
db1 = Database("Promotion10", "user1", "mdpuser1")
print(db1.requete())