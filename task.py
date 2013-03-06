class Task:
    ''' This class stores information retrieved from/to the request'''
    def __init__(self, number, payload, target, resource, extensions=None, banned_response_codes=None):
        self.number = number
        self.payload = payload
        self.target = target
        self.resource = resource
        self.extensions = extensions
        self.banned = banned_response_codes

        self.response_code = None
        self.response_size = None
        self.response_time = None

        self.valid = True

    def set_response_code(self, code):
        self.response_code = str(code)
        if self.response_code in self.banned:
            self.valid = False

    def values(self):
        return (self.number,
                self.payload,
                self.target,
                self.resource,
                self.extension,
                self.response_code,
                self.response_size,
                self.response_time)

    def get_complete_target(self):
        return self.target + self.resource

    def is_valid(self):
        return self.valid
