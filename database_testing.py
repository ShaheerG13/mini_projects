import psycopg2
import os
from collections import defaultdict

# establish connection with database
def get_connection():
    try:
        return psycopg2.connect(
            database="habit_tracker",
            user="habit_track_user",
            password="",
            host="127.0.0.1",
            port=5432,
        )
    except:
        print("Connection to the PostgreSQL encountered an error.")
        return False

connection = get_connection()
curr = connection.cursor()

# get the user_id based on username
username = 'default'
curr.execute("SELECT id FROM users WHERE username = %s", (username,))
row = curr.fetchone()
user_id = row[0] if row else None


# get all the habits of current user
curr.execute("""
    SELECT id, name
    FROM habits
    WHERE user_id = %s
    ORDER BY created_at
""", (user_id,))

habits = curr.fetchall()


# get history data for each habit
curr.execute("""
    SELECT habit_id, date, completed
    FROM daily_habits
    WHERE habit_id IN (
        SELECT id FROM habits WHERE user_id = %s
    )
    ORDER BY date
""", (user_id,))

habit_rows = curr.fetchall()


# display data
history = defaultdict(dict)

for habit_id, day, completed in habit_rows:
    history[day][habit_id] = completed

for day in sorted(history):
    print(day)
    for habit_id, name in habits:
        completed = history[day].get(habit_id, False)
        print(f"  {name}: {completed}")

connection.close()
