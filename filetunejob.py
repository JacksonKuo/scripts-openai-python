from openai import OpenAI

client = OpenAI()

job = client.fine_tuning.jobs.create(
    training_file="file-2h3qnhiCtargUEHZTD4rtb",
    model="gpt-4o-2024-08-06",
)