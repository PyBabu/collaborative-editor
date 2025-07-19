from django.shortcuts import render, get_object_or_404
from .models import Document
from django.contrib.auth.decorators import login_required

@login_required
def editor_view(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    return render(request, 'editor/editor.html', {'document': document})

from django.contrib.auth.decorators import login_required
from .models import Document
from django.shortcuts import render

@login_required
def document_list(request):
    docs = Document.objects.all()
    return render(request, 'editor/list.html', {'documents': docs})


from django.http import JsonResponse
from .utils import check_grammar
# from django.views.decorators.csrf import csrf_exempt
import json

from django.views.decorators.csrf import csrf_protect

@csrf_protect
@login_required
def grammar_check_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        text = data.get('text', '')
        matches = check_grammar(text)
        return JsonResponse({'matches': matches})


# New Document

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Document

@login_required
def create_document(request):
    if request.method == 'POST':
        title = request.POST.get('title', 'Untitled Document')
        doc = Document.objects.create(title=title, owner=request.user)
        return redirect('editor', doc_id=doc.id)
    return render(request, 'editor/create.html')
