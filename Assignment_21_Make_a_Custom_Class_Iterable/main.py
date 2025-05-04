class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self  # Returning the iterator object (itself in this case)

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stop iteration when countdown reaches 0
        self.current -= 1
        return self.current + 1  # Return the current value before decrement

# Example usage:
countdown = Countdown(5)
for number in countdown:
    print(number)
