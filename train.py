import random
import time

from gambler import Gambler
from GameController import MouseGame

def main():
    learning_rate = 0.05
    discount = 0.9
    iterations = 10000

    agent = Gambler(learning_rate=learning_rate, discount=discount, iterations=iterations)

    # setup simulation
    mouseGame = MouseGame()
    mouseGame.reset()
    total_reward = 0 # Score keeping
    last_total = 0

    # main loop
    for step in range(iterations):
        old_state = list(mouseGame.mouse) # Store current state
        action = agent.get_next_action(old_state) # Query agent for the next action
        new_state, reward = mouseGame.take_action(action) # Take action, get new state and reward
        agent.update(old_state, new_state, action.value, reward) # Let the agent update internals

        total_reward += reward # Keep score
        if step % 250 == 0: # Print out metadata every 250th iteration
            performance = (total_reward - last_total) / 250.0
            print({'step': step, 'performance': performance, 'total_reward': total_reward})
            last_total = total_reward

        time.sleep(0.00001) # Avoid spamming stdout too fast!

    # print("Final Q-table", agent.q_table)
    for i in range(len(agent.q_table)):
        for j in range(len(agent.q_table[i])):
            #print("[" + str(i) + "][" + str(j) + "]: ", end="")
            #print(agent.q_table[i][j])
            print("[%d][%d]:"%(i,j),agent.q_table[i][j])
    input() # so console window doesnt close on windows

if __name__ == "__main__":
    main()
