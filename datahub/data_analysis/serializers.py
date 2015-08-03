from rest_framework.serializers import BaseSerializer, empty


class DatasetSerializer(BaseSerializer):

    def __init__(self, *args, **kwargs):
        self.page_number = kwargs.get('page_number', 1)
        self.page_size = kwargs.get('page_size', 100)
        super().__init__(*args, **kwargs)


    def to_representation(self, instance):
        page = int(self.context["request"].query_params.get("page", self.page_number))
        if not self.page_number:
            return {
                'name': instance.name,
                'data': instance.data.to_json()
            }
        start = (page - 1) * self.page_size
        end = start + self.page_size
        return {
            'name': instance.name,
            'page': page,
            'data': instance.data.iloc[start:end]
        }