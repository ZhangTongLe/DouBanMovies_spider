#coding=utf-8

import MySQLdb


class DataBase(object):
    def __init__(self):
        self.user = ''
        self.pass_word = ''
        self.db_name = 'DouBanMovies'
        self.db = MySQLdb.connect('localhost', self.user, self.pass_word, self.db_name, charset='utf8')
        self.cursor = self.db.cursor()

    def insert_into_db(self, name, stars):
        sql = 'INSERT INTO DOUBANMOVIES(name, stars)' \
              'VALUES("%s", %f)' % (name, stars)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception, e:
            print str(e)
            self.db.rollback()

    def close(self):
        self.db.close()

    def create_table(self):
        sql = """CREATE TABLE DouBanMovies (
                 id INT UNSIGNED AUTO_INCREMENT,
                 name VARCHAR(25),
                 stars FLOAT(3, 2),
                 PRIMARY KEY(id) )"""
        self.cursor.execute(sql)
        self.db.close()


if __name__ == '__main__':
    database = DataBase()
    database.create_table()
