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

## References

* Sichkar V. N. Effect of various dimension convolutional layer filters on traffic sign classification accuracy. Scientific and Technical Journal of Information Technologies, Mechanics and Optics, 2019, vol. 19, no. 3, pp. (in English). doi: <a href="https://doi.org/10.17586/2226-1494-2019-19-3-546-552" target="_blank">10.17586/2226-1494-2019-19-3-546-552</a> (Full-text available also here https://www.researchgate.net/profile/Valentyn_Sichkar)

* Sichkar V.N. Comparison analysis of knowledge based systems for navigation of mobile robot and collision avoidance with obstacles in unknown environment. St. Petersburg State Polytechnical University Journal. Computer Science. Telecommunications and Control Systems, 2018, Vol. 11, No. 2, Pp. 64–73. doi: <a href="https://doi.org/10.18721/JCSTCS.11206" target="_blank">10.18721/JCSTCS.11206</a> (Full-text available also here https://www.researchgate.net/profile/Valentyn_Sichkar)

* The research results for Neural Network Knowledge Based system for the tasks of collision avoidance is put in separate repository and is available here: https://github.com/sichkar-valentyn/Matlab_implementation_of_Neural_Networks

* The study of Semantic Web languages OWL and RDF for Knowledge representation of Alarm-Warning System is put in separate repository and is available here: https://github.com/sichkar-valentyn/Knowledge_Base_Represented_by_Semantic_Web_Language

* The study of Neural Networks for Computer Vision in autonomous vehicles and robotics is put in separate repository and is available here: https://github.com/sichkar-valentyn/Neural_Networks_for_Computer_Vision



