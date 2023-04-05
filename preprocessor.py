import pandas as pd
import numpy as np

def preprocess():

    #Economy

    df = pd.read_csv('deliveries.csv')
    df = df.replace(np.nan, 0)
    bowler = df.groupby('bowler')['match_id'].nunique().reset_index()
    bowler = bowler.rename(columns={'match_id': 'number_of_matches'})
    bowler = bowler[bowler['number_of_matches'] > 20]
    bowler.reset_index(drop=True, inplace=True)
    run = df.groupby(['bowler'])['total_runs'].sum().reset_index()
    merged = pd.merge(bowler, run, left_on='bowler', right_on='bowler', how='inner')
    over = df[df['ball'] <= 6]
    over = over['bowler'].value_counts().reset_index()
    over = over.rename(columns={'index': 'bowler', 'bowler': 'no_of_balls'})
    over['no_of_overs'] = over['no_of_balls'] / 6
    final = pd.merge(merged, over, left_on='bowler', right_on='bowler', how='inner')
    final['overs'] = final['no_of_balls'] / 6
    final.drop('no_of_balls', inplace=True, axis=1)
    final['overs'] = final['overs'].round(decimals=2)
    final['economy'] = final['total_runs'] / final['overs']

    ## Ability
    df1 = df
    df1 = df1.drop(df1[df1['dismissal_kind'] == 'run out'].index)
    df1.dismissal_kind[df.dismissal_kind != 0] = 1
    df1 = df1.groupby(['bowler'])['dismissal_kind'].sum().reset_index()
    df1 = df1.rename(columns={'dismissal_kind': 'no_of_wickets'})
    final1 = pd.merge(df1, final, left_on='bowler', right_on='bowler', how='inner')
    df2 = df
    total_balls = df2['bowler'].value_counts().reset_index()
    total_balls.rename(columns={'index': 'bowler', 'bowler': 'no_of_balls'}, inplace=True)
    final2 = pd.merge(total_balls, final1, left_on='bowler', right_on='bowler', how='inner')
    final2.drop('no_of_overs', inplace=True, axis=1)
    final2['ability'] = final2['no_of_balls'] / final2['no_of_wickets']

    #Consistency
    consis = df.groupby('bowler')['wide_runs', 'noball_runs', 'batsman_runs'].sum().reset_index()
    consis = consis.eval('Sum=wide_runs+noball_runs+batsman_runs')
    consis.drop(['wide_runs', 'noball_runs', 'batsman_runs'], inplace=True, axis=1)
    consis = pd.merge(final2, consis, left_on='bowler', right_on='bowler', how='inner')
    consis['consistency'] = consis['Sum'] / consis['no_of_wickets']




    return consis,df


























