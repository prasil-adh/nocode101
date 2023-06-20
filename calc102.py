import os
import openai
import operator


# Set up OpenAI API credentials
openai.api_type = "azure"
openai.api_base = "https://imc-nocode.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "0daa58934ebb404884de4bfa04832674"

# Function to process user input and generate a response
def process_input(input_text):
    # Check if the input is an exit command
    if input_text.lower() == 'exit':
        exit()

    #Prompt Engineering
    prompt = 'Scan this expression: ' + '"' + input_text + '"' + '. Please give only the mathematical expression that needs to be carried out as a return(expression for eval function in python), no extra text before and/or after the expression, dont give the answer either, and dont give any characters like =,?, etc. If there is no mathematical operation rescan the expression and provide an appropriate answer.'
    print(prompt)
    response = openai.ChatCompletion.create(
        engine = "nocode101",
        #Few Shot Learning (based on the message and roles)
        messages=[
            {"role": "system", "content": "You are a helpful mathematical assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )
    
    expression = response["choices"][0]["message"]["content"]
    try:
        answer = eval(expression)
    except:
        answer = expression

    return answer
    
    

if __name__ == '__main__':
    while True:
        user_input = input("Enter your message: ")
        response = process_input(user_input)
        print(f"Response: {response}")