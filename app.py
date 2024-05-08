class App:
    def __call__(self,environ,start_response):
        status="200 ok"
        headers=[("Content-type","text/plain")]
        start_response(status,headers)


        return [b"Hello World"]