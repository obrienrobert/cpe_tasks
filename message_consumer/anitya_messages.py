from fedora_messaging import api, config

config.conf.setup_logging()

# config.toml contains the configuration required for the public Fedora message broker
# More info on configuration values can be found here:
# https://fedora-messaging.readthedocs.io/en/stable/configuration.html
config.conf.load_config("message_consumer/config.toml")


# The callback function used to print messages retrieved from the topic and print them the console
def print_messages(message):
    print(message)


api.consume(print_messages)
