import sys
from src.logger import logging

def get_error_message(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script [{0}] line number [{1}]   message [{2}]".format(
        filename,exc_tb.tb_lineno,str(error))

    return error_message
    


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = get_error_message(error_message,error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message
    


        
    