from os import getenv

PARAMS = {
    "MESSAGE_CONTENT": getenv("MESSAGE_CONTENT", "Sample message"),
    "MESSAGE_LABEL": getenv("MESSAGE_LABEL", "alertMessage"),
}
