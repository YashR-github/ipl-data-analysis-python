from loader import load_data
from plots import plot_total_runs , plot_top_rcb_batsmen, plot_matches_per_team_per_season, plot_matches_played_per_year,plot_matches_won_per_team, plot_extra_runs_conceded_per_team_2016, plot_no_of_umpires_by_country_except_India, plot_top_economical_bowlers_2015
from transform import total_runs_by_team, top_rcb_batsmen, matches_per_team_per_season, matches_played_per_year, matches_won_per_team, extra_runs_conceded_per_team_2016, no_of_umpires_by_country_except_India, top_economical_bowlers_2015


def main():
    matches, deliveries, umpires = load_data()
    # plot total runs by team
    result = total_runs_by_team(deliveries)
    plot_total_runs(result)
    # plot top 10 rcb batsmen
    result = top_rcb_batsmen(deliveries)
    plot_top_rcb_batsmen(result)
    #number of umpires in IPL by country except India
    result = no_of_umpires_by_country_except_India(umpires)
    plot_no_of_umpires_by_country_except_India(result)
    # matches played by team per season
    result = matches_per_team_per_season(matches)
    plot_matches_per_team_per_season(result)
    # no of matches played per year for all the years 
    result = matches_played_per_year(matches)
    plot_matches_played_per_year(result)
    # number of matches won per team per year in IPL
    result= matches_won_per_team(matches)
    plot_matches_won_per_team(result)
    # Extra runs conceded per team in the year 2016
    result= extra_runs_conceded_per_team_2016(deliveries,matches)
    plot_extra_runs_conceded_per_team_2016(result)
    # Top 10 economical bowlers in the year 2015
    result = top_economical_bowlers_2015(matches,deliveries)
    plot_top_economical_bowlers_2015(result)



if __name__ == "__main__":
    main()

