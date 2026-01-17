from os import environ


class Config(object):
    creds: "Creds"

    def __init__(self) -> None:
        self.creds = Creds()


class Creds(object):
    url: str
    key: str

    def __init__(self) -> None:
        URL_DOCX = environ.get("URL_DOCX")
        API_KEY = environ.get("API_KEY")

        assert type(URL_DOCX) is str, "URL_DOCX is not set"
        assert type(API_KEY) is str, "API_KEY is not set"

        self.url = URL_DOCX
        self.key = API_KEY

config = Config()
