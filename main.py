import json
import uuid
from dependencies import Injector


class Logger:

    def __init__(self):
        self.instance_value = "xpto"
        self.index = 1
        print("classe de log iniciada")

    def print(self, message):
        print(json.dumps({'instance_value': self.instance_value, 'index': self.index, 'message': message}))
        self.index += 1


class LoggerDependent1:

    def __init__(self, logger: Logger):
        self.log_object = logger

    def execute(self):
        self.log_object.print("classe 01")


class LoggerDependent2:

    def __init__(self, logger: Logger):
        self.log_object = logger

    def execute(self):
        self.log_object.print("classe 02")


class Main:

    def __init__(self, logger: Logger, logger_dependent_1: LoggerDependent1, logger_dependent_2: LoggerDependent2):
        self.logger = logger
        self.logger_dependent_1 = logger_dependent_1
        self.logger_dependent_2 = logger_dependent_2

    def execute(self):
        self.logger.instance_value = str(uuid.uuid4())
        self.logger.print("log configurado")
        self.logger_dependent_1.execute()
        self.logger_dependent_2.execute()


class MyContainer(Injector):
    logger = Logger
    logger_dependent_1 = LoggerDependent1
    logger_dependent_2 = LoggerDependent2
    main = Main


if __name__ == '__main__':
    MyContainer.main.execute()
