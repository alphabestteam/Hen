class Developer:
    # by default I set the the mission complit and mission to do to empty ,and day of work and payment to 0
    def __init__(self, name_of_developer) -> None:
        self._name_of_developer = name_of_developer
        self._mission_complit = {}
        self._day_of_work = 0
        self._payment = 0
        self._mission_to_do = {}
        self._expirience = 1

    # getters
    @property
    def name_of_developer(self):
        return self._name_of_developer

    @property
    def mission_complit(self):
        return self._mission_complit

    @property
    def day_of_work(self):
        return self._day_of_work

    @property
    def payment(self):
        return self._payment

    @property
    def mission_to_do(self):
        return self._mission_to_do

    @property
    def expirience(self):
        return self._expirience

    # setters
    @mission_complit.setter
    def mission_complit(self, name_of_mission, mission_ditails):
        self.mission_complit[name_of_mission] = mission_ditails

    @day_of_work.setter
    def day_of_work(self, mission_time):
        self.day_of_work += mission_time

    @payment.setter
    def payment(self, mission):
        self.payment = mission.payment * self.expirience

    @mission_to_do.setter
    def mission_to_do(self, name_of_new_mission, ditails_of_new_mission):
        self.mission_to_do[name_of_new_mission] = ditails_of_new_mission

    @expirience.setter
    def expirience(self, complex_of_mission):
        self.expirience += complex_of_mission
