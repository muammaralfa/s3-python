import s3fs


class Connection:
    def __init__(self):
        self.key = "key access"
        self.secret = "secret key"
        self.endpoint_url = "url"
        self.client_kwargs = {
            'key': self.key,
            'secret': self.secret,
            'endpoint_url': self.endpoint_url
        }
        self.s3 = s3fs.S3FileSystem(**self.client_kwargs)

    def connect(self):
        return self.s3