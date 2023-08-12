#!/usr/bin/env python3

# Imports
import os
# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import SystemMessage, HumanMessagePromptTemplate

# Setup 
key = os.environ["OPENAI_API_KEY"]


template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "You are a helpful assistant that re-writes the user's text to "
                "sound more upbeat."
            )
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)

llm = ChatOpenAI(temperature=0.9)
out = llm(template.format_messages(text='i hate the weather today.'))
print(out)