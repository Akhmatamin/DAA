OPEN_AI_KEY = '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'

from openai import OpenAI

client = OpenAI(
    api_key=OPEN_AI_KEY,
)

response = client.responses.create(
    model='gpt-6-luna',
    input='Write a one-sentence bedtime story about a unicorn.'
)
print(response.output_text)