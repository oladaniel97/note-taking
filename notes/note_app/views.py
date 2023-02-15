from django.shortcuts import render,redirect
from .models import Note
# Create your views here.

def editor(request):
    docid = int(request.GET.get('docid',0))
    notes = Note.objects.all()

    if request.method =='POST':
        docid = int(request.POST.get('docid',0))
        title = request.POST.get('title')
        content = request.POST.get('content','')

        if docid > 0:
            note = Note.objects.get(pk=docid)
            note.title = title
            note.content = content
            note.save()

            return redirect('/?docid=%i' % docid)
        else:
            note = Note.objects.create(title=title,content=content)

            return redirect('/?docid=%i' % note.id)

    if docid > 0:
        note = Note.objects.get(pk=docid)
    else:
        note = ''
    context = {
        'docid':docid,
        'notes':notes,
        'note':note
    }

    return render(request,'editor.html',context)

def delete(request, docid):
    note = Note.objects.get(pk=docid)
    note.delete()

    return redirect('/?docid=0')