import os
# os.system('cls') To clear console
import sqlite3


def table_exists(table_name):
    conn = sqlite3.connect('chatbot.db')  # Replace 'your_database.db' with your database file name
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    return cursor.fetchone() is not None



# Use SQLite3 to Access/Create the database table




if table_exists("learning"):
    file = open("ChatBot.txt", "r")
    name = str(file.read())
    file.close()
    print("Started ChatBot - " + name)
else:
    file = open("ChatBot.txt", "w")
    name = str(input("Give your new ChatBot a name: "))
    file.write(name)
    file.close()

    
    # Connect to an SQLite database (or create one if it doesn't exist)
    conn = sqlite3.connect('chatbot.db')

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    # Execute a SQL query to create a table
    cur.execute('''CREATE TABLE IF NOT EXISTS learning
                   (id REAL, question TEXT, reply TEXT)''')

    # Insert data into the table
    cur.execute("INSERT INTO learning VALUES (0, 'Hello', 'Hello')")

    # Commit the transaction
    conn.commit()

    # Execute a SQL query to retrieve data
    cur.execute("SELECT * FROM learning")
    rows = cur.fetchall()

    # Close the cursor and the connection
    cur.close()
    conn.close()
    
    print("Started new ChatBot - " + name)







# Use python to execute Machine Learning
exit_conditions = [":q", "exit", "quit"]

while True:
    user_input = str(input(">>> "))
    if user_input in exit_conditions:
        os.system('cls')
        break
    elif user_input == "tnt.en":
        file = open("ChatBot.txt", "w")
        name = str(input("Give your ChatBot a new name: "))
        file.write(name)
        file.close()
    elif user_input == "tnt.tb":
        print("Training Mode - Train " + name + ":")
        while True:
            conn = sqlite3.connect('chatbot.db')
            cur = conn.cursor()
            q = str(input("Q: "))
            if q in exit_conditions:
                cur.close()
                conn.close()
                break

            
            a = str(input("A:"))
            if q in exit_conditions:
                cur.close()
                conn.close()
                break

            
            cur.execute("SELECT MAX(id) FROM learning")
            result = cur.fetchone()
            current_id_get = int(result[0] + 1)
            cur.execute("INSERT INTO learning VALUES (" + str(current_id_get) + ", '" + str(q) + "', '" + str(a) + "')")

            conn.commit()
            cur.close()
            conn.close()
            
    else:
        user_input = user_input.split(" ")
        
        conn = sqlite3.connect('chatbot.db')
        cur = conn.cursor()
        cur.execute("SELECT question FROM learning")
        questions = cur.fetchall()

        cur.execute("SELECT reply FROM learning")
        answers = cur.fetchall()
        

        
        match_list = []
        for i in questions:
            match_list.append(0)
        
        for i in user_input:
            for j in range(len(questions)):
                sentence_question = questions[j][0]
                question_words = sentence_question.split(" ")
                for k in question_words:
                    if i.lower() == k.lower():
                        match_list[j] = match_list[j] + 1
        greatest = 0
        index = 0
        greatest_index = 0
        for i in match_list:
          if i > greatest:
            greatest = i
            greatest_index = index
          index += 1
        if greatest_index < 1:
            answer = "I'm sorry, I am unable to answer that! Please feel free to chat!
        else:
            answer = answers[greatest_index][0]

        print(name + ": " + answer)

        cur.close()
        conn.close()
        






