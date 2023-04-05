import numpy as np
import pandas as pd

matches = pd.read_csv('matches.csv')
delivery = pd.read_csv('deliveries.csv')
deliveries=delivery.drop(delivery[delivery['is_super_over']!=0].index)

## Innings played
innings_played=deliveries.groupby(['batsman'])['match_id'].nunique().reset_index()
innings_played=innings_played.rename(columns={'match_id':'total_innings'})
innings_played=innings_played[innings_played['total_innings']>20].reset_index(drop=True)
batsman_names=innings_played['batsman'].to_list()
deliveries=deliveries[deliveries.batsman.isin(batsman_names)]
deliveries_bowler=deliveries.drop(deliveries[deliveries['wide_runs'] != 0].index)
deliveries_bowler=deliveries.drop(deliveries[deliveries['noball_runs'] != 0].index)

## Run scored year wise by batsman

yearly_runs=deliveries.groupby(['match_id','batsman'])['batsman_runs'].sum().reset_index()
year=matches[['id','season']]
year=year.rename(columns={'id':'match_id'})
yearly=pd.merge(yearly_runs,year,on=['match_id'])
yearly=yearly.groupby(['batsman','season'])['batsman_runs'].sum().reset_index()

def fetch_player():
    return yearly,batsman_names

