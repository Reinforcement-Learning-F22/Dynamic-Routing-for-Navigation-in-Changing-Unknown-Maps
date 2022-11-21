# Dynamic-Routing-for-Navigation-in-Changing-Unknown-Maps

Using Reinforcement Learning (RL) algorithms to plan a global route for mobile robot navigation problems. Q-learning, Sarsa, and Double Q-learning algorithms for the environment with cliff, mouse, and cheese are compared.


## Explanation

RL algorithms for global path planning for mobile robots are implemented in Python. It is claimed that such a system has feedback. Both the agent and the environment have an impact on each other. The agent: 
- Takes action 
- Gets observation (new state) 
- Gets reward at each stage.

The environment:
- Receives action.
- Emits observation (new state).
- Emits reward.

The weights table, or Q-table of the system state, is the main part of the RL approach. The matrix Q contains all conceivable system states as well as the system's response weights to various actions. Mobile robot discovers how to avoid hazards and find the way to the desired location while attempting to move through the environment. Thus, the Q-table is created. It is possible to see the agent's decision for the subsequent action by looking at the table's values (mobile robot). Below are examples and descriptions of the experimental findings from various environments. There are numerous comments that support the code. It will walk you through the full notion of implementation step by step.

<br/>Each folder consists of three files:

* _env.py_ - building an environment with obstacles.
* _agent_brain.py_ - implementation of algorithm itself.
* _run_agent.py_ - running the experiments.




