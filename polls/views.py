from django.db.models import F
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Choice, Question, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import RegistrationForm
from django.db import connection, IntegrityError


@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

@method_decorator(login_required, name='dispatch')
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

@method_decorator(login_required, name='dispatch')
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

@login_required
def vote(request, question_id):
    #A01:2021 – Broken Access Control
    """ profile, created = UserProfile.objects.get_or_create(user=request.user)
    if not profile.verified:
        return HttpResponseForbidden("You are not allowed to vote. Verification is required.") """
    #A03:2021 – Injection
    question_id = request.GET.get("question_id", question_id)
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM polls_question WHERE id = {question_id}")
        question_data = cursor.fetchone()
    """with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM polls_question WHERE id = %s", [question_id])
        question_data = cursor.fetchone()"""
    if not question_data:
        return HttpResponseForbidden("Question does not exist.")
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )
            user_profile = UserProfile(
                user=user,
                verified=form.cleaned_data["verified"],
            )
            user_profile.set_address(form.cleaned_data["address"])
            user_profile.save()

            return redirect("")
    else:
        form = RegistrationForm()
    
    return render(request, "polls/register.html", {"form": form})
