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
