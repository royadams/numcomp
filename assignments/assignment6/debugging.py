def search(text, pattern):
    """
    Takes a string and searches if the `pattern` is substring within `text`.
    :param text: A string that will be searched.
    :param pattern: A string that will be searched as a substring within
                    `text`.
    :rtype: The indices of all occurences of where the substring `pattern`
            was found in `text`.
    """

    pattern_length = len(pattern)
    text_length = len(text)
    offsets = []
    if pattern_length > text_length:
        return offsets
    bmbc = [pattern_length] * 256
    for index, char in enumerate(pattern[:-1]):
        bmbc[ord(char)] = pattern_length - index - 1
    bmbc = tuple(bmbc)
    search_index = pattern_length - 1
    while search_index < text_length:
        pattern_index = pattern_length - 1
        text_index = search_index
        while text_index >= 0 and \
                text[text_index] == pattern[pattern_index]:
            pattern_index -= 1
            text_index -= 1
        if pattern_index == -1:
            offsets.append(text_index + 1)
        search_index += bmbc[ord(text[search_index])]

    return offsets
    
if __name__=="__main__":
    text =  'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
             Fusce semper vestibulum nunc ut rhoncus. In ut tellus a \
             velit commodo ullamcorper quis non odio. Mauris bibendum \
             viverra condimentum. Ut porttitor, nisl eget dictum \
             rhoncus, ipsum lacus tristique felis, vitae rutrum nibh \
             ex tempor tortor. Proin condimentum felis id viverra \
             malesuada. Sed efficitur libero eu sagittis interdum. \
             Nullam tempor placerat felis rhoncus gravida.\
             Vivamus porta ornare interdum. Proin eu tempus neque, \
             viverra condimentum nibh. Maecenas a lacus vitae ex \
             aliquet tristique. Etiam et tincidunt lorem. Proin \
             ultrices accumsan euismod. Nullam sed leo erat. \
             Morbi massa neque, convallis non interdum vel, euismod.'
    search_string = 'felis'
             
    print(search(text,search_string))