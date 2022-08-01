import csv
import os


class UkrFilmsNotes:
    def __init__(self, file_path):
        self.__file_path = file_path

    def read_notes(self, file_path):
        self.__file_path = file_path

    def add_note(self, film_name, note, rating):
        with open(self.__file_path, 'a', newline='') as f:
            note_writer = csv.writer(f)
            note_writer.writerow([film_name, note, rating])

    def remove_note(self, film_name):
        temp_file = 'note_temp.csv'
        with open(self.__file_path, 'r') as inp, open(temp_file, 'w', newline='') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if row[0] != film_name:
                    writer.writerow(row)
        with open(temp_file, 'r') as inp, open(self.__file_path, 'w', newline='') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                writer.writerow(row)
        os.remove(temp_file)

    def print_note(self):
        with open(self.__file_path, 'r') as f:
            csv_reader = csv.DictReader(f)
            line_count = 1
            for row in csv_reader:
                print(
                    f'{line_count}) {row["film_name"]}: {row["note"]}; Rating: {row["rating"]}.')
                line_count += 1

    def get_highest_rating_film(self):
        films_list = []
        with open(self.__file_path, 'r') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                films_list.append([row['film_name'], row['rating']])

        films_list.sort(key=lambda x: x[1], reverse=True)
        result = list(filter(lambda x: x[1] == films_list[0][1], films_list))
        return result

    def get_lowest_rating_film(self):
        films_list = []
        with open(self.__file_path, 'r') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                films_list.append([row['film_name'], row['rating']])

        films_list.sort(key=lambda x: x[1], reverse=False)
        result = list(filter(lambda x: x[1] == films_list[0][1], films_list))
        return result

    def get_average_film_rating(self):
        sum_rating = 0
        films_counter = 0
        with open(self.__file_path, 'r') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                sum_rating += int(row['rating'])
                films_counter += 1

        return sum_rating / films_counter
