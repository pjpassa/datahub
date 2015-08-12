from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from code_processing.models import SubmittedCode
from code_processing.serializers import SubmittedCodeSerializer
from data_analysis.models import Project


class SubmittedCodeCreateAPIView(generics.CreateAPIView):
    serializer_class = SubmittedCodeSerializer


    def get_queryset(self):
        return SubmittedCode.objects.all()

    def dispatch(self, request, *args, **kwargs):
        project = Project.objects.get(id=int(request.POST.get('project_id')))
        if project.profile.user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
