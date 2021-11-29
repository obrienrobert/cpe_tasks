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
2. Create the `config.toml` file. Please see the Fedora messaging [quick start](https://fedora-messaging.readthedocs.io/en/stable/quick-start.html) for more info on configuration:
```
sed -e "s/[0-9a-f]\{8\}-[0-9a-f]\{4\}-[0-9a-f]\{4\}-[0-9a-f]\{4\}-[0-9a-f]\{12\}/$(uuidgen)/g" message_consumer/fedora.toml > message_consumer/config.toml
```

3. Running the `anitya_messages.py` script will print messages from the `org.release-monitoring.prod.anitya.project.version.update.v2` topic to your console

### 3. Code Maintenance
I would use a top-down approach:
1. Study the repository from a high level to help understand what it does, and try to get it running locally or in a development environment to get familiar with it initially
2. Ask the previous maintainer for some context around the project to help answer questions such as why was the programming language of choice chosen, what state is the project currently in, etc.
3. Map out the individual components of the project to understand what they are, how to interact, and how they come together to create the overall architecture (existing architecture documentation would be helpful here)
4. Learn the language the project uses, if not already familiar
5. Learn by doing: take on a smaller or easier issue such as a bug fix

### 4. Deployment
> _what considerations do you give as to how the app is deployed_

The type of application is an important factor here. I.e. is it container based, or file based? Some common considerations would be:
1. Who is deploying the application (what team etc.)
2. Is there a deployment strategy in place to help minimise downtime
3. What a processes are in place (CI/CI or release gating) for deploying the application
4. How are rollbacks handled if one is required

> _and does this effect how you write your code or documentation?_

Yes, as the deployment method could be affect the application process depending on how it is implemented:

1. If the code comprises connections to databases/external resources, these need to be taken into consideration if the deployment strategy closes these connections (using retries for example)
2. The application code should be able to handle both rollbacks and upgrades using the deployment method
3. The application should take the method of deployment into account and be developed in a manner that supports it. E.g. blue/green deployments 
4. If the deployment method doesn't support zero downtime, this might require end-users to log back into and authenticate with the application. which should be documented, and end-users notified

### 5. Troubleshooting

Assuming nothing has changed on my end:

> _What things would you ask the server admin to check_
1. That the password to the server I am connecting to was not rotated/changed
2. There is no ongoing maintenance on the server
3. My public key exists on the server

> _what information would you provide to them_
1. The details of the server I am attempting to connect to
2. The error received when trying to connection. E.g. `ssh permission denied (publickey)`
3. The last time I was able to successfully connect to the server, if known
