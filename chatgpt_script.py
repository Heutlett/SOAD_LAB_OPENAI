from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="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"
)

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("*                    Chat with OpenAI                       *")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

while (True):

    msg_in = input("🐵 Yo: ")

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": msg_in,
            }
        ],
        model="gpt-3.5-turbo",
    )

    msg_out = chat_completion.choices[0].message.content

    print(f"\n💻 Openai: {msg_out}\n")
