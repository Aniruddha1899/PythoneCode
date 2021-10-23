import boto3
import pandas as pd
from io import StringIO

# Creating the low level functional client
client = boto3.client(
    's3',
    aws_access_key_id = 'AKIA3PU3C66B2LNYPL7U',
    aws_secret_access_key = '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',
    region_name = 'us-east-2'
)
    
# Creating the high level object oriented interface
resource = boto3.resource(
    's3',
    aws_access_key_id = 'AKIA3PU3C66B2LNYPL7U',
    aws_secret_access_key = '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',
    region_name = 'us-east-2'
)

# Fetch the list of existing buckets
clientResponse = client.list_buckets()
    
# Print the bucket names one by one
print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')


# print the file names in the bucket
my_bucket = resource.Bucket('pythontrainingbucket')

for file in my_bucket.objects.all():
    print(file.key)

#a = client.list_objects(
  #  Bucket='pythontrainingbucket',
#)



# Print the data in the file
csv_obj = client.get_object(Bucket='pythontrainingbucket', Key='movies.csv')
print(csv_obj['Body'])

#Decoding the file to utf-8
csv_obj_body = csv_obj['Body']

#Decoding the file
csv_string = csv_obj_body.read().decode('utf-8')
df = pd.read_csv(StringIO(csv_string))
print(df.head()) # printing the the first 5 records in the dataframe.

#printing the specific columns in the movies.csv
df1=df[['Film','Year']]
print(df1.head())