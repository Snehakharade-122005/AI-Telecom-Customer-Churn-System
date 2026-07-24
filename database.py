import mysql.connector


# -------------------------------------------------
# MySQL Connection
# -------------------------------------------------

def get_connection():

    connection = mysql.connector.connect(

        host="localhost",
        user="root",
        password="mysql@123",
        database="telecom_churn"

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