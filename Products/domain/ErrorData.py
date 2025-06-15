"""
Custom exception that represents an error related to the validity or consistency of data within the domain.
This exception should be thrown when the data received or manipulated does not comply with the business rules or fundamental validations of the domain model.
"""

class ErrorData(Exception):
    pass

class NotFoundError(ErrorData):
    pass
    """Error para indicar que un recurso no fue encontrado."""

class InvalidDataError(ErrorData):
    pass
    """Error para indicar que los datos son inválidos."""