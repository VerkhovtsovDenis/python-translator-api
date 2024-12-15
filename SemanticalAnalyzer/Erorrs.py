class RedeceredIdError(Exception):
    MESSAGE = "Semantic error, Re-declared identifier '{id}'."

    def __init__(self, id: str):
        super().__init__(self.MESSAGE.format(id=id))
