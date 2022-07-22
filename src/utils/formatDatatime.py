from dataclasses import dataclass
import datetime

class dateFormat():

    @classmethod
    def convert_date(self, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')