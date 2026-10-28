# This will serve an example of the structure for future provider implementation
# groq_init(), groq_send_message(), groq_list_models(free/paid/all), etc 

from groq import Groq, NotFoundError
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
    # Direct model ID is used because it is mostly readable and can be directly passed to Groq for model-related operations
    models = [model.id for model in client.models.list().data]

    return models

def groq_send_message(client, model_id, message):
    if not client:
        # TODO: use MissingClientError here when implemented
        raise ValueError("Please initialize Groq client before attempting to send messages to a model")

    if not model_id:
        raise ValueError("Please pass a model ID before attempting to send messages to a model")

    # TODO: add streaming support
    # TODO: context window
    try:
        completion = client.chat.completions.create(
            messages=[
                {"role":"user", "content":message}
            ],
            model=model_id
        )
    except NotFoundError as e:
        # TODO: setup custom class InvalidModelIdError exception
        raise ValueError(f"Please specific a valid model, \"{model_id}\" is not valid.")
    return completion.choices.message.content