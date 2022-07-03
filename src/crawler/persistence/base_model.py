class BaseModel:

    def from_dict(self, dictionary):
        """
        Maps dictionary to properties of the object
        """
        for key, value in dictionary.items():
            setattr(self, key, value)
