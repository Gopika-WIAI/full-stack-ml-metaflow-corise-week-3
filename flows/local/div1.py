from metaflow import FlowSpec, step


class DivideByZeroFlow(FlowSpec):
    
    @step
    def start(self):
        self.divisors = [0, 1, 2]
        self.next(self.divide, foreach="divisors")

    @step
    def divide(self):
        import numpy as np
        self.res = 10 / (self.input + np.finfo(float).eps)  # A
        self.next(self.join)

    @step
    def join(self, inputs):
        self.results = [inp.res for inp in inputs]
        print("results", self.results)
        self.next(self.end)

    @step
    def end(self):
        print("done!")


if __name__ == "__main__":
    DivideByZeroFlow()
