
# coding: utf-8

# # CREATING THE ENVIRONMENT

# In[1]:

# Let's import our dependencies
import  argparse
import gym


# In[2]:

#Let's define a function to process our user input
def build_arg_parser():
    parser = argparse.ArgumentParser(description = 'Run an environment')
    parser.add_argument('--input-env',dest = 'input_env',required = True , choices = ['cartpole','mountaincar','pendulum','lake','taxi'],help = 'specify the name of the environment')
    return parser


# In[3]:

#Now define the main function to call the parser
if __name__ == '__main__':
    args = build_arg_parser().parse_args()
    input_env = args.input_env
    # create a name map as in openai gym package
    name_map = {'cartpole': 'CartPole-v0','mountain-car':'Mountain-Car-v0','pendulum':'Pendulum-v0','taxi':'Taxi-v2','lake':'FrozenLake-v0'}
    #Create environment and reset it
    env = gym.make(name_map[input_env])
    env.reset()
    #iterate 1000 times 
    for _ in range(1000):
        #render the environment
        env.render()
        #take random action
        env.step(env.action_space.sample())

