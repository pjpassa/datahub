from collections import OrderedDict
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import BaseSerializer, Serializer, ModelSerializer


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
"""

class DatasetSerializer(Serializer):
    dataset = SerializerMethodField()
    page = SerializerMethodField()
    page_size = SerializerMethodField()
    next_page = SerializerMethodField()
    prev_page = SerializerMethodField()
    num_obs = SerializerMethodField()
    columns = SerializerMethodField()
    data = SerializerMethodField()

    def __init__(self, *args, **kwargs):
        self.page_number = kwargs.pop('page_number', 1)
        self.page_size = kwargs.pop('page_size', 100)
        super().__init__(*args, **kwargs)

    def get_dataset(self, instance):
        return instance.name

    def get_page(self, instance):
        return int(self.context["request"].query_params.get("page", self.page_number))

    def get_page_size(self, instance):
        return self.page_size

    def get_next_page(self, instance):
        page = int(self.context["request"].query_params.get("page", self.page_number))
        if instance.num_obs < int(self.page_size * page):
            return instance.api_link + "?page=" + str(page + 1)

    def get_prev_page(self, instance):
        page = int(self.context["request"].query_params.get("page", self.page_number))
        if page > 1:
            return instance.api_link + "?page=" + str(page - 1)

    def get_num_obs(self, instance):
        return instance.num_obs

    def get_columns(self, instance):
        return [{"data": column} for column in instance.column_list]

    def get_data(self, instance):
        page = int(self.context["request"].query_params.get("page", self.page_number))
        start = (page - 1) * self.page_size
        end = min(start + self.page_size, instance.num_obs)
        return instance.data.iloc[start:end].fillna("NaN").as_matrix()
"""
