import boto3
import zipfile


# Let's use Amazon S3
s3 = boto3.client("s3")

s3.download_file(
    Bucket="pcw-session-5",
    Key="Seymour Papert - Mindstorms - Children, Computers and Powerful Ideas (1981, Basic Books) - libgen.lc.pdf.zip",
    Filename="./mindstorm.zip",
)

with zipfile.ZipFile("./mindstorm.zip", "r") as zip_ref:
    zip_ref.extractall("./")

s3.upload_file(
    Filename="./Seymour Papert - Mindstorms - Children, Computers and Powerful Ideas (1981, Basic Books) - libgen.lc.pdf",
    Bucket="pcw-session-5",
    Key="mindstorm.pdf",
)
