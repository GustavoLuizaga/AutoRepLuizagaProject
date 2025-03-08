
class BrandValidatorDataUpdate:
    def __init__(self, new_data: str):
        self.new_data = new_data

    def is_valid_name(self) -> bool:
        name = self.new_data.get("name")
        return isinstance(name, str) and bool(name.strip())