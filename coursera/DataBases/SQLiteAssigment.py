import sqlite3

# Connect to SQLite database (this will create the database file if it doesn't exist)
conn = sqlite3.connect('email_counts.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

# Create the 'Counts' table if it doesn't exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS Counts (
        org TEXT,
        count INTEGER
    )
''')

# Read mbox.txt file
filename = 'mbox.txt'
with open(filename, 'r') as file:
    for line in file:
        if line.startswith('From: '):
            email = line.split()[1]  # Extract email address
            org = email.split('@')[1]  # Extract domain name (organization)
            cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
            row = cur.fetchone()
            if row is None:
                # Insert new organization with count 1
                cur.execute(
                    'INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
            else:
                # Update count for existing organization
                cur.execute(
                    'UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

# Commit the changes and close the database connection
conn.commit()
conn.close()

# Retrieve and print the top 10 organizations with highest counts
conn = sqlite3.connect('email_counts.db')
cur = conn.cursor()
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10')
rows = cur.fetchall()
for row in rows:
    print(f'Organization: {row[0]}, Count: {row[1]}')

# Close the database connection
conn.close()
