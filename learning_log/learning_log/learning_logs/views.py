from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from .forms import TopicForm, RecordForm
from .models import *


def index(request):
    """Home page of app Learning Log"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Print all the topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_add')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Print the topic and all its records"""
    topic = Topic.objects.get(id=topic_id)
    # Проверка того, что тема принадлежит пользователю
    if topic.owner != request.user:
        raise Http404

    records = topic.record_set.order_by('-date_add')
    context = {'topic': topic, 'records': records}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Определяет новую тему"""
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    else:
        form = TopicForm()

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_record(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request != 'POST':
        form = RecordForm()
    else:
        form = RecordForm(request.POST)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.topic = topic
            new_record.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_record.html', context)


@login_required
def edit_record(request, record_id):
    record = Record.objects.get(id=record_id)
    topic = record.topic
    if topic.owner != request.user:
        raise Http404

    if request != 'POST':
        form = RecordForm(instance=record)
    else:
        form = RecordForm(instance=record, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'record': record, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_record.html', context)





