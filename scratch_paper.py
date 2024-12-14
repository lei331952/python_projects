# from words import fetch_words, print_words

# print_words(fetch_words('http://sixty-north.com/c/t.txt'))


def new_decorator(func):

    def wrap_func():

        print('before executing func()')

        func()

        print('excute after the func()')

    return wrap_func


@new_decorator
def func_needs_decorator():
    print('func')


# func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()
