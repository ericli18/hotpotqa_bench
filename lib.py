import random

def get_prompts(n=4):
    with open('prompts.txt', 'r') as file:
        content = file.read().split('\n\n')
    
    prompts = [prompt.replace('\n', ' ').strip() for prompt in content if prompt.strip()]
    
    # Maybe throw error if it's larger idrk
    n = min(n, len(prompts))
    
    return random.sample(prompts, n)