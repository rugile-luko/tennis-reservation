import datetime
from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib import messages
from django.core.mail import send_mail

from . import models


@login_required
def home(request):
    context = {
        "clubs": models.Club.objects.all(),
        "date": datetime.datetime.now().date()
    }

    return render(request, 'home.html', context)


@login_required
def detail_view(request, club_pk, date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    today = datetime.datetime.now().date()
    today_hour = datetime.datetime.now().hour
    club = models.Club.objects.get(pk=club_pk)

    working_hours = []
    for hour in range(club.from_hour, club.to_hour+1):
        working_hours.append(hour)

    courts = models.Court.objects.all().filter(club=club)
    courts_with_schedule = {}

    for court in courts:
        court_schedule = []

        for hour in working_hours:
            court_schedule.append({
                "hour": hour,
                "is_reserved": court.is_reserved(hour, date),
                "is_unavailable": court.is_unavailable(hour, date)
            })

        courts_with_schedule[court] = court_schedule

    context = {
        "date": date,
        "today": today,
        "today_hour": today_hour,
        "previous_date": date - timedelta(days=1),
        "next_date": date + timedelta(days=1),
        "club": club,
        "working_hours": working_hours,
        "courts": courts,
        "courts_with_schedule": courts_with_schedule,
    }

    return render(request, 'detail_view.html', context)


@login_required
def reserve_court(request, club_pk, date, court_pk, hour):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    court = models.Court.objects.get(pk=court_pk)
    the_club = get_object_or_404(models.Club, pk=club_pk)
    if request.method == 'POST':
        form = forms.ReservationForm(the_club, date, court, hour, request.POST, initial={"date": date})
        if form.is_valid():
            reserved_court = form.cleaned_data.get("court")
            starting_hour = form.cleaned_data.get("starting_hour")
            reservation_date = form.cleaned_data.get("date")
            email = form.cleaned_data.get("email")
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            comment = "You have reserved a " + str(reserved_court) + " at " +\
                      str(starting_hour) + "h, " + str(reservation_date)
            send_mail('subject', comment, [email], [email])
            messages.success(request, 'The court reserved successfully!')
            return redirect('detail_view', club_pk=club_pk, date=date)
    else:
        form = forms.ReservationForm(the_club, date, court, hour, initial={"date": date})

    context = {
        "form": form,
        "date": date,
        "the_club": the_club,
        "court": court
    }

    return render(request, 'reserve_court.html', context)


@login_required
def create_club(request):
    if request.method == 'POST':
        form = forms.ClubForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = forms.ClubForm()

    context = {
        'form': form
    }

    return render(request, 'create_club.html', context)


@login_required
def create_court(request, club_pk, date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    the_club = get_object_or_404(models.Club, pk=club_pk)
    if request.method == 'POST':
        form = forms.CourtForm(the_club, request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.club = the_club
            new_form.save()

            return redirect('detail_view', club_pk=club_pk, date=date)
    else:
        form = forms.CourtForm(the_club)

    context = {
        'form': form,
        'the_club': the_club,
        "date": date
    }

    return render(request, 'create_court.html', context)


@login_required
def my_reservations(request):
    reservations = models.Reservation.objects.all().filter(user=request.user).order_by('-date', 'starting_hour')
    date = datetime.datetime.now().date()

    context = {
        "reservations": reservations,
        "time": datetime.datetime.now().hour + 1,
        "date": date
    }

    return render(request, 'my_reservations.html', context)


@login_required
def cancel_reservation(request, reservation_pk):
    reservation = models.Reservation.objects.get(pk=reservation_pk)
    reservation.cancelled = True
    reservation.save()
    messages.error(request, 'Your reservation was cancelled!')

    return redirect('my_reservations')


