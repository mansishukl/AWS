import boto3

# Initialize the Rekognition client
rekognition = boto3.client('rekognition')

# Define the S3 bucket and image
bucket_name = 'images-bucket31'  
image_name = 'img1.jpg'  

# AWS Rekognition to detect faces
response = rekognition.detect_faces(
    Image={
        'S3Object': {
            'Bucket': bucket_name,
            'Name': image_name
        }
    },
    Attributes=['ALL']  
)

# Print 
for faceDetail in response['FaceDetails']:
    print(f"Confidence: {faceDetail['Confidence']:.2f}%")
    print("Emotions:")
    for emotion in faceDetail['Emotions']:
        print(f"  {emotion['Type']}: {emotion['Confidence']:.2f}%")
    print(f"Gender: {faceDetail['Gender']['Value']}")
    print(f"Age Range: {faceDetail['AgeRange']['Low']} - {faceDetail['AgeRange']['High']}\n")

