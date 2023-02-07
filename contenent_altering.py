def status(arg: bytes):
    first_header = arg.split(b'\r')[0]
    status = first_header.split(b' ')
    status_code = status[1]
    if len(status) > 3:
        status_phrase = status[2] + (b' ') + status[3]
    else:
        status_phrase = status[2]
    # We put them in type string to be concatenate more easily
    status_code_str = status_code.decode(encoding="UTF-8")
    status_phrase_str = status_phrase.decode(encoding="UTF-8")
    print("The answer of the HTTP request is: ")
    print(status_code_str, status_phrase_str)


def text_modification(arg: bytes):
    data_modified = arg.replace(b"Stockholm", b"Linkoping")
    data_modified = data_modified.replace(b"Smiley", b"Trolly")
    return data_modified
