
import numpy as np
import pandas as pd
from operator import add
import random
from env import final_states
import matplotlib.pyplot as plt




import numpy as np
import pandas as pd

class Double_QLearning:

    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.1):
        self.actions = actions  
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy

        # Initialize two Q-tables (q1 and q2)
        self.q1_table = pd.DataFrame(columns=self.actions, dtype=np.float64)
        self.q2_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

        self.display_name="Double Q-Learning"
        print("Using Double Q-Learning ...")

    '''Choose a from s based on Q1 and Q2 (using epsilon greedy policy in Q1 + Q2)'''
    def choose_action(self, observation):
        self.check_state_exist(observation)

        q1_acton_values = self.q1_table.loc[observation, :]
        q2_acton_values = self.q2_table.loc[observation, :]

        # q1 + q2
        q_sum = q1_acton_values + q2_acton_values

        if np.random.uniform() >= self.epsilon:
            # Choose argmax action (exploitation)
            action = np.random.choice(q_sum[q_sum == np.max(q_sum)].index) # handle multiple argmax with random
        else:
            # Choose random action (exploration)
            action = np.random.choice(self.actions)

        return action

    '''Choose next a from s for target Q calculation'''
    def choose_next_action(self, observation, q_table):
        self.check_state_exist(observation)

        # Choose argmax action
        state_action_values = q_table.loc[observation, :]
        action = np.random.choice(state_action_values[state_action_values == np.max(state_action_values)].index) # handle multiple argmax with random

        return action

    '''Update the Q(S,A) state-action value table using the latest experience
       This is a not a very good learning update 
    '''
    def learn(self, s, a, r, s_):
        self.check_state_exist(s_)

        if np.random.random() < 0.5:
            # update q1
            return self.update_q_table(self.q1_table, self.q2_table, s, a, r, s_)
        else:
            # update q2
            return self.update_q_table(self.q2_table, self.q1_table, s, a, r, s_)

    '''Each Q function is updated using a value from the other Q function for the next state'''
    def update_q_table(self, q1, q2, s, a, r, s_):
        q_current = q1.loc[s, a]

        # Calucate target q value
        if s_ != 'terminal':
            a_ = self.choose_next_action(s_, q1) # argmax a in q1 table for s_
            q_target = r + self.gamma * q2.loc[s_, a_] # use q2 is used to update q1
        else:
            q_target = r  

        # Update current q value
        q1.loc[s, a] += self.lr * (q_target - q_current)  # update current state-action value

        return s_, self.choose_action(s_) # choose next action based on q1 and q2

    '''States are dynamically added to the Q(S,A) table as they are encountered'''
    def check_state_exist(self, state):
        if state not in self.q1_table.index:
            # append new state to q table
            self.q1_table = self.q1_table.append(
                pd.Series(
                    [0]*len(self.actions),
                    index=self.q1_table.columns,
                    name=state,
                )
            )

        if state not in self.q2_table.index:
            # append new state to q table
            self.q2_table = self.q2_table.append(
                pd.Series(
                    [0]*len(self.actions),
                    index=self.q2_table.columns,
                    name=state,
                )
            )
    def print_q_table(self):
       # Getting the coordinates of final route from env.py
       e = final_states()

       # Comparing the indexes with coordinates and writing in the new Q-table values
       for i in range(len(e)):
           state = str(e[i])  # state = '[5.0, 40.0]'
           # Going through all indexes and checking
           for j in range(len(self.q_table1.index)):
               if self.q_table1.index[j] == state:
                   self.q_table_final.loc[state, :] = self.q_table1.loc[state, :]

       print()
       print('Length of final Q-table =', len(self.q_table_final.index))
       print('Final Q-table with values from the final route:')
       print(self.q_table_final)

       print()
       print('Length of full Q-table =', len(self.q_table1.index))
       print('Full Q-table:')
       print(self.q_table1)

   # Plotting the results for the number of steps
    def plot_results(self, steps, cost):
       #
       f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
       #
       ax1.plot(np.arange(len(steps)), steps, 'b')
       ax1.set_xlabel('Episode')
       ax1.set_ylabel('Steps')
       ax1.set_title('Episode via steps')

       #
       ax2.plot(np.arange(len(cost)), cost, 'r')
       ax2.set_xlabel('Episode')
       ax2.set_ylabel('Cost')
       ax2.set_title('Episode via cost')

       plt.tight_layout()  # Function to make distance between figures

       #
       plt.figure()
       plt.plot(np.arange(len(steps)), steps, 'b')
       plt.title('Episode via steps')
       plt.xlabel('Episode')
       plt.ylabel('Steps')

       #
       plt.figure()
       plt.plot(np.arange(len(cost)), cost, 'r')
       plt.title('Episode via cost')
       plt.xlabel('Episode')
       plt.ylabel('Cost')

       # Showing the plots
       plt.show()