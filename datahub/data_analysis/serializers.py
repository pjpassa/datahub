from collections import OrderedDict
from rest_framework.serializers import BaseSerializer


class DatasetSerializer(BaseSerializer):

    def __init__(self, *args, **kwargs):
        self.page_number = kwargs.pop('page_number', 1)
        self.page_size = kwargs.pop('page_size', 100)
        super().__init__(*args, **kwargs)


    def to_representation(self, instance):
        page = int(self.context["request"].query_params.get("page", self.page_number))
        if not self.page_number:
            return OrderedDict([('dataset', instance.name),
                                ('data', instance.data)])
        start = (page - 1) * self.page_size
        end = start + self.page_size
        return OrderedDict([('dataset', instance.name),
                            ('page', page),
                            ('columns', instance.data.columns),
                            ('data', instance.data.iloc[start:end])])
