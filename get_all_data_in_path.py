from connection import Connection


def get_all_data(conn, bucket_name, folder_path) -> list:
    """
    get all data format json in path
    :param conn:
    :param bucket_name:
    :param folder_path:
    :return:
    """
    files = conn.glob(f's3://{bucket_name}/{folder_path}**')
    list_file = [file for file in files if file.endswith('.json')]
    return list_file


if __name__ == '__main__':
    conn = Connection().connect()
    datas = get_all_data(
        conn=conn,
        bucket_name="bucket",
        folder_path="data/path/"
    )
    for data in datas:
        print(data)