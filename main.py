import openai

#Adding your openAI secret Key
openai.api_key = "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"

#Creating the chat openai model

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
