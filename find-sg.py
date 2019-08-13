import boto3

ec2_client = boto3.client('ec2', region_name='us-east-1')
ec2_client.describe_security_groups()
security_groups=ec2_client.describe_security_groups()['SecurityGroups']

ingress_cidr='0.0.0.0/0'

for sg in security_groups:
    for ip_perm in sg['IpPermissions']:
        for ip_range in ip_perm['IpRanges']:
            if ip_range['CidrIp'] == ingress_cidr:
                print(sg['GroupId'])