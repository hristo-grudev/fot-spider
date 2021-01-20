import sqlite3


class FotPipeline:
    conn = sqlite3.connect('fot.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `fot` (
                                                        title varchar(100),
                                                        description text,
                                                        date text
                                                        )''')
        self.conn.commit()

    def process_item(self, item, spider):
        title = item['title'][0]
        description = item['description'][0]
        date = item['date'][0]

        self.cursor.execute(f"""select * from fot where title = '{title}'""")
        is_exist = self.cursor.fetchall()

        if len(is_exist) == 0:
            self.cursor.execute(f"""insert into `fot`
                                                    (`title`, `description`, `date`)
                                                    values (?, ?, ?)""", (title, description, date))
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
