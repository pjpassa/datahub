from rest_framework import generics
from code_processing.models import SubmittedCode
from code_processing.serializers import SubmittedCodeSerializer


class SubmittedCodeCreateAPIView(generics.CreateAPIView):
    serializer_class = SubmittedCodeSerializer


    def get_queryset(self):
        return SubmittedCode.objects.all()

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
