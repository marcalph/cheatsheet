from contextlib import contextmanager
import logging

@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


# with log_level(logging.DEBUG, 'my-log') as logger:
#     logger.debug(f'This is a message for {logger.name}!')
#     logging.debug('This will not print')


