class BaseCommand:
    def __init__(self, factory, protocol, data):
        self.factory = factory
        self.protocol = protocol
        self.data = data
        
        if self.Form:
            self.form = self.Form(data)
        
    def is_valid(self):
        if self.form:
            is_valid = self.form.is_valid()
            errors = self.form.errors
            return is_valid, errors
        else:
            raise NotImplementedError
    
    def run(self):
        raise NotImplementedError
