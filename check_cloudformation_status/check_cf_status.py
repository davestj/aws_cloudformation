import sys
import time
import boto3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def check_stack_status(stack_name):
    """
    Checks the status of a CloudFormation stack.

    Parameters:
        stack_name (str): The name of the CloudFormation stack.

    Returns:
        str: The stack status if successful, None otherwise.
    """
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
    """
    Terminates a CloudFormation stack.

    Parameters:
        stack_name (str): The name of the CloudFormation stack.
    """
    cloudformation = boto3.client('cloudformation')

    try:
        cloudformation.delete_stack(StackName=stack_name)
        print(f"Terminating stack: {stack_name}")

    except Exception as e:
        print(f"Failed to terminate stack: {str(e)}")
        send_error_email(stack_name, str(e))

def send_error_email(stack_name, error_message):
    """
    Sends an error email notification.

    Parameters:
        stack_name (str): The name of the CloudFormation stack.
        error_message (str): The error message.
    """
    sender_email = 'sender@example.com'
    receiver_email = 'receiver@example.com'
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'smtp_username'
    smtp_password = 'smtp_password'

    subject = f"Error in CloudFormation stack: {stack_name}"
    body = f"Error message: {error_message}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
        print("Error email sent successfully.")
    except Exception as e:
        print(f"Failed to send error email: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_cf_status.py <stack_name>")
        sys.exit(1)

    stack_name = sys.argv[1]
    terminate_attempts = 10
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
                print("Stack is stuck and termination attempts exhausted. Sending error email...")
                send_error_email(stack_name, "Stack termination attempts exhausted.")
                sys.exit(1)

        time.sleep(30)  # Wait for 30 seconds before polling again
