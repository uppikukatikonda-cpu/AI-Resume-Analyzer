from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5-mini",
    input="Say hello and confirm that you are working."
)

print(response.output_text)