from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


# Create your views here.
def index(req):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # context = {
    #     "latest_question_list": latest_question_list,
    # }
    # return HttpResponse(template.render(context, req))
    context = {"latest_question_list": latest_question_list}
    return render(req, "polls/index.html", context)


def detail(req, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "polls/detail.html", {"question": question})


def results(req, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(req, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
