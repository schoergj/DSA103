from data_cleaner_solution import load_and_clean_setup_data
from data_cleaner_solution import combine_datasets
from kinetics_analyser_solution import calculate_reaction_rates, find_optimal_conditions, compare_setups


data_a = load_and_clean_setup_data(r"C:\Users\jschoer\Desktop\DSA103 Coding and Tests\DSA103\exercises\lecture_6\data\setup_A.csv", "A")
data_b = load_and_clean_setup_data(r"exercises\lecture_6\data\setup_B.csv", "B")

combined_df = combine_datasets(data_a, data_b)

calculate_reaction_rates(combined_df)
# find_optimal_conditions(combined_df)
compare_setups(combined_df)

# liste = find_optimal_conditions(combined_df)
# print(liste[2])