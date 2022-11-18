'''
Convert input integer into a sentence of:
XX hours, XX minutes and XX seconds
with correct second or seconds.
'''

# test input
inp = 613252352


def helper_to_ten_to_word(n):
    """
    Takes a number from one to 9 and turns it into a word
    :param n: integer
    :return: string
    """
    numb_dict = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    return numb_dict[str(n)]


def helper_msg_maker(time_value=0, time_type_multiple='seconds'):
    # if 0 then return nothing
    if time_value == 0:
        return None
    # the format of txt endings
    if time_value == 1:
        msg = time_type_multiple[0:len(time_type_multiple) - 1]
    else:
        msg = time_type_multiple

    # words for 1 to 9
    if 1 <= time_value <= 9:
        time_value = helper_to_ten_to_word(time_value)

    return f'{time_value} {msg}'


def get_time_in_words(number):
    """
    convert a number input in seconds
    to hours, minutes, seconds
    :param number: int, seconds
    :return: string, text
    """

    # challenge task: extend to days and weeks
    # there are 24 hrs in a day
    # 24 x 60 = 1440 minutes in a day
    # 1440 x 60 = 86 400 seconds in a day

    # 24 x 7 = 168 hours in a week
    # 168 x 60 = 10 080 minutes in a week
    # 10080 x 60 = 604 800 seconds in a week

    weeks = number // 604800
    seconds_left = number - (weeks * 604800)
    days = seconds_left // 86400
    seconds_left -= (days * 86400)

    # there are 60 seconds in a minute,
    # 60 x 60 = 3600 seconds in an hour
    hours = seconds_left // 3600
    seconds_left -= (hours * 3600)
    minutes = seconds_left // 60
    seconds = seconds_left - (minutes * 60)

    msg1 = helper_msg_maker(hours, 'hours')
    msg2 = helper_msg_maker(minutes, 'minutes')
    msg3 = helper_msg_maker(seconds, 'seconds')
    msg4 = helper_msg_maker(weeks, 'weeks')
    msg5 = helper_msg_maker(days, 'days')

    # gather all valid texts for the output msg
    final_msg = []
    for message in [msg4, msg5, msg1, msg2, msg3]:
        if message is not None:
            final_msg.append(message)


    # if 3 or more in the output, need o say and.
    if len(final_msg) > 1:
        final_msg.insert(-1, 'and ')

    final_msg_txt = ''
    for i in range(len(final_msg)):
        # if first then add itself
        if i == 0 or i == len(final_msg) - 1:
            final_msg_txt += final_msg[i]
        # else add a comma
        else:
            final_msg_txt += ', ' + final_msg[i]

    # alternative to the above to do it faster
    txt = str.join(', ', final_msg).replace('and ,', 'and')

    if len(final_msg) == 3:
        final_msg_txt = final_msg_txt.replace(',', '')

    return final_msg_txt, txt


print(get_time_in_words(inp))
