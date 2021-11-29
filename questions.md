Answers for the CPE role questions
==

Original 

## 1. Development

* Write an API (of your choice) in Python framework (of your choice) that accepts
    * Timezone
    * Hour
    * Minute

and converts it in UTC time. (When no parameter is passed, take localtime to convert in UTC)
example: 
`curl http://127.0.0.1:5000/?tz=Europe/Paris&hr=10&min=5`

you are passing time = 10:05 in Paris
it should return 08:05 UTC

> * Please use libraries to convert timezones instead of attempting to write a logic for timezone conversion 

## 2. Working with Fedora messaging
Fedora-messaging is the main messaging service used for Fedora Infrastructure https://fedora-messaging.readthedocs.io/en/stable/index.html

Write a basic script which consumes all messages from the queue with the topic `org.release-monitoring.prod.anitya.project.version.update.v2` and print them to the console

## 3. Code Maintenance
You are given an application to take over from another developer and become the main maintainer. What steps would you take to familiarise yourself with the code?

## 4. Deployment
When writing an application what considerations do you give as to how the app is deployed and does this effect how you write your code or documentation?

## 5. Troubleshooting
You are unable to login to a remote server with ssh, you get 'Permission denied'. What things would you ask the server admin to check for you and what information would you provide to them?







