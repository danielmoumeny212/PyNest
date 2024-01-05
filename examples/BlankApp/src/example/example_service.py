from .example_model import Example
from functools import lru_cache
from nest.core.decorators import Injectable


@lru_cache()
@Injectable
class ExampleService:

    def __init__(self):
        self.database = []

    def get_example(self):
        return self.database

    def add_example(self, example: Example):
        self.database.append(example)
        return example
