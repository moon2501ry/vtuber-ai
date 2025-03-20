class History:
    def __init__(self, content:str|None=None):
        if content is not None:
            self.chat = [{"role": "system", "content": content}];
        else:
            self.chat = [];
    def add(self, content:str, role:str|None="user",):
        self.chat.append({"role": role, "content": content});
    def add_response(self, response):
        self.chat.append(response.choices[0].message);
    def print(self):
        '''Print Chat History'''
        _print = "CHAT - HISTORY\n--------------\n";
        for message in self.chat:
            _print += f"ROLE: {message["role"]}; CONTENT: {message["content"]}\n";
        print(_print);
        return print;

if __name__ == "__main__":
    print("U can't use this python file like main");