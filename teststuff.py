import sqlite3
import utility


while True:
    slave = input("enter command...")
    from utility import *

#ask what everything dose
    if slave == "/?":
        print("Commands list:\n/add_car\n/add_engine\n/com\n/view_cars\n/view_engines\n/del\n/quit")


# Insert car data into the car table 
    if slave == "/add_car":
        add()

# Insert engine data into the car table 
    if slave == "/com":
        save_changes()

# Fetch and print car table
    if slave == "/view_cars":
        veiw_cars()


# Fetch and print all rows
    if slave == "/view_engines":
        veiw_engines()

# Mr Rodkiss easteregg
    if slave == "/fish":
        print("🙄")

# Delete data from the table
    if slave == "/del":
        delete()


# Update data in the table
#c.execute("UPDATE users SET age = ? WHERE name = ?", (35, 'Alice'))

# Delete data from the table
#c.execute("DELETE FROM car WHERE id = ?", ('Bob',))

# Fetch and print all rows again
#c.execute("SELECT * FROM users")
#print("Updated users:")
#for row in c.fetchall():
#    print(row)

# Close the connection
    if slave == "/quit":
        break

print("you did good")

#SELECT car.make,model,engine,stockhp FROM car
#JOIN make
#ON car.make=make.id