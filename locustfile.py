import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def first_test(self):
        self.client.get("/user/222")
        self.client.get("/city/London/users")

