def timerange_to_minutes(t_str):
    """
    Return amount of minutes for the time ranges in HH:MM format
    :param t_str:
    :return:
    """

    hour = int(t_str.split(":")[0])
    minutes = int(t_str.split(":")[1])
    hour_to_minutes = hour * 60
    return hour_to_minutes + minutes
