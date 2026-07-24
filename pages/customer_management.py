import streamlit as st
import pandas as pd
import mysql.connector


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="Customer Management",
    page_icon="👥",
    layout="wide"
)


# -------------------------------------------------
# DATABASE CONNECTION
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



# -------------------------------------------------
# LOAD DATA FROM MYSQL
# -------------------------------------------------

def load_predictions():

    conn = get_connection()

    query = """
    SELECT *
    FROM predictions
    ORDER BY id DESC
    """

    df = pd.read_sql(
        query,
        conn
    )

    conn.close()

    return df



# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title(
    "👥 Customer Management System"
)


st.markdown("---")



# -------------------------------------------------
# FETCH DATA
# -------------------------------------------------

df = load_predictions()


if df.empty:

    st.warning(
        "No prediction history available."
    )


else:


    st.success(
        f"Total Records Found: {len(df)}"
    )


    st.subheader(
        "📋 Prediction History"
    )


    st.dataframe(
        df,
        width="stretch"
    )
    # -------------------------------------------------
# SEARCH AND FILTERS
# -------------------------------------------------

st.markdown("---")

st.subheader(
    "🔍 Search & Filter Customers"
)


col1, col2, col3 = st.columns(3)


with col1:

    search_text = st.text_input(
        "Search Customer ID / Gender"
    )


with col2:

    prediction_filter = st.selectbox(

        "Prediction",

        [
            "All",
            "Customer Will Churn",
            "Customer Will Stay"
        ]

    )


with col3:

    risk_filter = st.selectbox(

        "Risk Level",

        [
            "All",
            "🔴 High Risk",
            "🟡 Medium Risk",
            "🟢 Low Risk"
        ]

    )



filtered_df = df.copy()



# Search

if search_text:

    filtered_df = filtered_df[
        filtered_df.astype(str)
        .apply(
            lambda row:
            row.str.contains(
                search_text,
                case=False
            ).any(),
            axis=1
        )
    ]



# Prediction Filter

if prediction_filter != "All":

    filtered_df = filtered_df[
        filtered_df["prediction"]
        ==
        prediction_filter
    ]



# Risk Filter

if risk_filter != "All":

    filtered_df = filtered_df[
        filtered_df["risk"]
        ==
        risk_filter
    ]



st.subheader(
    "📊 Filtered Results"
)


st.dataframe(
    filtered_df,
    width="stretch"
)


st.info(
    f"Showing {len(filtered_df)} customers"
)
# -------------------------------------------------
# EXPORT FILTERED DATA
# -------------------------------------------------

st.markdown("---")

st.subheader(
    "📥 Export Customer Data"
)


csv = filtered_df.to_csv(
    index=False
).encode("utf-8")


st.download_button(

    label="📥 Download CSV",

    data=csv,

    file_name="customer_prediction_history.csv",

    mime="text/csv"

)



# -------------------------------------------------
# DELETE CUSTOMER RECORD
# -------------------------------------------------

st.markdown("---")

st.subheader(
    "🗑 Delete Prediction Record"
)


delete_id = st.number_input(

    "Enter Prediction ID to Delete",

    min_value=1,

    step=1

)



if st.button("❌ Delete Record"):


    conn = get_connection()

    cursor = conn.cursor()


    query = """
    DELETE FROM predictions
    WHERE id = %s
    """


    cursor.execute(
        query,
        (delete_id,)
    )


    conn.commit()


    cursor.close()

    conn.close()


    st.success(
        f"✅ Record {delete_id} deleted successfully"
    )


    st.rerun()