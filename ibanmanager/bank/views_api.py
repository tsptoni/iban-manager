# -*- coding: utf-8 -*-

import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import serializers as rf_serializers

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance

from thearomatrace.places import models as place_models
from thearomatrace.places import serializers as place_serializers



class PlaceFilter(django_filters.FilterSet):

    from_date = django_filters.IsoDateTimeFilter(name="created_at", lookup_expr='gte')
    to_date = django_filters.IsoDateTimeFilter(name="created_at", lookup_expr='lte')


    def get_name(self, name, value):
        qs = self.filter(name__unaccent__icontains=value).order_by(name) # .order_by(Length(name).asc())
        return qs

    name = django_filters.CharFilter(method=get_name)


    class Meta:
        model = place_models.Place
        fields = '__all__'
        exclude = ('location',)



class PlaceViewSet(ModelViewSet):

    queryset = place_models.Place.objects.all()
    serializer_class = place_serializers.PlaceSerializer

    filter_class = PlaceFilter
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = super(PlaceViewSet, self).get_queryset()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)

        center_lat = self.request.query_params.get('center_lat', None)
        center_lon = self.request.query_params.get('center_lon', None)
        radius = self.request.query_params.get('radius', None)

        point_lookup_param_present = center_lat is not None or center_lon is not None or radius is not None

        if point_lookup_param_present:

            if center_lon is None:
                raise rf_serializers.ValidationError('center_lon parameter is missing')
            if center_lat is None:
                raise rf_serializers.ValidationError('center_lat parameter is missing')
            if radius is None:
                raise rf_serializers.ValidationError('radius parameter is missing')

            if float(radius) > place_models.PLACE_LOOKUP_MAX_RADIUS:
                raise rf_serializers.ValidationError('radius parameter is above maximum ({} meters)'.format(place_models.PLACE_LOOKUP_MAX_RADIUS))

            queryset = queryset.filter(location__distance_lt=(Point(float(center_lon), float(center_lat)), Distance(m=radius)))

        return queryset
