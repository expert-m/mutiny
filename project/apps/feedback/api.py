from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .forms import *


class ApiFeedbackCreateView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        return Response(['ok'])
    #     self.feedback_form = FeedbackForm(request.POST)
    #
    #     if self.is_spam(request):
    #         messages.add_message(request, messages.INFO, 'Wait 60 sec...')
    #         return render(request, self.template_name, self.get_context_data())
    #
    #     if self.feedback_form.is_valid():
    #         text_content = "Subject: %s\nName: %s\nE-Mail: %s\nIP: %s\n\nText:\n%s" % (
    #             self.feedback_form.cleaned_data['subject'],
    #             self.feedback_form.cleaned_data['name'],
    #             self.feedback_form.cleaned_data['email'],
    #             get_client_ip(request),
    #             self.feedback_form.cleaned_data['message'],
    #         )
    #
    #         send_mail(
    #             self.feedback_form.cleaned_data['subject'],
    #             text_content,
    #             self.feedback_form.cleaned_data['email'],
    #             ['m.sulyak@gmail.com']
    #         )
    #
    #         self.feedback_form = FeedbackForm()
    #
    #         messages.add_message(request, messages.SUCCESS, 'Message send success.')
    #         request.session['last_feedback'] = (datetime.now() + timedelta(seconds=60)).timestamp()
    #     return render(request, self.template_name, self.get_context_data())
    #
    # def is_spam(self, request):
    #     return ('last_feedback' in request.session) and \
    #            (datetime.fromtimestamp(request.session['last_feedback']) > datetime.now())

