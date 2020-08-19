import main


def handler(event, context):
    return {
  "payload": {
    "google": {
      "expectUserResponse": False,
      "richResponse": {
        "items": [
          {
            "simpleResponse": {
              "textToSpeech": "Your current balance is {}".format(main.get_gas_balance())
            }
          }
        ]
      }
    }
  }
}