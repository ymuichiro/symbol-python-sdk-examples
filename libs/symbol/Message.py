class Message:
    @staticmethod
    def plain(message: str) -> bytes:
        return bytes([0]) + message.encode("utf-8")
