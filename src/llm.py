# This will serve an example of the structure for future provider implementation
# groq_init(), groq_send_message(), groq_list_models(free/paid/all), etc 

from groq import Groq
from os import environ
# TESTING
from dotenv import load_dotenv
# TESTING
load_dotenv()

def groq_init():
    # I am not sure if either passing the API key to groq_init() 
    # or directly fetching the API key via environ is better
    # TODO: change this after implementing proper API key processing
    api_key = environ.get("TEST_GROQ_KEY")
    if api_key:
        client = Groq(api_key=api_key)
        return client
    else:
        # TODO: setup custom class for MissingApiKeyError exception
        raise ValueError("Please setup API key before attempting to initalize Groq cliwnr")

def groq_list_models(client):
    if not client:
        # TODO: setup custom class for MissingClientError exception
        raise ValueError("Please initalize Groq client before attempting to fetch available models")
    
    # Just return their programmatic names/ids
    models = [model.id for model in client.models.list().data]

    return models