from rest_framework import viewsets
from rest_framework.response import Response
from .models import Make, Model, CarType
from django.db.models import Q

class CarSearchViewSet(viewsets.ViewSet):
    def list(self, request):
        query_text = request.query_params.get('make', '')
        texts_to_search = [text.strip() for text in query_text.split(',')]
        search_conditions = Q()

        for text in texts_to_search:
            search_conditions |= Q(make__name__icontains=text) | Q(model__name__icontains=text) | Q(name__icontains=text)

        results = CarType.objects.filter(search_conditions)

        items = [{
            "make": result.model.make.name,
            "model": result.model.name,
            "car_type": result.name,
            "car_type_id": result.id,
        } for result in results]

        return Response({"items": items})
