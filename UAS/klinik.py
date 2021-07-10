import mysql.connector

try:
    connection = mysql.connector.connect(user='root',database='klinik_L200190031')

    mySql_insert_query = """INSERT INTO pasien_has_obat (no_pasienFK, no_obatFK) 
                           VALUES (%s, %s) """

    records_to_insert = [(10,101),
                         (20,201),
                         (30,301),
                         (40,401),
                         (50,501,),
                         (60,601),
                         (70,101),
                         (80,301),
                         (90,1001),
                         (100,1101),
                         (110,101),
                         (120,1301),
                         (130,1401),
                         (140,1201),
                         (140,1201)]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")






import mysql.connector

try:
    connection = mysql.connector.connect(user='root',database='klinik_L200190031')

    mySql_insert_query = """INSERT INTO resep (no_induk_dokterFK, no_pasienFK, no_obatFK, keluhan, gejala, jenis_penyakit) 
                           VALUES (%s, %s, %s, %s, %s, %s) """

    records_to_insert = [(1, 10, 101,'Demam', 'Batuk Kering', 'Covid 19'),
                         (1, 20, 201,'Pusing', 'Mual dan Muntah', 'Vertigo'),
                         (2, 30, 301,'Mual saat makan', 'Sakit berlebihan diperut', 'Maag'),
                         (3, 40, 401,'Bersin', 'Demam', 'Flu'),
                         (4, 50, 501,'Sesak Nafas', 'Mati Rasa', 'Jantung'),
                         (5, 60, 601,'Demam', 'Bersin', 'Influenza'),
                         (6, 70, 101,'Benjol di Anus', 'Anus Sakit', 'Wasir'),
                         (7, 80, 301,'Perut Sakit', 'Feses Cair', 'Diare'),
                         (7, 90, 1001,'Mata Sakit', 'Badan Sakit', 'Kelelahan'),
                         (8, 100, 1101,'Nyeri Dada', 'Batuk', 'Asma'),
                         (9, 110, 101,'Sakit mata', 'Batuk Kering', 'Covid 19'),
                         (10, 120, 1301,'Demam', 'Mata berair', 'Hipermetropi'),
                         (11, 130, 1401,'Benjolan di tubuh', 'Gatal Gatal', 'Cacar Air'),
                         (12, 140, 1201,'Panas', 'Pusing', 'Demam'),
                         (13, 140, 1201,'Mulut Bau', 'Gigi Kuning', 'Karang gigi')]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")




        
