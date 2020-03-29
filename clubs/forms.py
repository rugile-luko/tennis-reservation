import datetime
from django import forms
from django.forms import TextInput
from django.urls import reverse
from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button


class ReservationForm(forms.ModelForm):
    def __init__(self, club, date, court, hour, *args, **kwargs):
        self.club = club
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['court'].queryset = models.Court.objects.filter(club=club)
        self.fields['court'].initial = court
        self.fields['starting_hour'].initial = hour
        self.helper = FormHelper()
        self.helper.form_id = 'id-ReservationForm'
        # self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_reservation'
        self.helper.add_input(Submit('submit', 'Reserve a Court'))
        # self.helper.add_input(Button('cancel', 'Cancel', css_class='btn btn-secondary',
        #                              onClick="window.location.href = '{}';"
        #                              .format(reverse('detail_view', args=[club.pk, date]))))

        club_open_hours = []
        for hour in range(club.from_hour, club.to_hour + 1):
            if date != datetime.datetime.now().date() or hour > datetime.datetime.now().hour:
                club_open_hours.append(
                    (int(hour), str(hour))
                )

        # club_open_hours = [(i, i) for i in range(club.from_hour, club.to_hour + 1)]
        self.fields['starting_hour'].choices = club_open_hours

    class Meta:
        model = models.Reservation
        fields = ['court', 'starting_hour', 'date', 'email']

        widgets = {
            'date': forms.TextInput(attrs={"autocomplete": 'off'})
        }

    def clean(self):
        data = self.cleaned_data
        court = data.get('court')
        starting_hour = data.get('starting_hour')
        date = data.get('date')

        if date == datetime.datetime.now().today() and datetime.datetime.now().hour > starting_hour:
            self.add_error('starting_hour', 'You cannot choose this time')

        if starting_hour and date and court and court.is_reserved(starting_hour, date):
            self.add_error('starting_hour', 'This time is already taken')

        if datetime.date.today() > date:
            self.add_error('date', 'Reservation is not available')


class ClubForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClubForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget = TextInput(attrs={
            # 'id': 'autocompleteAddress',
            'placeholder': 'Enter club address'
            })
        self.helper = FormHelper()
        self.helper.form_id = 'id-ClubForm'
        # self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'create_club'
        self.helper.add_input(Submit('submit', 'Create a Club'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn btn-secondary',
                                     onClick="window.location.href='{}';"
                                     .format(reverse('home'))))

    class Meta:
        model = models.Club
        fields = '__all__'

        # widgets = {
        #     'address': forms.CharField(max_length=200, attrs={"id": "autocomplete"})
        # }


class CourtForm(forms.ModelForm):
    def __init__(self, club, *args, **kwargs):
        self.club = club
        super(CourtForm, self).__init__(*args, **kwargs)
        # self.fields['club'].queryset = models.Club.objects.filter(name=club.name)
        self.helper = FormHelper()
        self.helper.form_id = 'id-CourtForm'
        # self.helper.form_class = 'blueForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'create_court'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.helper.add_input(Button('cancel', 'Cancel', css_class='btn btn-secondary',
        #                              onClick="window.location.href='{}';"
        #                              .format(reverse('detail_view', args=[club.pk]))))

    class Meta:
        model = models.Court
        fields = ['type', 'name']




