import random
import string

chars=string.ascii_lowercase + string.digits

def create_shortcode(instance, size=6 ):
    new_code = ''
    for _ in range(size):
        new_code += random.choice(chars)

    instance_class = instance.__class__
    qs_exists = instance_class.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code