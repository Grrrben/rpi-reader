class Keypad:

    BTN_DASH = "#"  # enter

    BTN_CLEAR = "*"  # Clear

    def __init__(self):
        # a sequence is a list of numbers that make a PIN
        self.sequence = []

    def input(self, key):
        print("registerKeyPressHandler")
        if key == Keypad.BTN_DASH:
            # this is the enter
            # thus; handle the PIN and clear the sequence afterwards
            print(self.sequence)
            self.clear()
        elif key == Keypad.BTN_CLEAR:
            self.clear()
        else:
            self.sequence.append(key)

    def clear(self):
        """
        empties the sequence
        """
        self.sequence = []