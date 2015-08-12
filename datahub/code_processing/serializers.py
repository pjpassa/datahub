from rest_framework import serializers
from rest_framework.serializers import BaseSerializer, ModelSerializer
from code_processing.models import SubmittedCode
from data_analysis.models import Project


class SubmittedCodeSerializer(ModelSerializer):
    code = serializers.CharField()
    project_id = serializers.IntegerField()

    class Meta:
        model = SubmittedCode
        fields = ['code', 'project_id']

    def to_internal_value(self, data):
        return {'code': data.get('code'),
                'project': Project.objects.get(id=int(data.get('project_id')))}

    def create(self, validated_data):
        return SubmittedCode(**validated_data)

    def to_representation(self, instance):
        self.save()
        result = instance.result
        return {"name": result.name,
                "url": result.api_link,
                "columns": result.column_list}
