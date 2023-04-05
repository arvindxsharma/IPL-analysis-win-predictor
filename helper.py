import pandas as pd
import numpy as np

def fetch_eco(final):
    eco=final
    eco=eco.drop(['no_of_balls','number_of_matches','no_of_wickets',
              'total_runs','overs','ability','Sum','consistency'],axis=1)
    eco=eco.sort_values(by='economy')
    eco=eco.reset_index(drop=True)
    eco=eco.head(10)

    return eco



def fetch_wicket_taking_ability(final):
    ability=final
    ability=ability.drop(['no_of_balls', 'number_of_matches',
                'no_of_wickets', 'total_runs', 'overs', 'Sum', 'consistency','economy'], axis=1)
    ability=ability.sort_values(by='ability')
    ability=ability.reset_index(drop=True)
    ability=ability.head(10)
    return ability

def consistency1(final):
    consis=final
    consis=consis.drop(['no_of_balls', 'number_of_matches',
                'no_of_wickets', 'total_runs', 'overs', 'Sum','economy','ability'], axis=1)
    consis=consis.sort_values(by='consistency')
    consis=consis.reset_index(drop=True)
    consis=consis.head(10)
    return consis

def critical_Wicket_Taking_Ability(df):
    deliveries = df
    deliveries.player_dismissed[deliveries.player_dismissed != 0] = 1
    deliv = deliveries.groupby(['bowler', 'match_id'])['player_dismissed'].sum().reset_index()
    deliv = deliv[deliv['player_dismissed'] >= 4]
    deliv.reset_index(drop=True, inplace=True)
    critical_wicket_taken = deliv['bowler'].value_counts().reset_index()
    critical_wicket_taken = deliv['bowler'].value_counts().reset_index()
    critical_wicket_taken=critical_wicket_taken.head(10)
    critical_wicket_taken = critical_wicket_taken.rename(columns={'index': 'bowler', 'bowler': 'no_of_times'})
    return critical_wicket_taken


def hard_hitting_ability(final):
    hard_hit=final.drop(['finish_ability','consistency','running_btw_wicket'],axis=1)
    hard_hit=hard_hit.sort_values(by='hard_hit_ability',ascending=False).reset_index(drop=True)
    hard_hit=hard_hit.head(10)
    return hard_hit

def finishing_ability(finishing_ability):
    finishing_ability=finishing_ability.sort_values(by='finish_ability',ascending=False).reset_index(drop=True)
    finishing_ability=finishing_ability.head(10)
    return finishing_ability

def consistency(final):
    consistency=final.drop(['finish_ability','hard_hit_ability','running_btw_wicket'],axis=1)
    consistency=consistency.sort_values(by='consistency',ascending=False).reset_index(drop=True)
    consistency=consistency.head(10)
    return consistency

def running_between_the_wickets(final):
    running_between_the_wickets=final.drop(['finish_ability','hard_hit_ability','consistency'],axis=1)
    running_between_the_wickets=running_between_the_wickets.sort_values(by='running_btw_wicket',ascending=False).reset_index(drop=True)
    running_between_the_wickets=running_between_the_wickets.head(10)
    return running_between_the_wickets




















































