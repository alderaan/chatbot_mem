#!/usr/bin/env python3

"""
Name:                   bot_simple
Memory:                 No
Continued Conversation: No
"""

# IMPORTS
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import SystemMessage, HumanMessagePromptTemplate

# MAIN
template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "You are an executive coach, helping the user to achieve "
                "mental, physical and professional peak performance."
            )
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)

llm = ChatOpenAI(temperature=0.9)

print("What's up?")
input = input()
output = llm(template.format_messages(text=input))
print(output)