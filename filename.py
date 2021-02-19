import csv
import cursor as cursor

with open('user.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    for row in readCSV:
        if row:
            first_name = int(row[0])
            last_name = int(row[1])
            user_id = int(row[2])
            cursor.execute("INSERT INTO t_users (first_name,last_name,user_id) VALUES (%s,%s,%s)",[first_name, last_name, user_id])
