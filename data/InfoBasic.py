class info:
    base_uri = "https://gorest.co.in/"
    endpoint = "public/v2/users"
    headers = {'content-type': 'application/json', 'Authorization': 'Bearer 99b97f9ca940c646de3871f2d212f613d4b3080b5aa9bb8c4ef1745c260cfb0b'}


class dataRequest:
    def __init__(self, id, name, email, gender, status):
        self.id = id
        self.name = name
        self.email = email
        #self.celular = celular
        self.gender = gender
        self.status = status
