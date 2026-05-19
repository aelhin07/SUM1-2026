from anthropic import Anthropic

client = Anthropic()

# user_prompt = input("What is your question? ")

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    system="",
    messages=[
        {"role": "user", "content": "What is Hult International Business School? "}
    ]
)

print(response.content[0].text)