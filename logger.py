import logging

logging.basicConfig(filename="debuglog/debug.log",
                    filemode="w",
                    format="[%(levelname)s]: %(message)s",
                    level=logging.DEBUG)

log = logging