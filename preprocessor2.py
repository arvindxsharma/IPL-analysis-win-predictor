import pandas as pd
import numpy as np

def preprocess():
    df = pd.read_csv('deliveries.csv')
    batsman = df.groupby('batsman')['match_id'].nunique().reset_index()
    batsman = batsman.rename(columns={'match_id': 'number_of_innings'})
    batsman = batsman[batsman['number_of_innings'] > 20].reset_index(drop=True)
    total_runs = df.groupby(['batsman'])['batsman_runs'].sum().reset_index()
    total_runs = total_runs.sort_values(by='batsman_runs').reset_index(drop=True)
    total_runs = pd.merge(total_runs, batsman, left_on='batsman', right_on='batsman', how='inner')
    total_runs = total_runs.reset_index(drop=True)

    # HARD HITTING ABILITY

    no_of_fours = df
    no_of_fours = no_of_fours[(no_of_fours['batsman_runs'] == 4)]
    no_4 = no_of_fours['batsman'].value_counts().reset_index()
    no_4 = no_4.rename(columns={'index': 'batsman', 'batsman': 'no_4'})
    no_of_six = df
    no_of_six = no_of_six[no_of_six['batsman_runs'] == 6]
    no_6 = no_of_six['batsman'].value_counts().reset_index()
    no_6 = no_6.rename(columns={'index': 'batsman', 'batsman': 'no_6'})
    final = pd.merge(total_runs, no_4, left_on='batsman', right_on='batsman', how='inner')
    final = pd.merge(final, no_6, left_on='batsman', right_on='batsman', how='left')
    no_of_balls = df
    no_of_balls = no_of_balls.drop(no_of_balls[no_of_balls['is_super_over'] != 0].index)
    no_of_balls = no_of_balls.drop(no_of_balls[no_of_balls['wide_runs'] != 0].index)
    no_of_balls = no_of_balls.drop(no_of_balls[no_of_balls['noball_runs'] != 0].index)
    balls = no_of_balls['batsman'].value_counts().reset_index()
    balls = balls.rename(columns={'index': 'batsman', 'batsman': 'balls'})
    hard_hit = pd.merge(balls, final, left_on='batsman', right_on='batsman', how='inner')
    hard_hit['4+6'] = hard_hit['no_4'] + hard_hit['no_6']
    hard_hit['hard_hit_ability'] = hard_hit['4+6'] / hard_hit['balls']

    # FINISHING ABILITY
    df = df.replace(np.nan, 0)
    only_out = df[df['player_dismissed'] != 0]
    count_out = only_out.groupby(['player_dismissed']).value_counts()
    count_out = count_out.reset_index()
    total_out = count_out['player_dismissed'].value_counts()
    total_out = total_out.reset_index()
    total_out = total_out.rename(columns={'index': 'batsman', 'player_dismissed': 'no_of_outs'})
    total_out = pd.merge(total_out, hard_hit, left_on='batsman', right_on='batsman', how='inner')
    total_out['not_outs'] = total_out['number_of_innings'] - total_out['no_of_outs']
    total_out['finish_ability'] = total_out['not_outs'] / total_out['number_of_innings']

    finish_ability=total_out
    finish_ability = finish_ability[
        finish_ability['batsman_runs'] / finish_ability['number_of_innings'] > 17].reset_index(drop=True)

    # CONSISTENCY OF PLAYER
    total_out['consistency'] = total_out['batsman_runs'] / total_out['no_of_outs']

    # RUNNING BETWEEN WICKETS
    total_out['running_run'] = total_out['batsman_runs'] - ((total_out['no_4'] * 4) + (total_out['no_6'] * 6))
    total_out['running_balls'] = total_out['balls'] - total_out['4+6']
    total_out['running_btw_wicket'] = total_out['running_run'] / total_out['running_balls']

    total_out=total_out.drop(columns=['no_of_outs','balls','batsman_runs','number_of_innings','no_4','no_6',
                                      '4+6','not_outs','running_run','running_balls'],axis=1)

    finish_ability=finish_ability.drop(columns=['no_of_outs','balls','batsman_runs','number_of_innings','no_4','no_6',
                                      '4+6','not_outs','hard_hit_ability'])
    return finish_ability,total_out






    return hard_hit

