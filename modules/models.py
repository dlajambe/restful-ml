"""This file contains class templates linked with the provided
endpoints. They can be modified, extended, or replaced entirely to fit
your use case."""

class LanguageModel():
    """A language model template that produces string output.
    """
    def predict(self, input_data: str) -> str:
        if isinstance(input_data, str) == False:
            raise TypeError(
                'Received argument of type {}, expected "str"'.
                format(type(input_data)))
        return input_data + ' prediction!'
    
class NumericalModel():
    """A numerical model template that produces floating point
    output.
    """
    def predict(self, input_data: list[float]) -> float:
        for num in input_data:
            if (isinstance(num, float) == False 
                and isinstance(num, int) == False):
                raise TypeError('All input_data elements must be numeric')
        return sum(input_data)
