from transformers import pipeline

chatbot = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

print("AI Chatbot (type 'exit' to stop)\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    prompt = f"User: {question}\nAssistant:"

    response = chatbot(prompt, max_new_tokens=100)

    answer = response[0]["generated_text"].split("Assistant:")[-1]

    print("Bot:", answer.strip())
