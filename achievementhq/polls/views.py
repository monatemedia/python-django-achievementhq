from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Question, Choice

@login_required
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    if not latest_question_list:
        messages.info(request, "No polls are available at the moment. Please check back later.")
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

@login_required
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        messages.error(request, "The poll you are looking for does not exist.")
        return redirect('polls:index')
    return render(request, 'polls/detail.html', {'question': question})

@login_required
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        messages.error(request, "You didn't select a valid choice. Please try again.")
        return render(request, 'polls/detail.html', {
            'question': question,
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        messages.success(request, "Your vote has been successfully recorded!")
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
