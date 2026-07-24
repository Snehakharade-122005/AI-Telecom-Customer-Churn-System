import pandas as pd
import numpy as np


def get_shap_explanation(
        model,
        background_data,
        customer_data,
        feature_names
):

    base_prediction = model.predict(customer_data)[0][0]

    impacts = []


    for i in range(customer_data.shape[1]):

        modified = customer_data.copy()


        # Change one feature slightly
        modified[0][i] = modified[0][i] + 0.5


        new_prediction = model.predict(modified)[0][0]


        impact = abs(
            base_prediction - new_prediction
        )


        impacts.append(impact)



    result = pd.DataFrame({

        "Feature": feature_names,

        "Impact": impacts

    })


    result["Importance"] = result["Impact"].abs()


    result = result.sort_values(
        by="Importance",
        ascending=False
    )


    return result.head(5)