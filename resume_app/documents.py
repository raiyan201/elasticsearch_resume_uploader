from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import * 

@registry.register_document
class myuploadfileDocument(Document):
    class Index:
        name = "myuploadfile"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = myuploadfile
        fields = [
            "role_name",
            "location",
            "company_name",
            "f_name",
            "status",
            "myfiles",
            "created_at",
            "created_by",
            "is_Delete",
            "extracted_text",
        ]