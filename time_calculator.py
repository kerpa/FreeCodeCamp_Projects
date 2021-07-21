def get_start_time_minute(starting_string):
    if len(starting_string) == 8:
        start_a = int(starting_string[:2]) * 60
        start_b = int(starting_string[3:5])
        return start_a + start_b
    elif len(starting_string) == 7:
        start_a = int(starting_string[:1]) * 60
        start_b = int(starting_string[2:4])
        return start_a + start_b


def get_added_time_minute(duration_string):
    if len(duration_string) == 5:
        start_a = int(duration_string[:1]) * 60
        start_b = int(duration_string[3:5])
        return start_a + start_b
    elif len(duration_string) == 4:
        start_a = int(duration_string[:1]) * 60
        start_b = int(duration_string[3:4])
        return start_a + start_b


def get_times_hour_minutes(time_in):
    time_type_1 = str(time_in // 60) + ':' + str(time_in % 60)
    time_type_2 = str(time_in // 60) + ':0' + str(time_in % 60)
    if time_in % 60 > 9:
        return time_type_1
    elif time_in % 60 <= 9:
        return time_type_2


def get_time_added_am_or_pm(starting_string):
    if starting_string[-2:] == 'AM':
        return 0
    elif starting_string[-2:] == 'PM':
        return 12 * 60


def add_time(start, duration):
    time_total_minute = get_start_time_minute(start) + get_added_time_minute(duration)
    return get_times_hour_minutes(time_total_minute)


print(add_time("11:06 PM", "2:02"))
