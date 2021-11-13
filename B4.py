def get_name():
    return "mredul"

def get_address():
    return "khulna"


def get_info():
    name = get_name()
    address = get_address()
    return name, address


name, _ = get_info()
print(name)
print(get_info()[0])
print(get_info()[1])