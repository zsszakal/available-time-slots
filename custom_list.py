class CustomList(list):
    def remove_if_exists(self,v):
        try:
            self.remove(v)
        except ValueError:
            pass