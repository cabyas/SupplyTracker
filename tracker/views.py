from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from tracker.models import Token


class HomeView(ListView):
    model = Token
    template_name = 'tracker/index.html'
    paginate_by = 30


class TokenDetailView(DetailView):
    model = Token
    slug_field = 'contract_address'
    slug_url_kwarg = 'contract_address'
    template_name = 'tracker/token_detail.html'
