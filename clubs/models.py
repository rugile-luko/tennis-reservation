import datetime
from django.contrib.auth.models import User
from django.db import models

HOURS_OF_THE_DAY = [(i, i) for i in range(1, 25)]


class Club(models.Model):
    MON = "Monday"
    TUE = "Tuesday"
    WED = "Wednesday"
    THU = "Thursday"
    FRI = "Friday"
    SAT = "Saturday"
    SUN = "Sunday"

    DAY_CHOICES = (
        (MON, 'Monday'),
        (TUE, 'Tuesday'),
        (WED, 'Wednesday'),
        (THU, 'Thursday'),
        (FRI, 'Friday'),
        (SAT, 'Saturday'),
        (SUN, 'Sunday')
    )

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    weekday_from = models.CharField(choices=DAY_CHOICES, max_length=100)
    weekday_to = models.CharField(choices=DAY_CHOICES,  max_length=100)
    from_hour = models.IntegerField(choices=HOURS_OF_THE_DAY)
    to_hour = models.IntegerField(choices=HOURS_OF_THE_DAY)

    def __str__(self):
        return self.name

    def get_hard_court_count(self):
        return Court.objects.filter(club=self, type=Court.HARD).count()

    def get_grass_court_count(self):
        return Court.objects.filter(club=self, type=Court.GRASS).count()

    def get_clay_court_count(self):
        return Court.objects.filter(club=self, type=Court.CLAY).count()

    def get_carpet_court_count(self):
        return Court.objects.filter(club=self, type=Court.CARPET).count()


class Court(models.Model):
    HARD = "Hard"
    GRASS = "Grass"
    CLAY = "Clay"
    CARPET = "Carpet"

    TYPE_OF_SURFACE = (
        (HARD, 'Hard'),
        (GRASS, 'Grass'),
        (CLAY, 'Clay'),
        (CARPET, 'Carpet')
    )

    club = models.ForeignKey(Club, related_name='court', on_delete=models.CASCADE)
    type = models.CharField(choices=TYPE_OF_SURFACE, max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % self.name

    def is_reserved(self, hour, date):
        reservations = Reservation.objects.filter(court=self, starting_hour=hour, date=date)
        if reservations.count() > 0:
            reservation = reservations.first()
            return not reservation.cancelled
        else:
            return False

    def is_unavailable(self, hour, date):
        new_datetime = datetime.datetime(year=date.year, month=date.month, day=date.day, hour=hour, minute=0, second=0)
        return datetime.datetime.now() > new_datetime

    class Meta:
        ordering = ('type', )


class Reservation(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    starting_hour = models.IntegerField(choices=HOURS_OF_THE_DAY)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    cancelled = models.BooleanField(default=False)

    class Meta:
        ordering = ("-date", "starting_hour", )
