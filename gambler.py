from Enums import *
import random

class Gambler:
    def __init__(self, learning_rate=0.1, discount=0.95, exploration_rate=1.0, iterations=10000):
        self.q_table = [[[0]*4]*8]*8
        self.learning_rate = learning_rate # How much we appreciate new q-value over current
        self.discount = discount # How much we appreciate future reward over current
        self.exploration_rate = 1.0 # Initial exploration rate
        self.exploration_delta = 1.0 / iterations # Shift from exploration to explotation

    def get_next_action(self, state):
        if random.random() > self.exploration_rate: # Explore (gamble) or exploit (greedy)
            return self.greedy_action(state)
        else:
            return self.random_action()

    def greedy_action(self, state):
        bestAction = max(self.q_table[state[0]][state[1]][Direction.UP.value], self.q_table[state[0]][state[1]][Direction.RIGHT.value], self.q_table[state[0]][state[1]][Direction.DOWN.value], self.q_table[state[0]][state[1]][Direction.LEFT.value])
        if self.q_table[state[0]][state[1]][Direction.UP.value] == bestAction:
            return Direction.UP
        elif self.q_table[state[0]][state[1]][Direction.RIGHT.value] == bestAction:
            return Direction.RIGHT
        elif self.q_table[state[0]][state[1]][Direction.DOWN.value] == bestAction:
            return Direction.DOWN
        elif self.q_table[state[0]][state[1]][Direction.LEFT.value] == bestAction:
            return Direction.LEFT

        return self.random_action()

    def random_action(self):
        return random.choice([Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT])

    def update(self, old_state, new_state, action, reward):
        # Old Q-table value
        old_value = self.q_table[old_state[0]][old_state[1]][action]
        # What would be our best next action?
        future_action = self.get_next_action(new_state).value
        # What is reward for the best next action?
        future_reward = self.q_table[new_state[0]][new_state[1]][future_action]

        # Main Q-table updating algorithm
        new_value = old_value + self.learning_rate * (reward + self.discount * future_reward - old_value)
        self.q_table[old_state[0]][old_state[1]][action] = new_value

        # Finally shift our exploration_rate toward zero (less gambling)
        if self.exploration_rate > 0:
            self.exploration_rate -= self.exploration_delta