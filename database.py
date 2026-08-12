import mysql.connector
import pandas as pd

# -------------------------------------------------
# MySQL Connection
# -------------------------------------------------

def get_connection():

    connection = mysql.connector.connect(

        host="sakura.proxy.rlwy.net",
        port=34046,
        user="root",
        password="ZTJTyCjqqdgWkWfFHbVRHPdRqfoLjHkL",
        database="railway"

    )

    return connection



def save_prediction(data):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO predictions
    (
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
    VALUES
    (
        %s, %s, %s, %s, %s,
        %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s
    )
    """

    cursor.execute(query, data)

    conn.commit()

    cursor.close()

    conn.close()



# ==========================================
# Get All Predictions
# ==========================================

def get_all_predictions():

    conn = get_connection()

    query = "SELECT * FROM predictions"

    df = pd.read_sql(query, conn)

    conn.close()

    return df