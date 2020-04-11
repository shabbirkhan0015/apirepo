from rest_framework.serializers import ModelSerializer
from .models import Branch

class BranchSerialzer(ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class BankcitySerialzer(ModelSerializer):
    class Meta:
        model = Branch
        fields = ('name', 'bank','city')
