def make_snippet(string):
    string_elements = string.split()
    if len(string_elements) <= 5:
        return string
    else:
        return " ".join(string_elements[0:5]) + '...'