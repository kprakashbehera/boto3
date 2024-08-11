import boto3

aws_mgmt_con = boto3.session.Session(profile_name='kpb.devops')
iam_session = aws_mgmt_con.resource('iam')

# listing users using 'resource'
for user in iam_session.users.all():
    print(user)
    print(user.name)