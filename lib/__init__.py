import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()

# Remove the imports from here to avoid circular imports