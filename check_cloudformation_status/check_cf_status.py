import sys
import time
import boto3

def check_stack_status(stack_name):
    cloudformation = boto3.client('cloudformation')

    try:
        response = cloudformation.describe_stacks(StackName=stack_name)
        stack = response['Stacks'][0]
        stack_status = stack['StackStatus']
        return stack_status

    except Exception as e:
        print(f"Failed to check stack status: {str(e)}")
        return None

def terminate_stack(stack_name):
    cloudformation = boto3.client('cloudformation')

    try:
        cloudformation.delete_stack(StackName=stack_name)
        print(f"Terminating stack: {stack_name}")

    except Exception as e:
        print(f"Failed to terminate stack: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_cf_status.py <stack_name>")
        sys.exit(1)

    stack_name = sys.argv[1]
    terminate_attempts = 3
    terminate_interval = 30  # seconds

    while True:
        stack_status = check_stack_status(stack_name)
        print(f"Stack Status: {stack_status}")

        if stack_status in ['CREATE_FAILED', 'ROLLBACK_FAILED', 'DELETE_FAILED']:
            print("Stack deployment failed. Exiting...")
            sys.exit(1)

        if stack_status in ['CREATE_COMPLETE', 'UPDATE_COMPLETE']:
            print("Stack deployment successful. Exiting...")
            sys.exit(0)

        if stack_status in ['ROLLBACK_COMPLETE']:
            print("Stack deployment failed. Rollback completed. Exiting...")
            sys.exit(1)

        if stack_status in ['UPDATE_ROLLBACK_FAILED', 'ROLLBACK_FAILED']:
            print("Stack deployment failed. Rollback failed. Exiting...")
            sys.exit(1)

        if stack_status in ['UPDATE_ROLLBACK_COMPLETE']:
            print("Stack deployment failed. Rollback completed. Exiting...")
            sys.exit(1)

        if stack_status in ['CREATE_IN_PROGRESS', 'UPDATE_IN_PROGRESS', 'DELETE_IN_PROGRESS']:
            # If the stack is stuck, attempt to terminate it
            if terminate_attempts > 0:
                terminate_stack(stack_name)
                terminate_attempts -= 1
            else:
                print("Stack is stuck and termination attempts exhausted. Exiting...")
                sys.exit(1)

        time.sleep(30)  # Wait for 30 seconds before polling again
