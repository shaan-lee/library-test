import configparser
import os
import csv
import json

from minio import Minio
from pyminio import Pyminio

config = configparser.ConfigParser()
config.read(".cfg")
config = config["MINIO"]


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(config["endpoint"], config["access_key"], config["secret_key"])
    pyclient = Pyminio(minio_obj=client)
    bucket_name = config["bucket_name"]

    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
    # print(client.bucket_exists(bucket_name))

    bucket_list = client.list_buckets()
    # print(bucket_list)

    # client.fput_object(bucket_name,"i.png","./i.png")

    # client.fget_object(bucket_name,"i.png","./minio_download/i.png")

    # client.remove_object(bucket_name,"i.png")

    # client.remove_bucket(bucket_name)
    # print(client.bucket_exists(bucket_name))

    obj_list = client.list_objects(bucket_name)
    for obj in obj_list:
        if obj.object_name == "legal/":
            print(obj.object_name)
            print(obj.is_dir)
            for folder in pyclient.listdir(f"/{bucket_name}/{obj.object_name}"):
                if pyclient.exists(
                    f"/{bucket_name}/{obj.object_name}{folder}info.json"
                ):
                    client.fget_object(
                        bucket_name,
                        f"{obj.object_name}{folder}info.json",
                        f"./minio_download/{folder}info.json",
                    )

    csv_file = open("./legal_sites.csv", "w")
    writer = csv.writer(csv_file)

    for path in os.listdir("./minio_download"):
        with open(f"./minio_download/{path}/info.json", "r") as f:
            data = json.load(f)
            writer.writerow(data.values())


if __name__ == "__main__":
    main()
