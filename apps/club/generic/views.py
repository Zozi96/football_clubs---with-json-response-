from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from apps.club.models import League


class LeaguesApiList(View):
    queryset = League.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        data = [{
            'id': str(i.pk),
            'league': str(i.name),
            'country': str(i.country.name),
            'clubs': [{
                'id': str(c.pk),
                'club_name': str(c.name),
            } for c in i.clubs.all()]
        } for i in self.queryset]
        return JsonResponse(data, safe=False)


class LeagueTemplate(TemplateView):
    template_name = 'club/list.html'

    def get_context_data(self, **kwargs):
        context = super(LeagueTemplate, self).get_context_data(**kwargs)
        context['title'] = 'Lista de ligas'
        return context

