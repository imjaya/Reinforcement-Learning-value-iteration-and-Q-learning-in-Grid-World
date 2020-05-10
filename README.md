# Reinforcement-Learning-value-iteration-and-Q-learning-in-Grid-World

# Value Iteration
value iteration agent is an onine planner, not a reinforcement learning agent, and so the relevant training option is the number of iterations of value iteration it should run (option -i) in its initial planning phase. ValueIterationAgent takes an MDP on construction and runs value iteration for the specified number of iterations before the constructor returns. Value iteration computes k-step estimates of the optimal values, Vk. In addition to running value iteration, implement the following methods for ValueIterationAgent using Vk.

 computeActionFromValues(state) computes the best action according to the value function given by self.values.

 computeQValueFromValues(state, action) returns the Q-value of the (state, action) pair given by the value function given by self.values.

These quantities are all displayed in the GUI: values are numbers in squares, Q-values are numbers in square quarters, and policies are arrows out from each square.

python gridworld.py -a value -i 100 -k 10
python gridworld.py -a value -i 5

# Bridge Crossing Analysis

BridgeGrid is a grid world map with the a low-reward terminal state and a high-reward terminal state separated by a narrow \bridge", on either side of which is a chasm of high negative reward. The agent starts near the low-reward state. With the default discount of 0.9 and the default noise of 0.2, the optimal policy does not cross the bridge. 

python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.9 --noise 0.2

# Polices

This grid has two terminal states with positive payoff (in the middle row), a close exit with payoff +1 and a distant exit with payoff +10. The bottom row of the grid consists of terminal states with negative payoff (shown in red); each state in this \cliff" region has payoff -10. The starting state is the yellow square. We distinguish between two types of paths: (1) paths that \risk the cliff" and travel near the bottom row of the grid; these paths are shorter but risk earning a large negative payoff, and are represented by the red arrow. (2) paths that \avoid the cliff" and travel along the top edge of the grid. These paths are longer but are less likely to incur huge negative payoffs. These paths are represented by the green arrow.

the discount, noise, and living reward parameters for this MDP to produce optimal policies of several different types. Your setting of the parameter values for each part should have the property that, if your agent followed its optimal policy without being subject to any noise, it would exhibit the given behavior. If a particular behavior is not achieved for any setting of the parameters, assert that the policy is impossible by returning the string 'NOT POSSIBLE'.

Here are the optimal policy types you should attempt to produce:
Prefer the close exit (+1), risking the cliff (-10)

Prefer the close exit (+1), but avoiding the cliff (-10)

Prefer the distant exit (+10), risking the cliff (-10)

Prefer the distant exit (+10), avoiding the cliff (-10)

Avoid both exits and the cliff (so an episode should never terminate)

python autograder.py -q q3

# Q-Learning

Q-learning agent, which does very little on construction, but instead learns by trial and error from interactions with the environment through its update(state, action, nextState, reward) method. A stub of a Q-learner is specied in QLearningAgent in qlearningAgents.py, and you can select it with the option '-a q'. For this question, you must implement the update, computeValueFromQValues, getQValue, and computeActionFromQValues methods.

Note: For computeActionFromQValues, you should break ties randomly for better behavior. The random.choice() function will help. In a particular state, actions that your agent hasn't seen before still have a Q-value, specifically a Q-value of zero, and if all of the actions that your agent has seen before have a negative Q-value, an unseen action may be optimal.

With the Q-learning update in place, you can watch your Q-learner learn under manual control, using the key-board:

python gridworld.py -a q -k 5 -m

Recall that -k will control the number of episodes your agent gets to learn. Watch how the agent learns about the state it was just in, not the one it moves to, and \leaves learning in its wake." Hint: to help with debugging, you can turn off noise by using the 􀀀􀀀noise 0.0 parameter (though this obviously makes Q-learning less interesting). If you manually steer Pacman north and then east along the optimal path for four episodes.

# Epsilon Greedy
python gridworld.py -a q -k 100


