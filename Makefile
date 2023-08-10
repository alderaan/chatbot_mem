# Variable for environment name
ENV_NAME = chatbot_mem

.PHONY: env_create env_activate env_remove

# Target to create the environment
env_create:
	conda env create -n $(ENV_NAME) -f environment.yml

# Target to activate the environment
env_activate:
	@echo "Note: Due to shell limitations, this Makefile cannot activate the environment directly."
	@echo "Please run the following command manually:"
	@echo "conda activate $(ENV_NAME)"

# Target to remove the environment
env_remove:
	conda env remove -n $(ENV_NAME)
