import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        # Store the virus in an attribute
        self.virus = virus
        # Store pop_size in an attribute
        self.pop_size = pop_size
        self.repro_num = 0
        # Store the vacc_percentage in a variable
        self.vacc_percentage = vacc_percentage
        self.unvaccinated = False
        # Store initial_infected in a variable
        self.initial_infected = initial_infected
        self.newly_infected = []
        # Create a population
        # If assigned pop_size gives a TypeError: 'int' object is not iterable
        # If assigned self._create_population() it becomes an infite loop
        self.population = self._create_population()
        self.rate_of_infection = self.virus.repro_rate
        # Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        self.file_name = f"{self.virus.name}_pop_size_{self.pop_size}_vacc_percent_{self.vacc_percentage}.txt"
        self.logger = Logger(self.file_name)
        # You need to store a list of people (Person instances)
        # Some of these people will be infected some will not.
        # Use the _create_population() method to create the list and
        # return it storing it in an attribute here.
        # Call self._create_population() and pass in the correct parameters.

    # ---------------------------------------
    def _create_population(self):
        """Return a list of people, should be equal to pop_size"""
        # Create a list of people (Person instances). This list
        # should have a total number of people equal to the pop_size.
        people = set()
        # Some of these people will be uninfected and some will be infected.
        # The number of infected people should be equal to the the initial_infected
        # Infected
        for infected in range(self.initial_infected):
            people.add(infected)

        # Vaccinated
        number_of_vaccinated = int(self.vacc_percentage - self.pop_size)
        for person in range(self.initial_infected, self.pop_size, number_of_vaccinated):
            if number_of_vaccinated < self.vacc_percentage:
                people.add(Person(person, True))
            else:
                people.add(Person(person, True))
        # Return the list of people
        return people

    # --------------------------------------
    def _simulation_should_continue(self):
        # This method will return a boolean indicating if the simulation
        # should continue.
        # The simulation should not continue if all of the people are dead,
        # or if all of the living people have been vaccinated.
        # Loop over the list of people in the population. Return True
        # if the simulation should continue or False if not.
        for _ in self.population:
            if self._simulation_should_continue:
                return True
            return False

    def run(self):
        # This method starts the simulation. It should track the number of
        # steps the simulation has run and check if the simulation should
        # continue at the end of each step.
        time_step_counter = 0
        should_continue = True
        
        if should_continue is True:
            # print("Have entered the loop")
            # Increment the time_step_counter
            time_step_counter += 1
            # for every iteration of this loop, call self.time_step()
            self.logger.log_time_step(time_step_counter, self.pop_size)
            self.time_step()
            # Call the _simulation_should_continue method to determine if
            # the simulation should continue
            should_continue = self._simulation_should_continue()
        #  Write meta data to the logger. This should be starting
        # statistics for the simulation. It should include the initial
        # population size and the virus.
        print("------------------------------------")
        self.logger.log_time_step(time_step_counter, self.pop_size)
        self.logger.log_infection_survival(self.time_step, self.population)
        # Whenc the simulation completes you should conclude this with
        # the logger. Send the final data to the logger.
        print("------------------------------------")
        self.logger.log_interactions(time_step_counter, self.initial_infected)
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)
        print("------------------------------------")
        print(f"The simulation has ended after {time_step_counter} step(s).")
        should_continue = False

    #----------------------------------------
    def time_step(self):
        """ 
        :desc: Will simulate interactions between people, calulate new infections
        and determine if vaccinations and fatalities from infections
        """
        # The goal here is have each infected person interact with a number of other
        # people in the population
        #  Loop over your population
        random_person = random.random()
        infected_person = Person
        for person in self.population:
            # For each person if that person is infected
            if person is infected_person:
                # have that person interact with 100 other living people
                self.interaction(person, random_person)
                # Run interactions by calling the interaction method below. That method
                # takes the infected person and a random person

    #---------------------------------------------------------
    def interaction(self, infected_person, random_person):
        """Log the interactions between people"""
        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.  If that number is smaller
            #     than repro_rate, add that person to the newly infected array
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
        # Call logger method during this method.
        if not random_person.is_vaccinated is None:
            if random_person.infection is None:
                if random.random() < self.rate_of_infection:
                    self.newly_infected.append(random_person.id)
                    self.logger.log_interactions(infected_person, random_person)
                else:
                    self.logger.log_interactions(infected_person, random_person)

            self.logger.log_interactions(infected_person, random_person)

    # ------------------------------------------
    def _infect_newly_infected(self):
        # Call this method at the end of every time step and infect each Person.
        # Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for infect in range(self.newly_infected):
            infect.infected = self.virus
        self.newly_infected = []


if __name__ == "__main__":
    # Test your simulation here
    virus_name = str(sys.argv[3])
    repro_num = float(sys.argv[2])
    mortality_rate = float(sys.argv[4])
    # virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = int(sys.argv[1])
    vacc_percentage = float(sys.argv[5])
    initial_infected = 100

    # Make a new instance of the imulation
    # Took out vacc_percentage
    virus = Virus(virus_name, pop_size, mortality_rate)
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected=1)

    sim.run()
