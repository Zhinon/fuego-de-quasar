def get_message(messages_list):
    """
    This method receives list with 3 list of string.
    It returns an string with the decoded message.

    Note: Messages could have gaps at the beggining.

    >>> get_message([
        ["Este", " ", " ", "mensaje"],
        [" ", " ", "es", " ", "mensaje"],
        [" ", " ", " ", " ", " ", "un", " "],
    ])
    "Este es un mensaje"
    """

    msg_one = messages_list[0][::-1]
    msg_two = messages_list[1][::-1]
    msg_three = messages_list[2][::-1]

    final_msg_len = min(len(msg_one), len(msg_two), len(msg_three))
    final_msg = []


    for counter in range(final_msg_len):
        final_word_set = set([msg_one[counter], msg_two[counter], msg_three[counter]])
        final_word_set.remove(' ')
        if len(final_word_set) != 1:
            raise Exception
        final_word = final_word_set.pop()
        final_msg.append(final_word)

    return ' '.join(final_msg[::-1])
