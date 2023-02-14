def status(arg: bytes):
#function to get the status code and the status phrase from the HTTP answer
    first_header = arg.split(b'\r')[0]
    status = first_header.split(b' ')
    status_code = status[1]
    # In the case the status phrase is in too part like "Not Modified"
    if len(status) > 3:
        status_phrase = status[2] + (b' ') + status[3]
    else:
        status_phrase = status[2]
    # We put them in type string to be concatenate them more easily
    status_code_str = status_code.decode(encoding="UTF-8")
    status_phrase_str = status_phrase.decode(encoding="UTF-8")
    #We finish by printing them
    print("The answer of the HTTP request is: ")
    print(status_code_str, status_phrase_str)


def text_modification(arg: bytes):
#function to do the content altering
    data_modified = arg.replace(b" Stockholm", b" Linkoping")
    data_modified = data_modified.replace(b" Smiley", b" Trolly")# modification inside the text
    data_modified = data_modified.replace(b"smiley", b"trolly")# for the image, we replace the corresponding string
    # inside the url of the image
    return data_modified




