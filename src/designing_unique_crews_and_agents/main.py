#!/usr/bin/env python
import sys

from designing_unique_crews_and_agents.crew import DesigningUniqueCrewsAndAgentsCrew
from designing_unique_crews_and_agents.crew import DesignCrew
from designing_unique_crews_and_agents.crew import Design2Crew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():

    """"
    Run the crew.
    """
inputs = {
        'type' : 'sample_value',
        'market_data_url': 'sample_value',
        'research_focus': 'sample_value'
   }

if type == "1":
        print(f"hello type2 {type}")
        DesigningUniqueCrewsAndAgentsCrew().crew().kickoff(inputs=inputs)

elif type == "2":
        print(f"hello type2 {type}")

        inputs = {
            'market_data_url': 'trial 2',
            'research_focus': 'akki'
        }
        DesignCrew().crew().kickoff(inputs=inputs)


elif type == "3":
        print(f"hello type3 {type}")

        inputs = {
            'market_data_url': 'trial 3',
        }
        Design2Crew().crew().kickoff(inputs=inputs)


else:
        print(f"hello type3 {type}")
        print("wrong task")



def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'market_data_url': 'sample_value',
        'research_focus': 'sample_value'
    }

    try:
        DesigningUniqueCrewsAndAgentsCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    task_id = sys.argv[1]
    if task_id == "1":
        print(f"hello task1 {task_id}")

        inputs = {
            'market_data_url': 'trial',
            'research_focus': 'aadim'
        }
        DesigningUniqueCrewsAndAgentsCrew().crew().kickoff(inputs=inputs)

    elif task_id == "2":
        print(f"hello task2 {task_id}")

        inputs = {
            'market_data_url': 'trial 2',
            'research_focus': 'akki'
        }
        DesignCrew().crew().kickoff(inputs=inputs)


    elif task_id == "3":
        print(f"hello task2 {task_id}")

        inputs = {
            'market_data_url': 'trial 3',
        }
        Design2Crew().crew().kickoff(inputs=inputs)


    else:
        print(f"hello task3 {task_id}")
        print("wrong task")


    #try:
      #DesigningUniqueCrewsAndAgentsCrew().crew().replay(task_id=sys.argv[1])

    #except Exception as e:
     #   raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'market_data_url': 'sample_value',
        'research_focus': 'sample_value'
    }
    try:
        DesigningUniqueCrewsAndAgentsCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)