class Singleton:
    _instance = None

    def __init__(self):
        print("Llamado al metodo Init")
        self.nombre = "Soy Unico"

    def __new__(cls, *args, **kwargs):

        if not isinstance(cls._instance, cls):
            print("Llamado al metodo nueva instancia")
            cls._instance = object.__new__(cls)

        return cls._instance


