from person import Person

class Logger(object):
    """Creates a logger"""
    def __init__(self, file_name):
        # Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

    # The methods below are just suggestions. You can rearrange these or
    # rewrite them to better suit your code style.
    # What is important is that you log the following information from the simulation:
    # Meta data: This shows the starting situtation including:
    #   population, initial infected, the virus, and the initial vaccinated.
    # Log interactions. At each step there will be a number of interaction
    # You should log:
    #   The number of interactions, the number of new infections that occured
    # You should log the results of each step. This should inlcude:
    #   The population size, the number of living, the number of dead, and the number
    #   of vaccinated people at that step.
    # When the simulation concludes you should log the results of the simulation.
    # This should include:
    #   The population size, the number of living, the number of dead, the number
    #   of vaccinated, and the number of steps to reach the end of the simulation.

    # ---------------------------------------------------
    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        """Write the metadata to the file"""
        # This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        with open(self.file_name, 'w', encoding="utf-8") as file:
            print(f"Population Size: {pop_size}\nVaccination Percent: {vacc_percentage}\nVirus Name: {virus_name}\nMortality Rate: {mortality_rate}")
            print(f"Repro Number is {basic_repro_num}")
        file.close()

    # ---------------------------------------------------
    def log_interactions(self, step_number, number_of_interactions):
        """Display Interactions"""
        # Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        random_person_sick = None
        random_person_vacc = None
        did_infect = None

        with open(self.file_name, 'a', encoding="utf-8") as file:
            if did_infect is True:
                print(f"Step Number: {step_number}")
                print(f"Number of Interactions: {number_of_interactions}")
                print("Random person has been infected by a random infected person")
            elif random_person_vacc is True:
                print(f"Step Number: {step_number}")
                print(f"Number of Interactions: {number_of_interactions}")
                print("Random infected person did not infect vaccinated person")
            elif random_person_sick is True:
                print(f"Step Number: {step_number}")
                print(f"Number of Interactions: {number_of_interactions}")
                print("Random person could not infect already sick Person")
            else:
                
                print(f"Step Number: {step_number}")
                print(f"Number of Interactions: {number_of_interactions}")
                print("Random person has failed to infect random person")
        file.close()

    # ---------------------------------------------
    def log_infection_survival(self, step_number, population_count):
        """Displaying the infection survivial rate and appending the results"""
        # Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        did_survive_from_infection = True
        with open(self.file_name, 'a', encoding="utf-8") as file:
            if did_survive_from_infection is True:
                print(f"Person did survive")
            else:
                print("------------------------------------")
                print(step_number)
                print("Person did not survive")
                print(f"Population count is {population_count}.")
        file.close()

    # ---------------------------------------------
    def log_time_step(self, time_step_number, population):
        """Displays the beginning of time in the simulation"""
        # print("Population is printed from logger.py")
        print(f"This is the start of time number {time_step_number + 1}, Start Population is {population}.")
        print(f"Number of steps taken: {time_step_number}")
