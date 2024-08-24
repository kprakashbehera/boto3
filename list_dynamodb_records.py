import boto3

# dynamodb = boto3.resource('dynamodb')

aws_session = boto3.session.Session(profile_name="kpb.devops")
dynamodb_session = aws_session.resource('dynamodb')

table = dynamodb_session.Table('http-crud-tutorial-items')

'''
list_items = table.scan()
print(list_items['Items'])
'''

# print(table.scan()) /// This line will print all the details of the scan. Items, Count, RequestedCount, Metadata


# running for loop to find each record data
for record in table.scan()['Items']:
    print(record)

No_of_records = table.scan()['Count']
print(No_of_records)