#!/usr/bin/env python3

# Imports
import os
from langchain.llms import OpenAI

# Setup 
key = os.environ["OPENAI_API_KEY"]
llm = OpenAI(temperature=0.9, openai_api_key=key)

# Call API
out = llm.predict("How are you?")
print(out)