import os

def choose_gpt_model():
    # get model choices
    models = os.getenv('MODELS', 'gpt-3.5-turbo').split(',')

    # prepare the list that will print for user to select from
    model_choices = {str(i+1): model for i, model in enumerate(models)}

    # print the list to console
    print("\nSelect a model:")
    for key, value in model_choices.items():
        print(f"{key}: {value}")

    # get user input
    model_selection = input("Enter the number for the model you want to use: ")

    return model_choices.get(model_selection, 'gpt-3.5-turbo')