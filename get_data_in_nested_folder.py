from connection import Connection
import json


def get_all_data(conn, bucket_name, folder_path) -> dict:
    """
    get all data format json in path
    :param conn:
    :param bucket_name:
    :param folder_path:
    :return:
    """
    for file in conn.listdir(path=f'{bucket_name}/{folder_path}'):
        folder_province = file['Key']
        for folder in conn.listdir(path=folder_province):
            path_metadata_json = folder['Key']
            if "path_metadata_json" in path_metadata_json:
                for each in conn.listdir(path=path_metadata_json):
                    file = each['Key']
                    with conn.open(file, "r") as f:
                        data = json.load(f)
                        yield data


if __name__ == '__main__':
    conn = Connection().connect()
    datas = get_all_data(
        conn=conn,
        bucket_name="bucket",
        folder_path="data/path/"
    )
    for data in datas:
        print(data)