import ollama

print("🤖 Local AI Chatbot (type 'exit' to quit)\n")

while True:
    prompt = input("You: ")
    if prompt.lower() == 'exit':
        break

    response = ollama.chat(
        model='llama3',  # make sure you've pulled this model
        messages=[{'role': 'user', 'content': prompt}]
    )

    print("AI:", response['message']['content'].strip())

