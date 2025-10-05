

def calculate_reaction_rates(dataframe):
    import pandas as pd
    import numpy as np
    df = pd.read_csv(dataframe)  
    #print(df.head(5))
    times = df["time_min"]
    prod = df["product_yield"]
    delta_times = times.diff()
    delta_prod = prod.diff()
    df["reaction_rate"] = delta_prod/delta_times
    df["reaction_rate"][0] = 0
    return df

def find_optimal_conditions(dataframe):
    import pandas as pd
    import numpy as np
    df = pd.read_csv(dataframe)
    df["delta_yield"] = df["product_yield"].diff()
    best_setup = df.loc[df["delta_yield"].idxmax()]
    return best_setup
    
def compare_setups(dataframe_A,dataframe_B):
    import pandas as pd
    import numpy as np
    df_A = pd.read_csv(dataframe_A)
    df_B = pd.read_csv(dataframe_B)
    df_A["setup"] = "A"
    df_B["setup"] = "B"
    combined = pd.concat([df_A, df_B])
    avg_yields = combined.groupby("setup")["product_yield"].mean()
    print(avg_yields)
    best = avg_yields.idxmax()
    print(f"Better setup is {best}")

compare_setups("exercises\lecture_6\data\setup_A.csv","exercises\lecture_6\data\setup_B.csv")
    