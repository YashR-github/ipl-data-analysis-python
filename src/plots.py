import matplotlib.pyplot as plt,os



def plot_total_runs(result):
    plt.figure(figsize=(12, 6)) 
    result.sort_values(ascending=False)
    result.plot(kind="bar")
    plt.title("Total Runs by Team")
    plt.xlabel("Team")
    plt.ylabel("Runs")
    plt.xticks(rotation=45, ha="right")  # rotate + align x axis terms
    plt.tight_layout()
    os.makedirs("output", exist_ok=True)
    plt.savefig("output/total_runs_by_team.png")
    plt.close()



def plot_top_rcb_batsmen(result):
    plt.figure(figsize= (12,6))
    result.plot(kind="bar")
    plt.title("Top 10 RCB batsmen")
    plt.xlabel("Batsmen")
    plt.ylabel("Runs")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    os.makedirs("output",exist_ok=True)
    plt.savefig("output/top_rcb_batsmen.png")
    plt.close()



def plot_matches_per_team_per_season(df):
    plt.figure(figsize= (36,18))
    df.plot(kind="bar", stacked=True)
    plt.title("Matches played per Team per season")
    plt.xlabel("Season")
    plt.ylabel("Matches")
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor =(1.05,1.00), loc= "upper left")
    plt.tight_layout()
    os.makedirs("output",exist_ok=True)
    plt.savefig("output/matches_per_team_per_season.png", bbox_inches="tight")
    plt.close()



def plot_matches_played_per_year(result):
    plt.figure(figsize=(18,9))
    result.plot(kind="bar")
    plt.title("Matches played per year")
    plt.xlabel("Year")
    plt.ylabel("Matches")
    plt.xticks(rotation=45)
    os.makedirs("output",exist_ok=True)
    plt.savefig("output/matches_per_year.png")
    plt.close()



def plot_matches_won_per_team(result):
    plt.figure(figsize=(19,9))
    result.plot(kind="bar")
    plt.title("Matches won per Team")
    plt.xlabel("Team")
    plt.ylabel("Matches")
    plt.xticks(rotation=45)
    plt.tight_layout()
    os.makedirs("output",exist_ok=True)
    plt.savefig("output/matches_won_per_team.png")
    plt.close()


def plot_extra_runs_conceded_per_team_2016(result):
    plt.figure(figsize=(19,9))
    result.plot(kind="bar")
    plt.title("Extra Runs Conceded per Team in 2016")
    plt.xlabel("Team")
    plt.ylabel("Runs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    os.makedirs("output",exist_ok=True)
    plt.savefig("output/extra_runs_per_team_2016.png")
    plt.close()



def plot_no_of_umpires_by_country_except_India(result):
    plt.figure(figsize= (18,9))
    result.plot(kind="bar")
    plt.title("Number of Umpires by Country except India")
    plt.xlabel("Country")
    plt.ylabel("Umpires")
    plt.xticks(rotation = 45)
    plt.tight_layout()
    os.makedirs("output",exist_ok=True)
    plt.savefig("output/no_of_umpires_by_country.png")
    plt.close()


def plot_top_economical_bowlers_2015(result):
    plt.figure(figsize= (18,9))
    result.plot(kind="bar")
    plt.title("Top 10 economical bowlers in 2015")
    plt.xlabel("Bowler")
    plt.ylabel("Runs")
    plt.xticks(rotation= 45)
    plt.tight_layout()
    os.makedirs("output",exist_ok= True)
    plt.savefig("output/top_10_economical_bowlers_2015.png")
    plt.close()



