from conductor.client.worker.worker_task import worker_task
import time

@worker_task(task_definition_name='greet')
def greet(name: str) -> str:
    sleep_time = 15
    print(f'Running greet task and sleep for {sleep_time}')
    time.sleep(sleep_time)
    return f'Hello {name}'
