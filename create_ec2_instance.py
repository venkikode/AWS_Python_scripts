import boto3

def create_ec2_instance():
    try:
        print("Create EC2 Instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-0f74c08b8b5effa56",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="KODE"
        )
    except Exception as e:
        print(e)
create_ec2_instance()