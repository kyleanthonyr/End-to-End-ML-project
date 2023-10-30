import sys

# Designs custom exceptions for package


def error_message_detail(error, error_detail: sys):
    '''This function is a wrapper for errors outputted from sys for better readability.'''
    _, _, exc_tb = error_detail.exc_info()  # gets error name, line num and detail

    filename = exc_tb.tb_frame.f_code.co_filename

    error_message = "The error occurred in Python script name {0} on line # {1}. Error message: {2}".format(
        filename, exc_tb.tb_lineno, str(error)
    )

    return error_message


class customException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
