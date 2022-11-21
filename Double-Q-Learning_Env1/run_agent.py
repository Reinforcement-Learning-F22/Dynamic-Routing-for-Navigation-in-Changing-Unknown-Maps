

# Importing classes
from env import Environment
from agent_brain import Double_QLearning



def main():
    # Resulted list for the plotting Episodes via Steps
    steps = []

    # Summed costs for all episodes in resulted list
    all_costs_1 = []
    all_costs_2 = []
    #epsilon3 = 0.9
    #decay_factor3 = 0.999

    for episode in range(1000):
        # Initial Observation
        observation = env.reset()
        #epsilon3 *= decay_factor3

        # Updating number of Steps for each Episode
        i = 0

        # Updating the cost for each episode
        cost_1 = 0
        cost_2 = 0

        while True:
            # Refreshing environment
            env.render()

            # RL chooses action based on observation
            action = RL.choose_action(str(observation))

            # RL takes an action and get the next observation and reward
            observation_, reward, done = env.step(action)

            # RL learns from this transition and calculating the cost
            cost_1, cost_2  = RL.learn(str(observation), action, reward, str(observation_))
            
            cost_1 += cost_1
            cost_2 += cost_2

            # Swapping the observations - current and next
            
            observation = observation_

            # Calculating number of Steps in the current Episode
            i += 1

            # Break while loop when it is the end of current Episode
            # When agent reached the goal or obstacle
            if done:
                steps += [i]
                all_costs_1 += [cost_1]
                all_costs_2 += [cost_2]
                break

    # Showing the final route
    env.final()

    # Showing the Q-table with values for each action
    RL.print_q_table()

    # Plotting the results
    RL.plot_results(steps, all_costs_1)
    #RL.plot_results(steps, all_costs_2)


# Commands to be implemented after running this file
if __name__ == "__main__":
    # Calling for the environment
    env = Environment()
    # Calling for the main algorithm
    RL = Double_QLearning(actions=list(range(env.n_actions)))
    # Running the main loop with Episodes by calling the function update()
    env.after(100, main)  # Or just update()
    env.mainloop()
    
