## AWS CloudFormation Template - Full-Featured EC2 Instance with ELB and ASG

This CloudFormation template creates an EC2 instance with Elastic Load Balancer (ELB) and Auto Scaling Group (ASG) resources. It also includes configuration for copying an artifact from an S3 bucket to the EC2 instance and updating Route 53 hosted zones.

### Parameters

- `AMIId` (AWS::EC2::Image::Id): ID of the AMI to use for the EC2 instances.
- `InstanceType` (String): EC2 instance type. Default: `t2.micro`.
- `MinInstances` (Number): Minimum number of instances in the Auto Scaling Group. Default: `1`.
- `MaxInstances` (Number): Maximum number of instances in the Auto Scaling Group. Default: `3`.
- `KeyPairName` (AWS::EC2::KeyPair::KeyName): Name of the key pair for SSH access.
- `DiskSize` (Number): Size of the root disk in GB. Default: `8`.
- `DiskType` (String): Type of the root disk. Default: `gp2`.
- `EnableEncryption` (String): Enable encryption for the ELB and ASG. Default: `false`.
- `ArtifactBucket` (String): S3 bucket name containing the artifact.
- `Artifact` (String): Artifact file to copy from the S3 bucket.
- `NodeJSAppName` (String): Demoapp name.
- `HealthCheckInterval` (Number): Health check interval (in seconds) for the ELB. Default: `30`.
- `Route53HostedZoneName` (String): Root domain name for the Route 53 hosted zone.
- `SubdomainName` (String): Subdomain name to add/update in the Route 53 hosted zone.
- `Monitoring` (String): Whether to enable detailed monitoring (true or false). Default: `false`.

### Resources

- `MyEC2Instance` (AWS::EC2::Instance): EC2 instance resource with the specified properties and configuration.
- `MyLoadBalancer` (AWS::ElasticLoadBalancingV2::LoadBalancer): ELB resource with the specified properties.
- `MyTargetGroup` (AWS::ElasticLoadBalancingV2::TargetGroup): Target Group resource for the ELB with the specified properties.
- `MyListener` (AWS::ElasticLoadBalancingV2::Listener): Listener resource for the ELB with the specified properties.
- `MyAutoScalingGroup` (AWS::AutoScaling::AutoScalingGroup): Auto Scaling Group resource with the specified properties.
- `MyLaunchConfiguration` (AWS::AutoScaling::LaunchConfiguration): Launch Configuration resource with the specified properties.
- `MySecurityGroup` (AWS::EC2::SecurityGroup): Security Group resource for the EC2 instance with the specified properties.

### Outputs

- `InstanceId`: ID of the created EC2 instance.
- `LoadBalancerDNSName`: DNS name of the load balancer.
- `FullUrl`: Full URL with subdomain.

Please provide values for the required parameters when deploying the CloudFormation stack.