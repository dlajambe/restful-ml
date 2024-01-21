"""This file contains class templates linked with the provided
endpoints. They can be modified, extended, or replaced entirely to fit
your use case."""

class LanguageModel():
    """A language model template that produces string output.
    """
    def predict(self, input_str: str) -> str:
        if isinstance(input_str, str) == False:
            raise TypeError(
                'Received argument of type {}, expected "str"'.
                format(type(input_str)))
        return input_str + ' prediction!'
    
class NumericalModel():
    """A numerical model template that produces floating point
    output.
    """
    def predict(self, input_floats: list[float]) -> float:
        for num in input_floats:
            if (isinstance(num, float) == False 
                and isinstance(num, int) == False):
                raise TypeError('All input_floats elements must be numeric')
        return sum(input_floats)
