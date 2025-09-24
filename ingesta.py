import boto3

ficheroUpload = "data.csv"
nombreBucket = "lucechaos-storage"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, "ingesta/" + ficheroUpload)
print(response)

print("Ingesta completada")