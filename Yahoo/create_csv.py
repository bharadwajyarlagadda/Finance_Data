__author__ = 'Bharadwaj'

import csv
import time

class create_csv:

    def __init__(self, stock_symbol, summary_values, calls_headers, calls_row_data, puts_headers, puts_row_data):
        self.stock_symbol = stock_symbol
        self.summary_values = summary_values
        self.file = ''
        self.summary = "-summary"
        self.calls = "-calls"
        self.puts = "-puts"
        self.calls_headers = calls_headers
        self.calls_row_data = calls_row_data
        self.puts_headers = puts_headers
        self.puts_row_data = puts_row_data

    def execute(self):
        self.create_csv()

    def create_csv(self):
        today_date = time.strftime("%Y%m%d")
        if self.stock_symbol and self.summary_values:
            file_name = self.stock_symbol + "-" + today_date + self.summary
            self.write_to_csv(file_name)
        elif self.stock_symbol and not self.summary_values:
            file_name_calls = self.stock_symbol + "-" + today_date + self.calls
            file_name_puts = self.stock_symbol + "-" + today_date + self.puts
            self.write_to_csv(file_name_calls)
            self.write_to_csv(file_name_puts)
        else:
            pass

    def write_to_csv(self, file_name):
        file_write = open(file_name+".csv", 'w')
        csv_writer = csv.writer(file_write, lineterminator="\n")
        if "-calls" in file_name:
            csv_writer.writerow(self.calls_headers)
            csv_writer.writerows(self.calls_row_data)
        elif "-puts" in file_name:
            csv_writer.writerow(self.puts_headers)
            csv_writer.writerows(self.puts_row_data)
        elif "-summary" in file_name:
            for key, value in self.summary_values.items():
                csv_writer.writerow([key, value])
        else:
            pass
        file_write.close()