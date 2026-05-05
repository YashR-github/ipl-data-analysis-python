import pandas as pd

def total_runs_by_team(deliveries):
    return deliveries.groupby("batting_team")["total_runs"].sum().sort_values(ascending=False)


def top_rcb_batsmen(deliveries):
    rcb = deliveries[deliveries["batting_team"] == "Royal Challengers Bangalore"]
    result = (rcb.groupby("batsman")["total_runs"]
                .sum()
                .sort_values(ascending=False)
                .head(10) )
    return result


def matches_per_team_per_season(matches):
    df1= matches[["season","team1"]].rename(columns={"team1":"team"})
    df2= matches[["season","team2"]].rename(columns={"team2":"team"})
    df = pd.concat([df1,df2])
    result =(
        df.groupby(["season","team"])
          .size()
          .unstack(fill_value=0)
    )
    return result



def matches_played_per_year(matches):
    return matches.groupby("season")["id"].count()


def matches_won_per_team(matches):
    return matches.groupby("winner")["id"].count().sort_values(ascending=False)


def extra_runs_conceded_per_team_2016(deliveries,matches):
    match_ids_2016 = matches[matches["season"]==2016]["id"]
    df_2016 = deliveries[deliveries["match_id"].isin(match_ids_2016)]
    return df_2016.groupby("bowling_team")["extra_runs"].sum().sort_values(ascending=False)


def no_of_umpires_by_country_except_India(umpires):
    foreign_umpires = umpires[umpires["country"] != "India"]
    return foreign_umpires.groupby("country").size().sort_values(ascending=False)


def top_economical_bowlers_2015(matches, deliveries):
    match_ids = matches[matches["season"]==2015]["id"]
    deliveries_2015 = deliveries[deliveries["match_id"].isin(match_ids)]
    runs = deliveries_2015.groupby("bowler")["total_runs"].sum()
    legal_deliveries= deliveries_2015[(deliveries_2015["wide_runs"]== 0) & (deliveries_2015["noball_runs"]==0)]
    balls= legal_deliveries.groupby("bowler").size()
    inner_join= runs.to_frame("runs").join(balls.to_frame("balls"),how= "inner")
    valid_data= inner_join[inner_join["balls"]>0] 
    economy =valid_data["runs"]/(valid_data["balls"]/6)
    return economy.sort_values(ascending =True).head(10)


