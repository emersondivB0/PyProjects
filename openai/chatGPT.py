import openai
<<<<<<< HEAD
openai.api_key = "openapi-key-here"
=======
openai.api_key = "key"
>>>>>>> e99ef44 (Nuevo prpyecto nibel inyermedio, modificación chat)

"""
while True:
    model_engine = "text-davinci-003"
    prompt = input("Enter new topic, Emerson: ")
    if "exit" in prompt or "quit" in prompt:
        break

    completion = openai.Completion.create(
            engine = model_engine,
            prompt = prompt,
            max_tokens = 1024,
            n =1,
            stop = None,
            temperature = 0.5
            )
    response = completion.choices[0].text

    print(response)
    print()

    import openai
"""

model_engine = "text-davinci-003"
prev_queries = []
prev_responses = []

while True:
    prompt = input("Enter new topic, Emerson (or enter 'exit' to quit): ")

    if "exit" in prompt or "quit" in prompt:
        break

    if prompt in prev_queries:
        index = prev_queries.index(prompt)
        response = prev_responses[index]
        print("Response from cache:")
        print(response)
    else:
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        )
        response = completion.choices[0].text
        prev_queries.append(prompt)
        prev_responses.append(response)
        print("New response:")
        print(response)

    print()

