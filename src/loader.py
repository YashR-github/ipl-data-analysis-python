import pandas as pd
from csv import DictReader


def load_data():
    with open("data/matches.csv", newline ='') as match:
        matches= pd.DataFrame(list(DictReader(match)))
    with open("data/deliveries.csv", newline='') as delivery:
        deliveries = pd.DataFrame(list(DictReader(delivery)))
    with open("data/umpires.csv", newline='') as umpire_read:
        umpires = pd.DataFrame(list(DictReader(umpire_read)))
    matches["season"] = pd.to_numeric(matches["season"], errors = "coerce")
    matches["id"] = pd.to_numeric(matches["id"], errors = "coerce")
    deliveries["total_runs"] = pd.to_numeric(deliveries["total_runs"],errors = "coerce")
    deliveries["extra_runs"] = pd.to_numeric(deliveries["extra_runs"],errors = "coerce")
    deliveries["match_id"] = pd.to_numeric(deliveries["match_id"],errors = "coerce")
    deliveries["wide_runs"] = pd.to_numeric(deliveries["wide_runs"],errors = "coerce")
    deliveries["noball_runs"] = pd.to_numeric(deliveries["noball_runs"],errors = "coerce")

    return matches, deliveries, umpires

    


        














# import pandas as pd

# def load_data():
#     matches = pd.read_csv("data/matches.csv")
#     deliveries = pd.read_csv("data/deliveries.csv")
#     return matches, deliveries




