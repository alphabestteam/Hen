from mission import Mission
from developer import Developer


class Project:
    def __init__(self, description_of_project, start_project) -> None:
        self._description_of_project = description_of_project
        self._start_project = start_project
        self._end_project = start_project
        self._mission_list = {}
        self._developer_list = {}
        self._mission_to_do_list = []
        self._complited_mission = []
        self._cost_of_project = 0
        self._does_complit = True

    # getters
    @property
    def description_of_project(self):
        return self._description_of_project

    @property
    def start_project(self):
        return self._start_project

    @property
    def end_project(self):
        return self._end_project

    @property
    def mission_list(self):
        return self._mission_list

    @property
    def developer_list(self):
        return self._developer_list

    @property
    def mission_to_do_list(self):
        return self._mission_to_do_list

    @property
    def complited_mission(self):
        return self._complited_mission

    @property
    def cost_of_project(self):
        return self._cost_of_project

    @property
    def does_complit(self):
        return self._does_complit

    # setters
    @description_of_project.setter
    def description_of_project(self, new_description_of_project):
        self.description_of_project = new_description_of_project

    @start_project.setter
    def start_project(self, new_start_project):
        self.start_project = new_start_project

    @end_project.setter
    def end_project(self, mission: Mission):
        self.end_project += mission.day_of_work

    @mission_list.setter
    def add_new_mission(self, new_mission: Mission):
        if new_mission.description_of_mission in self.mission_list:
            print("the mission already exit")
        else:
            self.mission_list[new_mission.description_of_mission] = new_mission
            self.end_project(new_mission)
            if new_mission.does_complit:
                self.mission_to_do_list.append(new_mission.description_of_mission)

    @mission_list.setter
    def sub_mission(self, new_mission: Mission):
        if new_mission.description_of_mission in self.mission_list:
            self.mission_list.pop(new_mission.description_of_mission)
            if new_mission.description_of_mission in self.mission_to_do_list:
                self.mission_to_do_list.pop(new_mission.description_of_mission)
            else:
                self.complited_mission.pop(new_mission.description_of_mission)
            self.sub_mission_from_developer(new_mission)
        else:
            print("this mission not exist in the mission list")

    @developer_list.setter
    def sub_mission_from_developer(self, mission: Mission):
        for develo in self.developer_list:
            if mission.description_of_mission in develo.mission_to_do:
                self.developer_list[develo].mission_to_do.pop(
                    mission.description_of_mission
                )

    @does_complit.setter
    def does_complit(self, update):
        self.does_complit = update

    @developer_list.setter
    def add_mission_to_developer(self, name, mission: Mission):
        for devlo in self.developer_list:
            if devlo.name_of_developer == name:
                if (
                    mission.description_of_mission
                    in self.developer_list[name].mission_to_do
                ):
                    print("the mission exit in this developer")
                else:
                    self.developer_list[name].mission_to_do(
                        mission.description_of_mission, mission
                    )
        else:
            print(f"there is no developer named {name}")

    @developer_list.setter
    def add_new_deveolper(self, developer: Developer):
        if developer.name_of_developer not in self.developer_list:
            self.developer_list[developer.name_of_developer] = developer
        else:
            print("this developer exit in the system")

    @developer_list.setter
    def complit_mission(self, developer: Developer, mission: Mission):
        if mission.description_of_mission in developer.mission_to_do:
            self.developer_list[developer].mission_complit(
                mission.description_of_mission, mission
            )
            self.developer_list[developer].mission_to_do.pop(
                mission.description_of_mission
            )
