# import mysql.connector
# import pandas as pd

# # -------------------------------------------------
# # MySQL Connection
# # -------------------------------------------------

# def get_connection():

#     connection = mysql.connector.connect(

#         host="sakura.proxy.rlwy.net",
#         port=34046,
#         user="root",
#         password="ZTJTyCjqqdgWkWfFHbVRHPdRqfoLjHkL",
#         database="railway"

#     )

#     return connection



# def save_prediction(data):

#     conn = get_connection()

#     cursor = conn.cursor()

#     query = """
#     INSERT INTO predictions
#     (
#         gender,
#         senior_citizen,
#         partner,
#         dependents,
#         tenure,
#         phone_service,
#         multiple_lines,
#         internet_service,
#         contract,
#         monthly_charges,
#         total_charges,
#         prediction,
#         probability,
#         risk,
#         revenue_risk
#     )
#     VALUES
#     (
#         %s, %s, %s, %s, %s,
#         %s, %s, %s, %s,
#         %s, %s, %s, %s, %s, %s
#     )
#     """

#     cursor.execute(query, data)

#     conn.commit()

#     cursor.close()

#     conn.close()



# # ==========================================
# # Get All Predictions
# # ==========================================

# def get_all_predictions():

#     conn = get_connection()

#     query = "SELECT * FROM predictions"

#     df = pd.read_sql(query, conn)

#     conn.close()

#     return df

import mysql.connector
import pandas as pd


# -------------------------------------------------
# Local MySQL Connection
# -------------------------------------------------

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="mysql@123",
        database="telecom_churn"
    )
    return connection


# -------------------------------------------------
# Save Prediction
# -------------------------------------------------

def save_prediction(data):
    conn = get_connection()

    try:
        cursor = conn.cursor()

        query = """
        INSERT INTO predictions (
            gender,
            senior_citizen,
            partner,
            dependents,
            tenure,
            phone_service,
            multiple_lines,
            internet_service,
            contract,
            monthly_charges,
            total_charges,
            prediction,
            probability,
            risk,
            revenue_risk
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s
        )
        """

        cursor.execute(query, data)
        conn.commit()

    finally:
        if conn.is_connected():
            if 'cursor' in locals():
                cursor.close()
            conn.close()


# -------------------------------------------------
# Get All Predictions
# -------------------------------------------------

def get_all_predictions():
    conn = get_connection()

    try:
        query = "SELECT * FROM predictions"
        df = pd.read_sql(query, conn)
        return df

    finally:
        conn.close()

