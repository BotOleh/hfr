import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log", filemode="w",
                    format="We have next logging message: "\
                           "%(asctime)s:%(levelname)s-%(message)s"
                    )
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

"""
>>> 2+2*28
"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()

def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
        result += _
    return result