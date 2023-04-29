# Description: This is the Python Program to send Prompts & Receive Response from OpenAI API

import openai
import time

# Set up the OpenAI API key
openai.api_key = "<YOUR API KEY>"

# Define the maximum time to wait for an API response (in seconds)
API_TIMEOUT = 10

# Prompt the user for input and validate it
while True:
    try:
        prompt = input("Enter the prompt (or enter 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break
        if len(prompt) < 10:
            print("Please enter a longer prompt.")
            continue

        # Generate response with OpenAI API
        start_time = time.time()
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=4000,
            n=1,
            stop=None,
            temperature=1,
            timeout=API_TIMEOUT,
        )
        response_time = time.time() - start_time

        # Print the generated response
        print(response.choices[0].text.strip())
        print(f"Response generated in {response_time:.2f} seconds.")
    except openai.Error as e:
        print(f"Error: {e.message}")
    except Exception as e:
        print(f"Error: {str(e)}")
