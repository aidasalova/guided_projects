import mysql.connector
con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("Type the word: ").lower()

query = cursor.execute("SELECT * FROM Dictionary WHERE LOWER(Expression) = '%s' " %word)
results = cursor.fetchall()
query_fuzzy = cursor.execute("SELECT * FROM Dictionary WHERE SOUNDEX(LOWER(Expression)) = soundex('%s') " %word )
results_fuzzy = cursor.fetchall()

def definition(word):
    if results:
        return [f"{result[1]}" for result in results]
    elif results_fuzzy:
        user_input = input(f"Did you mean {results_fuzzy[0][0]}? Type Y or N: ")
        if user_input == 'Y':
            match = results_fuzzy[0][0]
            query_match = cursor.execute("SELECT * FROM Dictionary WHERE LOWER(Expression) = '%s' " %match )
            results_match = cursor.fetchall()
            return [f"{result_match[1]}" for result_match in results_match]
        elif user_input == 'N':
            return "The word does not exist"
        else:
            return "We didn't understand your entry"
    else:
        return "No word found"


mydefinition = definition(word)

if isinstance(mydefinition, list):
    for item in mydefinition:
        print("\n" + item + "\n")
else:
    print(mydefinition)   

