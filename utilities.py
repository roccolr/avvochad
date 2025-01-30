import os
import google.generativeai as genai

def get_prompts(path, delimiter='#') -> list:
    # legge fino al delimiter     
    with open(path, 'r') as file:
        text = file.read()
        prompt_list = text.split('#')
        return prompt_list

def clear_prompts(prompts)-> list:
    prompts_cleared = []
    for prompt in prompts:
        # print('debug')
        prompts_cleared.append(prompt.replace("\n", " "))
    return prompts_cleared

def initial_setup():
    os.environ["GRPC_VERBOSITY"] = "ERROR"
    os.environ["GLOG_minloglevel"] = "2"

def genera(prompt:str, api_key:str) -> str:
    genai.configure(api_key = api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text


if __name__ == '__main__':
    path = "/home/jsorel/Documents/Projects/OPEN_AI/gemini_api_test/prompts.txt"
    prompts = get_prompts(path)
    cleared_prompts = clear_prompts(prompts)
    print(cleared_prompts)