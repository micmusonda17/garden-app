# Gardening advice app
# This program gives you gardening tips based on the season and the
# type of plant you are growing.

# Hardcoded values for the season and plant type
season = "summer"  # TODO: Replace with input() to allow user interaction.
plant_type = "flower"  # TODO: Replace with input() to allow user interaction.


def get_season_advice(season):
    """Work out the advice for the season the user is in.

    Args:
        season (str): The season, for example "summer" or "winter".

    Returns:
        str: The advice for that season.
    """
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """Work out the advice for the type of plant being grown.

    Args:
        plant_type (str): The plant type, for example "flower" or "vegetable".

    Returns:
        str: The advice for that plant type.
    """
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def get_advice(season, plant_type):
    """Put the season advice and the plant advice together.

    Args:
        season (str): The season the user is in.
        plant_type (str): The type of plant the user is growing.

    Returns:
        str: The full advice message.
    """
    advice = ""
    advice += get_season_advice(season)
    advice += get_plant_advice(plant_type)
    return advice


# print the advice out for the user
print(get_advice(season, plant_type))

# TODO: Examples of possible features to add:
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
