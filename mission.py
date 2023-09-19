import datetime


class Mission:
    def __init__(
        self,
        description_of_mission,
        start_date: datetime,
        belong_to_project,
        day_of_work,
        complex_of_mission,
    ) -> None:
        self._description_of_mission = description_of_mission
        self._start_date = start_date
        self._belong_to_project = belong_to_project
        self._belong_to_developer = False
        self._day_of_work = day_of_work
        self._end_date = start_date + datetime.timedelta(days=day_of_work)
        self._complex_of_mission = complex_of_mission
        self._does_complit = False
        self._payment = 0

    def __str__(self) -> str:
        return f"belong to prject {self.belong_to_project}"

    # getters
    @property
    def description_of_mission(self):
        return self._description_of_mission

    @property
    def start_date(self):
        return self._start_date

    @property
    def belong_to_project(self):
        return self._belong_to_project

    @property
    def belong_to_developer(self):
        return self._belong_to_developer

    @property
    def day_of_work(self):
        return self._day_of_work

    @property
    def end_date(self):
        return self._end_date

    @property
    def complex_of_mission(self):
        return self._complex_of_mission

    @property
    def does_complit(self):
        return self._does_complit

    @property
    def payment(self):
        return self.complex_of_mission / self.day_of_work

    # setters
    @start_date.setter
    def start_date(self, new_date: datetime):
        self.start_date = new_date
        self.end_date = new_date + datetime.timedelta(days=self.day_of_work)

    @belong_to_project.setter
    def belong_to_project(self, new_project: str):
        self.belong_to_project = new_project

    @day_of_work.setter
    def day_of_work(self, new_days_of_work: int):
        self.day_of_work = new_days_of_work
        self.end_date = self.start_date + datetime.timedelta(days=new_days_of_work)

    @complex_of_mission.setter
    def complex_of_mission(self, new_complex):
        self.complex_of_mission = new_complex

    @belong_to_developer.setter
    def belong_to_developer(self, new_developer):
        self.belong_to_developer = new_developer

    @does_complit.setter
    def does_complit(self, update):
        self.does_complit = update

    @end_date.setter
    def end_date(self, update):
        self.end_date = update
