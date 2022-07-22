class Status:
    def __init__(self, id, status) -> None:
        self.id = id
        self.status = status

    def to_JSON(self):
        return{
            "status": self.status
        }