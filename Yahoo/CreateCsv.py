__author__ = 'Bharadwaj'

# This class helps in creating csv files for the respective stock symbols
# and write the relevant data (summary, calls, puts) to the files.
# Input - 1) Stock symbol
#         2) Summary
#         3) Calls - table headers
#         4) Calls - table data
#         5) Puts - table headers
#         6) Puts - table data
# Output - csv files with the respective data. csv files are created in the
#          format "stock_symbol-today_date-summary" (inside "Yahoo_Data" folder)

import csv
import time
import os


class CreateCsv:
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

    # create_csv - Input - strings(summary, calls, puts)
    #              Create "Yahoo_Data" directory structure
    #              Passes the file name to write_to_csv
    def create_csv(self):
        data_main_directory = os.getcwd() + os.path.sep + "Yahoo_Data"
        stock_summary_dir = os.getcwd() + os.path.sep + "Yahoo_Data" + os.path.sep + "Yahoo_NASDAQ_Stock_Summary"
        stock_calls_dir = os.getcwd() + os.path.sep + "Yahoo_Data" + os.path.sep + "Yahoo_NASDAQ_Stock_Calls"
        stock_puts_dir = os.getcwd() + os.path.sep + "Yahoo_Data" + os.path.sep + "Yahoo_NASDAQ_Stock_Puts"
        today_date = time.strftime("%Y%m%d")
        self.create_dir(data_main_directory)
        if self.stock_symbol and self.summary_values:
            file_name = self.stock_symbol + "-" + today_date + self.summary
            self.create_dir(stock_summary_dir)
            self.write_to_csv(stock_summary_dir, file_name)
        elif self.stock_symbol and not self.summary_values:
            file_name_calls = self.stock_symbol + "-" + today_date + self.calls
            file_name_puts = self.stock_symbol + "-" + today_date + self.puts
            self.create_dir(stock_calls_dir)
            self.create_dir(stock_puts_dir)
            self.write_to_csv(stock_calls_dir, file_name_calls)
            self.write_to_csv(stock_puts_dir, file_name_puts)
        else:
            pass

    def create_dir(self, dir_name):
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        else:
            pass

    # write_to_csv - Input - file_name
    #                Creates the csv files respectively
    #                Writes all the respective data to the files
    def write_to_csv(self, dir_name, file_name):
        file_write = open(dir_name + os.path.sep + file_name+".csv", 'w')
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