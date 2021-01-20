# Locust Sample Test

Performance Testing has always been one complex test to automate where you need to use either grid or Master/Slave set up for running the distributed test.

If you are interested in using Python for putting together your Performance Test Framework, Locust is a good open source tool which allow you to start with initial set up for API based performance tests simulation quite easily.


# Minimum requirement

1.Python Version 3.6 or any higher latest version

Download python 3.6 or higher version from Python org - https://www.python.org/downloads/release/python-360/
If don't have 3.6 or higher on your Machine.


# Steps to Implement

Install Locust using pip.

$ pip3 install locust
Validate your installation and show the Locust version number:

$ locust -V

Automated Test:

Simple Test to Hit Host : http://bpdts-test-app-v2.herokuapp.com
 with Multiple Get Requests for 1. specific User search and 2. specific city (i.e. London) specific Users.

Load Test Pattern:
Check test script : locustfile.py for get requests.

Quick Test:

  Run below command in the same directory where you have downloaded this repo specific data and make sure locustfile.py is in your current directory:

$ locust

  If your Locust file is located somewhere else, you can specify it using -f

$ locust -f locust_files/my_locust_file.py

Access Locust’s web interface :
Once you’ve started Locust using one of the above command lines, you should open up a browser and point it to http://127.0.0.1:8089

Fill out the form and try it out!

Sample Run specific Data -

      Number of total users to simulate
        1000 or any number of users to play around.

      Spawn rate (users spawned/second)
        2 or any other spawn rate to play around.

      Host (e.g. http://www.example.com)
        http://bpdts-test-app-v2.herokuapp.com

Checks you are getting success response and user are building up as per the load trend you set in Locust web Interface running on Host : http://127.0.0.1:8089

As we mostly used to have requirement of running distributed Load test where load test needs to be simulated from multiple machines and collated test trend can be monitored from Master, we can achieve the same with Locust as well with docker compose and docker run commands

Running distributed Test:

Note: Make sure you have docker installed on your machine (Chose mac or Windows whatever applicable to you) from the Docker official site - https://www.docker.com/
 If you already have docker installed ignore this step.

Run the same Test script (i.e. locustfile.py) from docker image.

docker run -p 8089:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py

Run workers through docker compose (4 workers chosen, you change this to play around)

docker-compose up --scale worker=4

Locust’s web interface :
Once you’ve started Locust using one of the above command lines, you should open up a browser and point it to http://127.0.0.1:8089

Fill out the form and try it out!

Sample Run specific Data -

      Number of total users to simulate
        1000 or any number of users to play around.

      Spawn rate (users spawned/second)
        2 or any other spawn rate to play around.

      Host (e.g. http://www.example.com)
        http://bpdts-test-app-v2.herokuapp.com

Checks you are getting success response and user and building up as per the load trend you set in Locust web Interface running on Host : http://127.0.0.1:8089

# Documentation

Test file: locustfile.py
Docker: docker-compose.yml
Report: Check Locust Dashboard and Console output once test run stopped.

# Help

Send your questions to the
- [rudraksh awasthy - rudraksh_awasthy@yahoo.com]

Refer standard Locust documentation 	
- [https://docs.locust.io/en/stable/index.html]
