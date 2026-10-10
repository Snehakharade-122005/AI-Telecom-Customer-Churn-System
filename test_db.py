import mysql.connector

try:

    conn = mysql.connector.connect(
        
        host="sakura.proxy.rlwy.net",
                port=34046,
                user="root",
                password="ZTJTyCjqqdgWkWfFHbVRHPdRqfoLjHkL",
                database="railway",
                connection_timeout=15
    )

    print("MySQL connection successful!")

    conn.close()

except mysql.connector.Error as e:
    print("MySQL connection failed:", e)