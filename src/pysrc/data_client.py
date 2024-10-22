class DataClient:

    def __init__(self):
        raise NotImplementedError

    def _query_api(self) -> None:
        raise NotImplementedError

    def _parse_message(self, message):
        raise NotImplementedError

    def get_data(self):
        raise NotImplementedError
