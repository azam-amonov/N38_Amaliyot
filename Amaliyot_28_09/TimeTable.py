class Time:
    def __init__(self, hour, minute, second):
        self._hour = hour
        self._minute = minute
        self._second = second

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    @property
    def second(self):
        return self._second

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"


class TimeTable(Time):
    def __init__(self, subject, start_time, classroom):
        super().__init__(start_time.hour, start_time.minute, start_time.second)
        self._subject = subject
        self._classroom = classroom

    @property
    def subject(self):
        return self._subject

    @property
    def start_time(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    @property
    def classroom(self):
        return self._classroom


if __name__ == "__main__":
    time1 = Time(11, 0, 0)
    time2 = Time(10, 0, 0)
    time3 = Time(8, 30, 0)

    print(time1)
    subject = TimeTable("Programming", time1, "SAP")
    subject0 = TimeTable("Programming", time1, "eBay")
    subject1 = TimeTable("Programming", time1, "YouTube")
    subject2 = TimeTable("Design", time2, "Google")
    subject3 = TimeTable("SMM", time3, "Microsoft")

    print(f"Subject: {subject.subject}")
    print(f"Start Time: {subject.start_time}")
    print(f"Classroom: {subject.classroom}")
    print()

    print(f"Subject: {subject2.subject}")
    print(f"Start Time: {subject2.start_time}")
    print(f"Classroom: {subject2.classroom}")
    print()

    print(f"Subject: {subject3.subject}")
    print(f"Start Time: {subject3.start_time}")
    print(f"Classroom: {subject3.classroom}")
