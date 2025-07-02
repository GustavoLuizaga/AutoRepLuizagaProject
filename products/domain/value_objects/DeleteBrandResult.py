from enum import Enum

class DeleteBrandResult(Enum):
    DELETED = "deleted"
    NOT_FOUND = "not_found"
    HAS_PRODUCTS = "has_products"
