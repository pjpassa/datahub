from collections import OrderedDict
from rest_framework.serializers import BaseSerializer


class DatasetSerializer(BaseSerializer):

    def __init__(self, *args, **kwargs):
        self.page_number = kwargs.pop('page_number', 1)
        self.page_size = kwargs.pop('page_size', 100)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        columns = self.context["request"].query_params.get("columns", None)
        if columns:
            for column in instance.data.columns:
                print(column)
            return [{"data": column} for column in instance.data.columns]
        page = int(self.context["request"].query_params.get("page", self.page_number))
        num_obs = len(instance.data.index)
        start = (page - 1) * self.page_size
        end = min(start + self.page_size, num_obs)
        next_page = None
        prev_page = None
        if end < num_obs:
            next_page = instance.api_link + "?page=" + str(page + 1)
        if start > 0:
            prev_page = instance.api_link + "?page=" + str(page - 1)
        data = [OrderedDict(row) for _, row in instance.data.iloc[start:end].iterrows()]
        return OrderedDict([('dataset', instance.name),
                            ('page', page),
                            ('page_size', self.page_size),
                            ('next_page', next_page),
                            ('prev_page', prev_page),
                            ('num_obs', num_obs),
                            # ('columns', instance.data.columns),
                            ('data', data)])
