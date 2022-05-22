from django.views.generic import TemplateView
from apps.content.models import CategoryService,Comment,News


class LandingView(TemplateView):
    """
    Лэндиннг сайта
    """

    template_name="landing.html"

    def get_context_data(self, **kwargs):
        """
        Контекст данных лэндинга
        """
        data = super().get_context_data(**kwargs)
        data["category_service"] = CategoryService.objects.filter(is_published=True)
        data["news"] = News.objects.filter(is_published_landing=True,)
        data["comments"] = Comment.objects.filter(is_published_landing=True)
        return data
