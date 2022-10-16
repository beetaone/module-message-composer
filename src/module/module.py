"""
This file implements module's main logic.
Data processing should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from .params import PARAMS
from module import moduleUtils
import re

log = getLogger("module")

def module_main(received_data: any) -> [any, str]:
    """
    Process received data by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        any: Processed data that are ready to be sent to the next module or None if error occurs.
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Processing ...")

    try:
        output_message = PARAMS["MESSAGE_CONTENT"]

        for label in [x[2:-2] for x in re.findall("{{.*?}}", PARAMS["MESSAGE_CONTENT"])]:
            if label.startswith("utils."):
                # emplace function results into the output message
                output_message = output_message.replace("{{" + label + "}}", str(getattr(moduleUtils, label[6:])()))
            else:
                # emplace data into the output message
                output_message = output_message.replace("{{" + label + "}}", str(received_data[label]))

        processed_data = {
            PARAMS["MESSAGE_LABEL"]: output_message
        }

        return processed_data, None

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"
