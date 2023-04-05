import streamlit as st
import matplotlib.pyplot as plt

import graphs
import helper
import preprocessor
import preprocessor2

st.sidebar.title("IPL data Analyzer")

selected_option=st.sidebar.radio("Whom you want to analyze",('Baller','Batsman'))

if selected_option=="Baller":
  st.sidebar.write('You selected bowler')

else:
   st.sidebar.write('You selected batsman')


option=st.sidebar.selectbox(
    'How do you want to do analysis',('Overall','Yearly')
)

if st.sidebar.button("Show Analysis"):
      if selected_option=='Baller' and option=='Overall':
        final,df=preprocessor.preprocess()

        economy=helper.fetch_eco(final)
        wicket_taking_ability=helper.fetch_wicket_taking_ability(final)
        consistency=helper.consistency1(final)
        critical_wicket_taking_ability=helper.critical_Wicket_Taking_Ability(df)

        st.title("Top Statistics of Bowler")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown("**Economy**")
            st.dataframe(economy)

        with col2:
            st.markdown("**Wicket-taking ability**")
            st.dataframe(wicket_taking_ability)

        with col3:
            st.markdown("**Consistency**")
            st.dataframe(consistency)

        with col4:
            st.markdown("**Critical Wicket Taker**")
            st.dataframe(critical_wicket_taking_ability)


      elif  selected_option=='Batsman' and option=='Overall':

          finishing_ability,final = preprocessor2.preprocess()

          st.title("Top Statistics of Batsman")
          col1, col2, col3, col4 = st.columns(4)

          hard_hitting_ability=helper.hard_hitting_ability(final)
          finish_ability=helper.finishing_ability(finishing_ability)
          consistency=helper.consistency(final)
          running_between_the_wickets=helper.running_between_the_wickets(final)



          with col1:
             st.markdown("**Hard-hitting Ability**")
             st.dataframe(hard_hitting_ability)

          with col2:
             st.markdown("**Finishing ability**")
             st.dataframe(finish_ability)

          with col3:
             st.markdown("**Consistency**")
             st.dataframe(consistency)

          with col4:
             st.markdown("**Running b/w wickets**")
             st.dataframe(running_between_the_wickets)


          # Graphs

          st.title("Batsman Strike Rate variation")
          year_df,names_options=graphs.fetch_player()
          names=st.multiselect("Select Batsman Names",names_options,["V Kohli"])
          fig,ax=plt.subplots()
          for batsman in names:
              x=year_df[year_df['batsman']==batsman]['season']
              y = year_df[year_df['batsman'] == batsman]['batsman_runs']
              ax.plot(x,y,label=batsman)

          # Set the x-axis label, y-axis label, and title
          ax.set_xlabel('Season')
          ax.set_ylabel('Batsman Runs')
          ax.set_title('Batsman Runs per Season in IPL')

          # Add a legend
          ax.legend()

          # Display the graph
          st.pyplot(fig)
































