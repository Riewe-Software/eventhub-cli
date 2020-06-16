# Eventhub CLI

## Installation
`pip install eventhub-cli`

## Usage
### `push`: Uploading an event-file
Example:
```
eventhub-cli push test_event_file.json -e ... -p .. -o ... -w ...
```
Options:
```
Usage: eventhub-cli push [OPTIONS] EVENT_FILE

Options:
  -e, --email TEXT         Your email
  -p, --password TEXT      Your password
  -w, --workspace TEXT     Your workspace name
  -o, --organization TEXT  Your organization name
  --endpoint TEXT          Eventhub endpoint
  --help                   Show this message and exit.
```