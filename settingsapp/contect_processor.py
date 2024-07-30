from settingsapp.models import Social_links


def get_social_links(request):
    social_links = Social_links.objects.all()
    return {"social_links": social_links}