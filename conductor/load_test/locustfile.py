from locust import HttpUser, task, between

class APIUser(HttpUser):
    # wait_time = between(1, 5)  # Time between tasks (in seconds)

    @task
    def post_request(self):
        # The POST request with empty JSON body
        self.client.post("/api/workflow/demo_http?priority=0", json={})

