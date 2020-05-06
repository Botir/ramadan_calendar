import sqlite3


class DBHelper:

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def get_regions(self):
        return self.cursor.execute('select id, name from regions order by sort_order asc limit 20').fetchall()

    def get_region(self, region_id):
        return self.cursor.execute('select id, name from regions where id=?', (region_id,)).fetchone()

    def get_calendar_by_region(self, region_id, dt):
        return self.cursor.execute('select * from ramadan_calendar where region_id = ? and r_date = ?',
                                   (region_id, dt)).fetchone()
