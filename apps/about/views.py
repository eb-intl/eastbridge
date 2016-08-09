#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import ContentBox


class IndexView(generic.ListView):
    template_name = 'about/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return ContentBox.objects.all()[:5]


class DetailView(generic.DetailView):
    model = ContentBox
    template_name = 'about/detail.html'


class ResultsView(generic.DetailView):
    model = ContentBox
    template_name = 'about/results.html'

'''
def vote(request, poll_id):
    p = get_object_or_404(ContentBox, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, ContentBox.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
'''
