"""
Validates whether the incoming data has an acceptable type and structure.

Edit this file to verify data expected by you module.
"""

from logging import getLogger
from .params import PARAMS
from module import moduleUtils
import re

log = getLogger("validator")

# list of supported utils functions
supported_utils = []

# lists of required labels and functions
required_labels = []
required_functions = []

def validation_requirements():
    log.debug("Composing validation requirements ...")

    global supported_utils
    global required_labels
    global required_functions

    try:
        # make a list of supported utils functions
        supported_utils = [("utils." + func) for func in dir(moduleUtils) if not func.startswith('__') and func != "datetime" and func != "time"]
        log.debug(f"SUPPORTED UTILS: {supported_utils}")

        # make a list of required functions or labels that will be later replaced in the message content text
        for label in [x[2:-2] for x in re.findall("{{.*?}}", PARAMS["MESSAGE_CONTENT"])]:
            if label.startswith("utils."):
                required_functions.append(label)
            else:
                required_labels.append(label)

        log.debug(f"REQUIRED FUNCTIONS: {required_functions}")
        log.debug(f"REQUIRED LABELS: {required_labels}")

        detected_unsupported_functions = list(set(required_functions) - set(supported_utils))
        if detected_unsupported_functions:
            return f"Detected calls to the following unsupported functions in Message Content: {detected_unsupported_functions}"

        return None

    except Exception as e:
        return f"Exception when composing validation requirements: {e}"


def data_validation(data: any) -> str:
    """
    Validate incoming data i.e. by checking if it is of type dict or list.
    Function description should not be modified.

    Args:
        data (any): Data to validate.

    Returns:
        str: Error message if error is encountered. Otherwise returns None.

    """

    log.debug("Validating ...")

    try:
        allowed_data_types = [dict]

        if not type(data) in allowed_data_types:
            return f"Detected type: {type(data)} | Supported types: {allowed_data_types} | invalid!"
        else:
            # check if all labels required in Message Content are present in the received data
            missing_labels = list(set(required_labels) - set(data.keys()))
            if missing_labels:
                return f"The following data labels included in Message Content were not found in received data: {missing_labels}"

        return None

    except Exception as e:
        return f"Exception when validating module input data: {e}"
