from csv import DictReader
from collections import defaultdict
import pandas as pd


def total_runs_by_team(deliveries_path):
    result= defaultdict(int)
    with open(deliveries_path) as deliveries_file:
        deliveries_reader = DictReader(deliveries_file)
        for delivery in deliveries_reader:
            team= delivery["batting_team"]
            runs=int(delivery["total_runs"])
            result[team] +=runs
    return pd.Series(dict(sorted(result.items(),key = lambda x:x[1],reverse= True)))


def top_rcb_batsmen(deliveries_path):
    result= defaultdict(int) 
    with open(deliveries_path) as deliveries_file:
        delivery_reader= DictReader(deliveries_file)
        for delivery in delivery_reader:
            if delivery["batting_team"] == "Royal Challengers Bangalore":
                batsman = delivery["batsman"]
                runs=int(delivery["total_runs"])
                result[batsman] +=runs
    return pd.Series(dict(sorted(result.items(),key =lambda x: x[1],reverse=True)[:10]))



def matches_per_team_per_season(matches_path):
    result = defaultdict(lambda: defaultdict(int))
    with open(matches_path) as matches_file:
        match_reader = DictReader(matches_file)
        for match in match_reader:
            season = match["season"]
            result[season][match["team1"]] +=1
            result[season][match["team2"]] +=1
    return pd.DataFrame(dict(sorted(result.items(), key= lambda x:x[0], reverse = False))).transpose()



def matches_played_per_year(matches_path):
    result = defaultdict(int)
    with open(matches_path) as matches_file:
        match_reader = DictReader(matches_file)
        for match in match_reader:
            result[int(match["season"])] +=1
    return pd.Series(dict(sorted(result.items(), key= lambda x: x[0], reverse= False)))



def matches_won_per_team(matches_path):
    result = defaultdict(int)
    with open(matches_path)  as matches_file:
        match_reader= DictReader(matches_file)
        for match in match_reader:
            result[match["winner"]]+=1
    return pd.Series(dict(sorted(result.items(),key= lambda x :x[1], reverse=True)))



def extra_runs_conceded_per_team_2016(deliveries_path,matches_path):
    matches= set()
    bowling_teams = defaultdict(int)
    with open(matches_path) as matches_file:
        match_reader = DictReader(matches_file)
        for match in match_reader:
            if(int(match["season"])==2016):
                matches.add(int(match["id"]))
    with open(deliveries_path) as deliveries_file:
        deliveries_reader = DictReader(deliveries_file)
        for deliveries in deliveries_reader:
            if(int(deliveries["match_id"]) in matches):
                bowling_teams[deliveries["bowling_team"]]+= int(deliveries["extra_runs"])
    return pd.Series(dict(sorted(bowling_teams.items(), key= lambda x: x[1], reverse=True)))
       



def no_of_umpires_by_country_except_India(umpires_path):
    countries_umpires = defaultdict(int)
    with open(umpires_path) as umpires_file:
        umpires_reader = DictReader(umpires_file)
        for umpire in umpires_reader:
            if(umpire["country"]!= "India"):
                countries_umpires[umpire["country"]]+=1
    return pd.Series(dict(sorted(countries_umpires.items(), key=lambda x:x[1], reverse=True)))


def top_economical_bowlers_2015(matches_path, deliveries_path):
    matches_2015 = set()
    bowler_economy = defaultdict(int)
    bowler_runs = defaultdict(int)
    bowler_legal_deliveries = defaultdict(int)
    with open(matches_path) as matches_file:
        matches_reader = DictReader(matches_file)
        for match in matches_reader:
            if(int(match["season"])==2015):
                matches_2015.add(int(match["id"]))
    
    with open(deliveries_path) as deliveries_file:
        deliveries_reader= DictReader(deliveries_file)
        for delivery in deliveries_reader:
            if(int(delivery["match_id"]) in matches_2015):
                bowler_runs[delivery["bowler"]]+= int(delivery["total_runs"])
                if(int(delivery["wide_runs"]) ==0 and int(delivery["noball_runs"])==0):
                    bowler_legal_deliveries[delivery["bowler"]]+=1
        for bowler in bowler_legal_deliveries:
            if(bowler in bowler_runs):
                overs = bowler_legal_deliveries[bowler]/6
                bowler_economy[bowler]= bowler_runs[bowler]/overs
    return pd.Series(dict(sorted(bowler_economy.items(), key = lambda x: x[1], reverse=False)[:10]))
            

