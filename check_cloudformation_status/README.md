## CloudFormation Stack Status Checker

This Python script allows you to check the status of a CloudFormation stack and perform specific actions based on the stack status. The script utilizes the AWS SDK for Python (Boto3) to interact with the AWS CloudFormation service.

### Prerequisites

- Python 3.x
- Boto3 library (`pip install boto3`)

### Usage

1. Clone the repository or download the script `check_cf_status.py` to your local machine.

2. Install the required dependencies by running the following command:

   ```
   pip instal boto3
   ```

3. Provide the necessary configuration and parameters:

   - Update the sender and receiver email addresses in the `send_error_email` function to specify the email notification recipients.

   - Set the SMTP server and authentication details in the `send_error_email` function.

4. Execute the script using the following command:

   ```
   python check_cf_status.py <stack_name>
   ```

   Replace `<stack_name>` with the name of the CloudFormation stack you want to monitor.

### Functionality

The script continuously polls the CloudFormation stack status every 30 seconds. It performs the following actions based on the stack status:

- If the stack deployment fails (`CREATE_FAILED`, `ROLLBACK_FAILED`, `DELETE_FAILED`), the script exits with a return code of 1.

- If the stack deployment completes successfully (`CREATE_COMPLETE`, `UPDATE_COMPLETE`), the script exits with a return code of 0.

- If the stack deployment fails and a rollback is completed (`ROLLBACK_COMPLETE`), the script exits with a return code of 1.

- If the stack deployment fails and a rollback fails (`UPDATE_ROLLBACK_FAILED`, `ROLLBACK_FAILED`), the script exits with a return code of 1.

- If the stack deployment fails and a rollback is completed (`UPDATE_ROLLBACK_COMPLETE`), the script exits with a return code of 1.

- If the stack deployment is in progress (`CREATE_IN_PROGRESS`, `UPDATE_IN_PROGRESS`, `DELETE_IN_PROGRESS`), the script attempts to terminate the stack.

- If the stack is stuck and termination attempts are exhausted, the script sends an error email notification and exits with a return code of 1.

### Error Email Notification

The script includes an error email notification feature to alert specific recipients when the stack is stuck and termination attempts are exhausted. The email is sent using the Simple Mail Transfer Protocol (SMTP). To configure the email notification, update the following variables in the `send_error_email` function:

- `sender_email`: The email address from which the error notification is sent.
- `receiver_email`: The email address to which the error notification is sent.
- `smtp_server`: The SMTP server address for sending the email.
- `smtp_port`: The SMTP server port number.
- `smtp_username`: The username for authenticating with the SMTP server.
- `smtp_password`: The password for authenticating with the SMTP server.

Ensure that you have the necessary permissions and configurations to send emails via SMTP.

### Limitations and Considerations

- The script assumes you have valid AWS credentials configured locally or through environment variables to access the AWS CloudFormation service.

- Terminating a stack should be used with caution as it can lead to resource deletion and potential data loss. Ensure you have proper backups and confirm the termination before executing it.

- Ensure the necessary email configuration is provided for the error email notification feature to work correctly.

### License

This script is released under the [MIT License](LICENSE).

Feel free to modify and use it according to your needs.