class People:
    def __init__(self) -> None:
        self._names= []

    def add_person(self,name):
        self._names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            name = self._names[0]
            del self._names[0]
            return name
        except:
            print("no more names")