from django.shortcuts import redirect, render
from .models import Room
from .forms import RoomForm

def home(request):
    rooms = Room.objects.all()
    context = {"rooms":rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room":room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    formroom = RoomForm()

    if request.method == 'POST':
        formroom = RoomForm(request.POST)
        if formroom.is_valid():
            formroom.save()
            return redirect('home')
    context = {'roomfields':formroom}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'roomfields':form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})


