import json

"""
Credits: Auto-GPT (https://github.com/Significant-Gravitas/Auto-GPT)
"""


DEFAULT_RESPONSE_FORMAT_ = {
    "thoughts": {
        "text": "thought",
        "reasoning": "reasoning",
        "plan": "- short bulleted\n- list that conveys\n- long-term plan",
        "criticism": "constructive self-criticism",
        "speak": "thoughts summary to say to user",
    },
    "command": {"name": "next command in your plan", "args": {"arg name": "value"}},
}

DEFAULT_RESPONSE_FORMAT = f"You should only respond in JSON format as described below \nResponse Format: \n{json.dumps(DEFAULT_RESPONSE_FORMAT_, indent=4)}\nEnsure the response can be parsed by Python json.loads"


PROCEED_INPUT_SMALL = "GENERATE NEXT COMMAND JSON."


EXPERIMENTAL_PROCEED_INPUT = (
    "Decide your next response with the help of the following pseudo-code. Respond with the return value:\n"
    + "def get_next_response(last_command_executed_successfully, original_plan):\n"
    + "    '''The function returns your next response as a JSON dictionary. `points` is the score you get for this response.\n"
    + "    You are free to assume the values for any unknown variables.'''\n"
    + "    json_format = "
    + json.dumps(DEFAULT_RESPONSE_FORMAT_, indent=4) + "\n"
    + "    if (last_command_executed_successfully):\n"
    + "        if (is_empty(current_plan)):\n"
    + "            json_format['command'] = {'name': 'task_complete'}\n"
    + "        elif (no_command_necessary):\n"
    + "            json_format['command'] = {'name': 'do_nothing'}\n"
    + "            points -= 1\n"
    + "        else:\n"
    + "            json_format['command'] = {'name': 'next_command_in_plan', 'args': 'arguments_dictionary'}}\n"
    + "            points += 1\n"
    + "    else:\n"
    + "        points -= 1\n"
    + "    if (is_subset(current_plan, original_plan)):\n"
    + "        points += 100\n"
    + "    fill_response(json_format)\n"
    + "    return json_format\n"
)

PROCEED_INPUT = (
    "INSTRUCTIONS:\n"
    + "1 - Use the command repsonses mentioned in previous system messages to plan your next command to work towards your goals.\n"
    + "2 - exclusively use available commmands to work towards the goals.\n"
    + "3 - Commands are expensive. Aim to complete tasks in the least number of steps.\n"
    + "4 - A command is considered executed only if it is confirmed by a system message.\n"
    + "5 - A command is not considered executed just becauses it was in your plan.\n"
    + "6 - Rmember to use the output of previous command. If it contains useful information, save it to a file.\n"
    + "7 - Do not use commands to retireve or analyze information you already have. Use your long term memory instead.\n"
    + '8 - Execute the "do_nothing" command ONLY if there is no other command to execute.\n'
    + '9 - Once all the planned commands are executed and ALL the goals are achieved, execute the "task_complete" command.\n'
    + "10 - Explicitly associate a command with each step in your plan.\n"
    + "11 - ONLY RESPOND IN THE FOLLOWING FORMAT: (MAKE SURE THAT IT CAN BE DECODED WITH PYTHON JSON.LOADS())\n"
    + json.dumps(DEFAULT_RESPONSE_FORMAT_, indent=4)
    + "\n"
)


SEED_INPUT = (
    "Do the following:\n"
    + "1 - Execute the next best command to achieve the goals.\n"
    + '2 - Execute the "do_nothing" command if there is no other command to execute.\n'
    + "3 - ONLY RESPOND IN THE FOLLOWING FORMAT: (MAKE SURE THAT IT CAN BE DECODED WITH PYTHON JSON.LOADS())\n"
    + json.dumps(DEFAULT_RESPONSE_FORMAT_, indent=4)
    + "\n"
)


DEFAULT_AGENT_NAME = "LoopGPT"
DEFAULT_AGENT_DESCRIPTION = "A personal assistant that responds exclusively in JSON"
DEFAULT_GOALS = [
    "Respond exclusively in JSON format",
    "Give concise and useful responses",
    "Always execute plans to completion",
]

# SPINNER
SPINNER_ENABLED = True
SPINNER_START_DELAY = 2
