import time

def load_binary_image(image_path) :
    b_image = open(image_path, 'rb')
    return b_image

def profile_function_time(function):
    def wrap(*args):
        time1 = time.time()
        response = function(*args)
        time2 = time.time()
        print('%s:\t%0.3f' % (function.func_name, time2-time1))
        return response
    return wrap