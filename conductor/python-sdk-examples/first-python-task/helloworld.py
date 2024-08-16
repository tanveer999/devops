from conductor.client.automator.task_handler import TaskHandler
from conductor.client.configuration.configuration import Configuration
from conductor.client.workflow.conductor_workflow import ConductorWorkflow
from conductor.client.workflow.executor.workflow_executor import WorkflowExecutor
from greetings_workflow import greetings_workflow

def register_workflow(workflow_executor: WorkflowExecutor) -> ConductorWorkflow:
    workflow = greetings_workflow(workflow_executor=workflow_executor)
    workflow.register(True)
    return workflow

def main():
    api_config = Configuration(server_api_url='http://localhost:8080/api')

    workflow_executor = WorkflowExecutor(configuration=api_config)
    
    workflow = register_workflow(workflow_executor)

    task_handler = TaskHandler(configuration=api_config)
    task_handler.start_processes()

    # workflow_run = workflow_executor.execute(name=workflow.name, version=workflow.version, workflow_input={'name': 'World'})

    # print(f'\nworkflow result: {workflow_run.output["result"]}')
    # print(f'see the workflow execution here: {api_config.ui_host}/execution/{workflow_run.workflow_id}')
    # task_handler.stop_processes()

if __name__ == '__main__':
    main()