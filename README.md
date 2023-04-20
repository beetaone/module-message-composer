# Message Composer

|                |                                                                                         |
| -------------- | --------------------------------------------------------------------------------------- |
| Name           | Message Composer                                                                        |
| Version        | v1.1.0                                                                                  |
| Dockerhub Link | [weevenetwork/message-composer](https://hub.docker.com/r/weevenetwork/message-composer) |
| authors        | Jakub Grzelak                                                                           |

- [Message Composer](#message-composer)
  - [Description](#description)
    - [Supported Utils Functions](#supported-utils-functions)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

This module enables a customized composition of messages, in example alert messages that can be later passed to the next module like Slack Alert which would further pass it to the selected Slack endpoint channel. To include some data in the message use double curly brackets and provide a desired label like `{{ label_name }}`. To use one of the supported utils functions to add extra information to your message, use double curly brackets and prefix `utils.` before the name of the function you want to apply `{{ utils.function_name }}` (see Supported Utils Functions section below).

For instance, if we expect to receive data in the following format:
```json
{
    "temperature": 12,
    "volume": 375,
    "location": "Berlin"
}
```

and if we have our Message Label set to `alertMessage` and our Message Content variable is set to the following:

`Device {{utils.getNodeName}} (in {{location}}) measured temperature {{temperature}} on {{utils.getDateAndTime}}`

then the output of the module will be:

```json
{
    "alertMessage": "Device Kunbus (in Berlin) measured temperature 12 on 2022-09-25 15:35:17.31234"
}
```

### Supported Utils Functions

| Function Name  | Description                                                                              |
| -------------- | ---------------------------------------------------------------------------------------- |
| getNodeName    | Returns the name of the node on which the module is running.                             |
| getNodeID      | Returns the ID of the node on which the module is running.                               |
| getDateAndTime | Returns the current date and time in the following format: `YYYY-MM-DD HH:MM:SS.mmmmmm`. |
| getDate        | Returns the current date in the following format: `YYYY-MM-DD`.                          |
| getTime        | Returns the current time in the following format: `HH:MM:SS.mmmmmm`.                     |
| getTimestamp   | Returns the number of seconds since the Unix epoch.                                      |


## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name            | Environment Variables | type   | Description                                                                                                                                         |
| --------------- | --------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Message Content | MESSAGE_CONTENT       | string | Message content. Use double curly brackets to access labels from your data (i.e. to access data assigned to temperature label use {{temperature}}). |
| Message Label   | MESSAGE_LABEL         | string | Label to assign message to in the output JSON object.                                                                                               |


### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output) |
| EGRESS_URLS           | string | HTTP ReST endpoints for the next module        |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
requests
```

## Input

Input to this module is:

* JSON body single object, example:

```json
{
    "temperature": 12,
    "volume": 375,
    "location": "Berlin"
}
```

## Output

Output of this module is (assuming Message Content is `Device {{utils.getNodeName}} (in {{location}}) measured temperature {{temperature}} on {{utils.getDateAndTime}}`)

* JSON body single object, example:

```json
{
    "alertMessage": "Device Kunbus (in Berlin) measured temperature 12 on 2022-09-25 15:35:17.31234"
}
```
