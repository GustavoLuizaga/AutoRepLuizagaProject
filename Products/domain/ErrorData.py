"""
Custom exception that represents an error related to the validity or consistency of data within the domain.
This exception should be thrown when the data received or manipulated does not comply with the business rules or fundamental validations of the domain model.
"""

class ErrorData(Exception):
    pass