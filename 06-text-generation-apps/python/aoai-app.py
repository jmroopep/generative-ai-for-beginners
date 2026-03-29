# pylint: disable=all
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# validate required environment variables
required_vars = ['AZURE_OPENAI_ENDPOINT', 'AZURE_OPENAI_API_KEY', 'AZURE_OPENAI_DEPLOYMENT']
missing_vars = [var for var in required_vars if not os.environ.get(var)]

if missing_vars:
    print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
    print("Please configure these variables in your .env file")
    exit(1)

# configure Azure OpenAI service client 
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"], 
  api_key=os.environ['AZURE_OPENAI_API_KEY'],  
  api_version = "2024-02-01"
#  api_version = "2023-05-15"
  )

deployment = os.environ['AZURE_OPENAI_DEPLOYMENT']

# add your completion code
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]  

# make completion with error handling
try:
    completion = client.chat.completions.create(model=deployment, messages=messages)
    # print response
    print(completion.choices[0].message.content)
except Exception as e:
    print(f"Error calling Azure OpenAI: {e}")
    print(f"Deployment: {deployment}")
    print(f"Endpoint: {os.environ['AZURE_OPENAI_ENDPOINT']}")
    exit(1)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.