import pandas as pd
filepath1 = r"C:\Users\UZH\OneDrive - Universität Zürich UZH\Dokumente\HS25\Chemical Data Science\CDS_Excercises\CDS_Session_6\DSA103\exercises\lecture_6\data\setup_A.csv"
filepath2 = r"C:\Users\UZH\OneDrive - Universität Zürich UZH\Dokumente\HS25\Chemical Data Science\CDS_Excercises\CDS_Session_6\DSA103\exercises\lecture_6\data\setup_B.csv"

def load_and_clean_setup_data(filepath, setup_name):
    """Load and standardize data from one setup"""
    data = pd.read_csv(filepath)
    if "temp_fahrenheit" in data.columns:
        data["temp_fahrenheit"] = round((data["temp_fahrenheit"]-32)*(5/9), 1)
    colnames = ["time_min", "temp_C", "conc_M", "pH", "yield_percent"]
    data.columns = colnames
    data["setup_name"] = setup_name

    return data


data1 = load_and_clean_setup_data(filepath1, "A")
data2 = load_and_clean_setup_data(filepath2, "B")



# print(data1.head())
# print(data2.head())

def combine_datasets(setup_a_data, setup_b_data):
    """Combine datasets from both setups"""
    concat_data = pd.concat([setup_a_data, setup_b_data])
    return concat_data

print(combine_datasets(data1, data2))

