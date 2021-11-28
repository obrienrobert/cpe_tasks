## Answers for the CPE role questions
The repository contains answers to the questions outlined in the [questions.md](questions.md) file.

### 1. Development
The code for this task is located in the `utc_conversion` folder.

The `utc_time_conversion.py` script can be verified using the following commands:
```
curl http://127.0.0.1:5000
# Expected result: local UTC time

curl http://127.0.0.1:5000/?tz=Europe/Paris
# Expected result: UTC time of the given time zone.
```
### 2. Working with Fedora messaging
The code for this task is located in the `message_consumer` folder. Retrieving messages from the public Fedora broker requires the creation of a config file which contains the required authentication and configuration values.

1. Run the following command to get the `pem` files required to authenticate:
```
curl https://raw.githubusercontent.com/fedora-infra/fedora-messaging/stable/configs/cacert.pem -o message_consumer/cecert.pem && \
curl https://raw.githubusercontent.com/fedora-infra/fedora-messaging/stable/configs/fedora-key.pem -o message_consumer/fedora-key.pem && \
curl https://raw.githubusercontent.com/fedora-infra/fedora-messaging/stable/configs/fedora-cert.pem -o message_consumer/fedora-cert.pem
```
2. Create the `config.toml` file:
```
sed -e "s/[0-9a-f]\{8\}-[0-9a-f]\{4\}-[0-9a-f]\{4\}-[0-9a-f]\{4\}-[0-9a-f]\{12\}/$(uuidgen)/g" message_consumer/fedora.toml > message_consumer/config.toml
```

3. Running the `anitya_messages.py` script will print messages from the `org.release-monitoring.prod.anitya.project.version.update.v2` topic being printed to your console

### 3. Code Maintenance
I would use a top-down approach:
1. Study the repository from a high level to help understand what it does, and try to get it running locally or in a development environment to get familiar with it initially
2. Ask the previous maintainer for some context around the project to help answer questions such as why was the programming language of choice chosen, what state is the project currently in, etc.
3. Map out the individual components of the project to understand what they are, how to interact, and how they come together to create the overall architecture (existing architecture documentation would be helpful here)
4. Learn the language the project uses, if not already familiar
5. Learn by doing: take on a smaller or easier issue such as a bug fix

### 4. Deployment

### 5. Troubleshooting
