import timeit

def load_binary_image(image_path) :
    b_image = open(image_path, 'rb')
    return b_image

def profile_function_time(function) :
    start = timeit.default_timer()
    response = function
    end = timeit.default_timer()

    time = end-start
    return response, time