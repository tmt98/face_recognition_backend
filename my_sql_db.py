import mysql.connector


class Database:

    def __init__(self):

        self.connection2 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            # database="recognize2"
        )
        # create database
        cursor = self.connection2.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS recognize")
        cursor.close()

        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="recognize"
        )
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `recognize`.`faces` (`id` INT NOT NULL AUTO_INCREMENT,`user_id` INT(11) NOT NULL,`filename` VARCHAR(500) NOT NULL,`created` VARCHAR(45) NOT NULL,PRIMARY KEY (`id`),UNIQUE INDEX `id_UNIQUE` (`id` ASC));")
        cursor.execute("CREATE TABLE IF NOT EXISTS `recognize`.`users` (`id` INT NOT NULL AUTO_INCREMENT, `name` VARCHAR(45) NOT NULL,`class` VARCHAR(45) NOT NULL, `created` VARCHAR(45) NOT NULL, PRIMARY KEY(`id`))")
        # cursor.execute("")
        cursor.close()

    def init_db(self):
        print("connection to MySQL", self.connection.is_connected())
        if self.connection.is_connected() == False:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="recognize"
            )

    def query(self, q, arg=()):
        self.init_db()
        cursor = self.connection.cursor()

        cursor.execute(q, arg)
        results = cursor.fetchall()
        cursor.close()

        return results

    def insert(self, q, arg=()):
        self.init_db()
        cursor = self.connection.cursor()

        cursor.execute(q, arg)

        self.connection.commit()
        result = cursor.lastrowid
        cursor.close()
        return result

    def select(self, q, arg=()):
        self.init_db()
        cursor = self.connection.cursor()
        cursor.execute(q, arg)
        records = cursor.fetchall()
        # return cursor.execute(q, arg)
        return records

    def delete(self, q, arg=()):
        self.init_db()
        cursor = self.connection.cursor()
        result = cursor.execute(q, arg)
        self.connection.commit()
        return result
