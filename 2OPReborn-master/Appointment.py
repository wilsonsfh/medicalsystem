class default_timeslots:
    def __init__(self,day,time):
        self.__day = day
        self.__time = time

class Store:
    a_timeslots = {}
    def __init__(self):
        if len(__class__.a_timeslots) <= 0:
            self.create_default_timeslots()

    def create_default_timeslots(self):
        Monday = default_timeslots('Mon',time={"8:00","9:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00"})
        Tuesday = default_timeslots('Tue',
                                   time={"8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00",
                                             "17:00", "18:00"})
        Wednesday = default_timeslots('Wed',
                                   time={"8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00",
                                             "17:00", "18:00"})
        Thursday = default_timeslots('Thursday',
                                   time={"8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00",
                                             "17:00", "18:00"})
        Friday = default_timeslots('Friday',
                                   time={"8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00",
                                             "17:00", "18:00"})

        Store.a_timeslots[Monday.day] = Monday
        Store.a_timeslots[Tuesday.day] = Tuesday
        Store.a_timeslots[Wednesday.day] = Wednesday
        Store.a_timeslots[Thursday.day] = Thursday
        Store.a_timeslots[Friday.day] = Friday


