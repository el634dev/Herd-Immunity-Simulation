class Virus(object):
    """
    :desc: Properties and attributes of the virus used in Simulation.
    :return: None
    """
    def __init__(self, name, repro_rate, mortality_rate):
        """
        :desc: Define the attributes of your virus
        :return: None
        """
        self.name = name
        # Define the other attributes of Virus
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3
