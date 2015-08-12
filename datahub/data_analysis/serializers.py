from collections import OrderedDict
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import BaseSerializer, ModelSerializer
from data_analysis.models import Project


class DatasetSerializer(BaseSerializer):

    def __init__(self, *args, **kwargs):
        self.page_number = kwargs.pop('page_number', 1)
        self.page_size = kwargs.pop('page_size', 100)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        columns = [{"data": column} for column in instance.column_list]
        request_columns = self.context["request"].query_params.get("columns", None)
        if request_columns:
            return columns
        page = int(self.context["request"].query_params.get("page", self.page_number))
        start = (page - 1) * self.page_size
        end = min(start + self.page_size, instance.num_obs)
        next_page = None
        prev_page = None
        if end < instance.num_obs:
            next_page = instance.api_link + "?page=" + str(page + 1)
        if start > 0:
            prev_page = instance.api_link + "?page=" + str(page - 1)
        data = instance.data.iloc[start:end].fillna("NaN").as_matrix()
        return OrderedDict([('dataset', instance.name),
                            ('page', page),
                            ('page_size', self.page_size),
                            ('next_page', next_page),
                            ('prev_page', prev_page),
                            ('num_obs', instance.num_obs),
                            ('columns', columns),
                            ('data', data)])


class ProjectSerializer(ModelSerializer):
    datasets = SerializerMethodField()

    class Meta:
        model = Project
        fields = ["name", "datasets"]

    def get_datasets(self, instance):
        return [{"name": dataset.name,
                 "url": dataset.api_link,
                 "columns": dataset.column_list} for dataset in instance.dataset_set.all()]

