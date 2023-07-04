from django.shortcuts import render
from .models import *
from Accounts.views import *
from datetime import datetime
from django.db.models import Q
# Create your views here.

today = datetime.today()
def contest(request):
    contest = Contests.objects.all().order_by('contest_date').filter(Q(contest_date__gte=today))
    pcontest = Contests.objects.all().order_by('contest_date').filter(Q(contest_date__lt=today))
    is_student = StudentProfile.objects.filter(user_id=request.user.id).exists()
    context = {'contests':contest, 'is_student':is_student,'pcontest':pcontest}
    return render(request, 'Programs/contest.html', context)


@student_required
def add_contest(request):
    if request.method == "POST":
        contest_name = request.POST["cname"]
        branch = request.POST["branch"]
        contest_date = request.POST["date-time"]
        coordinator = request.POST["coordinator"]
        contact_to = request.POST["contact"]
        title = request.POST["title"]
        link = request.POST["link"]
        user = request.user
        contest = Contests.objects.create(
            contest_name=contest_name,
            branch=branch,
            contest_date=contest_date,
            coordinator=coordinator,
            contact_to=contact_to,
            platform_title=title,
            platform_link=link,
            user=user
        )
        contest.save()
        return redirect('contest')

        pass

    return render(request, 'Programs/contest-form.html')


def delete_contest(request,contest_id):
    contest = Contests.objects.filter(id=contest_id).first()
    contest.delete()
    return redirect('contest')


def events(request):
    event = Events.objects.all().order_by('event_date').filter(Q(event_date__gte=today))
    pevent = Events.objects.all().order_by('event_date').filter(Q(event_date__lt=today))
    is_student = StudentProfile.objects.filter(user_id=request.user).exists()
    context = {'events': event, 'is_student': is_student, 'pevents':pevent}
    return render(request, 'Programs/events.html', context)


def add_event(request):
    if request.method == "POST":
        event_name = request.POST['topic-name']
        branch = request.POST.get('branch')
        event_date = request.POST['date-time']
        speaker = request.POST['speaker']
        contact_to = request.POST['contact']
        platform_title = request.POST['title']
        platform_link = request.POST['link']
        user = request.user
        event = Events.objects.create(
            event_name=event_name,
            branch=branch,
            event_date=event_date,
            speaker=speaker,
            contact_to=contact_to,
            platform_title=platform_title,
            platform_link=platform_link,
            user=user
        )

        event.save()
        return redirect('event')

    return render(request, 'Programs/event-form.html')


def delete_event(request, event_id):
    event = Events.objects.filter(id=event_id).first()
    event.delete()
    return redirect('event')
