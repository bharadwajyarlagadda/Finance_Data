__author__ = 'Bharadwaj'

import csv
import time

class create_csv:

    def __init__(self, stock_symbol, summary_values):
        self.stock_symbol = stock_symbol
        self.summary_values = summary_values
        self.file = ''

    def execute(self):
        self.create_csv()
        self.write_to_csv()

    def create_csv(self):
        today_date = time.strftime("%Y%m%d")
        file_name = self.stock_symbol + "-" + today_date + "-summary"
        self.file = open(file_name+".csv", 'w')

    def write_to_csv(self):
        csv_writer = csv.writer(self.file, lineterminator="\n")
        for key, value in self.summary_values.items():
            csv_writer.writerow([key, value])
        self.file.close()