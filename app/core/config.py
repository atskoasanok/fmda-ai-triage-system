import os

from dotenv import load_dotenv


load_dotenv()


class Settings:

    def __init__(self):

        self.APP_NAME = "FMDA"

        self.OPENAI_API_KEY = os.getenv(
            "OPENAI_API_KEY",
            ""
        )

        self.MODEL_NAME = os.getenv(
            "MODEL_NAME",
            "gpt-4o-mini"
        )

        self.USE_MOCK = os.getenv(
            "USE_MOCK",
            "true"
        ).lower() == "true"

        self.TEMPERATURE = float(
            os.getenv(
                "TEMPERATURE",
                "0.3"
            )
        )


settings = Settings()
