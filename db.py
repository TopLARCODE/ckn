import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
    
    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def set_nickname(self, user_id, nickname):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `nickname` = ? WHERE `user_id` = ?", (nickname, user_id,))


    def set_bbb(self, user_id, whoaset):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `kormyes` = ? WHERE `user_id` = ?", (whoaset, user_id,))



    def get_signup(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `signup` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `signup` = ? WHERE `user_id` = ?", (signup, user_id,))


    def set_kormlvl(self, user_id, lvl):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `korm_lvl` = ? WHERE `user_id` = ?", (lvl, user_id,))

    def set_time(self, user_id, time_sub):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `time_sub` = ? WHERE `user_id` = ?", (time_sub, user_id,))

    def set_sum(self, user_id, time_sub):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `sumshop` = ? WHERE `user_id` = ?", (time_sub, user_id,))

    def set_money(self, user_id, money):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `money` = ? WHERE `user_id` = ?", (money, user_id,))

    def set_kurs(self, user_id, kurs):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `kurs` = ? WHERE `user_id` = ?", (kurs, user_id,))


    def set_real(self, user_id, reals):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `real` = ? WHERE `user_id` = ?", (reals, user_id,))


    def get_nickname(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `nickname` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                nickname = str(row[0])
            return nickname


    def get_money(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `money` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                money = str(row[0])
            return money

    def get_korm(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `korm` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                korm = str(row[0])
            return korm

    def get_kormlvl(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `korm_lvl` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                korms = str(row[0])
            return korms


    def get_bank(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `bank` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                bank = str(row[0])
            return bank

    def get_bbb(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `kormyes` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                bbb = str(row[0])
            return bbb
            
    def get_kurs(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `kurs` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                kurs = str(row[0])
            return kurs


    def get_time(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `time_sub` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                sub = str(row[0])
            return sub


    def get_sum(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `sumshop` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                sum = str(row[0])
            return sum