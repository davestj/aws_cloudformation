## CloudFormation Stack Status Checker

This Python script allows you to monitor the status of a CloudFormation stack and print the StackStatus to the console. It can be used to continuously poll a CloudFormation stack until it reaches a terminal state.

### Prerequisites

- Python 3.x installed
- Boto3 library installed (`pip install boto3`)
- AWS credentials configured (either via environment variables or AWS CLI configuration)

### Usage

```
python check_cf_status.py <stack_name>
```

Replace `<stack_name>` with the name of the CloudFormation stack you want to monitor.

### Behavior

The script continuously polls the CloudFormation stack every 30 seconds and prints the StackStatus to the console. It will keep polling until the stack reaches a terminal state such as `CREATE_COMPLETE` or `UPDATE_COMPLETE`. If the stack gets stuck in a non-terminal state, it will attempt to terminate the stack after a certain number of attempts.

The

 script handles the following stack statuses:
- `CREATE_FAILED`, `ROLLBACK_FAILED`, `DELETE_FAILED`: Stack deployment failed.
- `CREATE_COMPLETE`, `UPDATE_COMPLETE`: Stack deployment successful.
- `ROLLBACK_COMPLETE`: Stack deployment failed, rollback completed.
- `UPDATE_ROLLBACK_FAILED`, `ROLLBACK_FAILED`: Stack deployment failed, rollback failed.
- `UPDATE_ROLLBACK_COMPLETE`: Stack deployment failed, rollback completed.

If the stack is stuck in one of the following states: `CREATE_IN_PROGRESS`, `UPDATE_IN_PROGRESS`, `DELETE_IN_PROGRESS`, the script will attempt to terminate the stack. It allows a maximum number of termination attempts before exiting.

Please note that terminating a stack should be used with caution as it can lead to resource deletion and potential data loss. Ensure you have proper backups and confirm the termination before executing it.

### License

This script is released under the [MIT License](LICENSE).

Feel free to modify and use it according to your needs.
```