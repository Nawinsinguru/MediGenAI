from app.rag.chat_service import HospitalChatService

chat = HospitalChatService()

while True:

    question = input("\nAsk: ")

    if question.lower() == "exit":
        break

    answer = chat.ask(question)

    print("\nAI:\n")
    print(answer)