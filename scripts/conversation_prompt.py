from transformers import pipeline, Conversation

prompt = input("Ask me a question to get started. \n")
model_name = "facebook/blenderbot-3B"

chatbot = pipeline(model=model_name)
conversation = Conversation(prompt)
conversation = chatbot(conversation)
response = conversation.generated_responses[-1]

print(response)
