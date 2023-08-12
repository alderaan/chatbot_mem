# Chatbot with memory
Building a simple LLM chatbot with memory, leveraging langchain.
Refer to [this page](https://python.langchain.com/docs/modules/memory/) for an introduction on how to handle memory for llm based chatbots. 


## Setup
- Make sure environment variable `OPENAI_API_KEY` is set to your OpenAI API Key. For example, export it directly in your ~/.zsrh:
    - Just add `export OPENAI_API_KEY='enter_your_key_here'` to the end of your ~/.zshrc and execute `source ~/.zshrc in your terminal`.
- Make sure Conda is installed.
- Run `make env_create`.
- Run `conda activate chatbot_mem`.
- Run `python bot.py`.


