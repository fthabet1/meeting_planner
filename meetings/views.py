from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Room
from .forms import MeetingForm

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk = id)
    return render(request, "meetings/detail.html", {
        "meeting": meeting
    })

def rooms(request):
    rooms = Room.objects.all()
    return render(request, "meetings/rooms.html", {
        "rooms": rooms,
    })

def room_info(request, id):
    room = get_object_or_404(Room, pk = id)
    return render(request, "meetings/room_info.html", {
        "name": room.name,
        "floor": room.floor_number,
        "room": room.room_number 
    })

def new(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {
        "form": form
    })