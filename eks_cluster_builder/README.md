# EKS Cluster CloudFormation Template

This CloudFormation template creates a full-featured Amazon Elastic Kubernetes Service (EKS) cluster in a new AWS account.

## Prerequisites

- An AWS account
- Basic knowledge of AWS CloudFormation and EKS

## Deployment Steps

1. Open the AWS CloudFormation console.

2. Choose "Create Stack" and upload the CloudFormation template file.

3. Provide the required parameters such as ClusterName, VpcId, SubnetIds, KeyPairName, etc.

4. Review the stack configuration and click "Create Stack".

5. Wait for the CloudFormation stack to be created. It may take several minutes.

## Parameters

- **ClusterName**: The name of the EKS cluster.
- **VpcId**: The ID of the VPC in which to create the EKS cluster.
- **SubnetIds**: The list of subnet IDs for the EKS cluster.
- **KeyPairName**: The name of the SSH key pair to associate with the EKS cluster instances.
- **ClusterVersion**: The version of the EKS cluster (default: 1.20).
- **DesiredCapacity**: The desired number of worker nodes in the EKS cluster (default: 2).
- **MaxSize**: The maximum number of worker nodes in the EKS cluster (default: 3).
- **MinSize**: The minimum number of worker nodes in the EKS cluster (default: 1).
- **InstanceType**: The EC2 instance type for the worker nodes (default: t3.medium).

## Outputs

- **ClusterNameOutput**: The name of the EKS cluster.
- **ClusterEndpoint**: The endpoint URL of the EKS cluster.
- **ClusterArn**: The ARN of the EKS cluster.
- **WorkerNodeSecurityGroupId**: The ID of the security group for the worker nodes.
- **WorkerNodeIAMRoleArn**: The ARN of the IAM role for the worker nodes.

## Security Considerations

- By default, the CloudFormation template opens port 22 and port 443 from anywhere (0.0.0.0/0) in the security group for demonstration purposes. Adjust the security group rules as per your security requirements.

## Cleanup

To delete the CloudFormation stack and associated resources:

1. Open the AWS CloudFormation console.

2. Select the stack created by this template.

3. Choose "Delete Stack" and confirm the deletion.

4. Wait for the stack to be deleted. It may take several minutes.

## License

This CloudFormation template is released under the [MIT License](LICENSE).

