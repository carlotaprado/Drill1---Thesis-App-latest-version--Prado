from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Thesis, Comment
from .models import Thesis
from django.db.models import Q

def thesis_list(request):
    thesis_list = Thesis.objects.all()
    paginator = Paginator(thesis_list, 2)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'thesis/thesis_list.html', {'page_obj': page_obj})

def thesis_detail(request, thesis_id):
    thesis = get_object_or_404(Thesis, pk=thesis_id)
    return render(request, 'thesis/thesis_detail.html', {'thesis': thesis})

def thesis_search(request):
    """View function to perform a search for theses."""
    query = request.GET.get('q')
    if query:
        results = Thesis.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(abstract__icontains=query))
    else:
        results = None
    return render(request, 'thesis/thesis_search.html', {'query': query, 'results': results})

def add_comment_to_thesis(request, pk):
    """View function to add a comment to a thesis."""
    thesis = get_object_or_404(Thesis, pk=pk)
    if request.method == 'POST':
        text = request.POST.get('comment_text')
        Comment.objects.create(thesis=thesis, text=text)
        # Redirect to the same page after submitting the comment
        return redirect('thesis_detail', thesis_id=pk)
    return render(request, 'thesis/add_comment_to_thesis.html', {'thesis': thesis})
