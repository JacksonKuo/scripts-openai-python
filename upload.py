from openai import OpenAI
client = OpenAI()

client.files.create(
  file=open("finetune.jsonl", "rb"),
  purpose="fine-tune"
)