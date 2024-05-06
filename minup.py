from minio import Minio
import uuid
import datetime
from PIL import Image
import io

class MinioUpload:
    def __init__(self, url, access_key, secret_key, bucket_name, http_prefix):
        try:
            self.client = Minio(url, access_key=access_key, secret_key=secret_key)
            print("connected")
        except Exception as e:
            print("can not connect")

        self.bucket_name = bucket_name
        self.http_prefix = http_prefix

    def upload_image(self, file):
        try:
            image = Image.open(file)
            image_data = io.BytesIO()
            image.save(image_data, format="WebP")
            image_data.seek(0)  # Reset the position to the beginning of the buffer
            object_name = f"{datetime.datetime.now().strftime('%m/%d')}/{uuid.uuid4()}.webp"
            #print(object_name)
            self.client.put_object(self.bucket_name, object_name, image_data, len(image_data.getvalue()))
            url = self.client.presigned_get_object(self.bucket_name, object_name)
            return url
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
minio_upload = MinioUpload(url="static.snpxdev.com", access_key="uXQ5Dk0in18El2F1F79H", secret_key="litiS53Pn4ObapMVr3mOhubi9mEIrjXLhUstKQps", bucket_name="test-parmida", http_prefix="https")
uploaded_image_url = minio_upload.upload_image("/home/parmida/Downloads/IMG_0758.jpeg")
print(uploaded_image_url)