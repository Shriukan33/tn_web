from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# hello_asso_2019 = """https://www.helloasso.com/associations/transport-nantes/adhesions/adhesion-transport-nantes-2019/"""
hello_asso_join = """https://www.helloasso.com/associations/transport-nantes/adhesions/adhesion-transport-nantes-2019/"""
hello_asso_don = """https://www.helloasso.com/associations/transport-nantes/formulaires/2"""

@register.simple_tag
def bouton_don(link_text):
    return mark_safe(
        """<a href="{url}" class="btn btn-primary btn-sm" role="button" target="_blank">{text}</a>""".format(
            url=hello_asso_don,
            text=link_text)
    )

@register.simple_tag
def bouton_join(link_text):
    return mark_safe(
        """<a href="{url}" class="btn btn-primary btn-sm" role="button" target="_blank">{text}</a>""".format(
            url=hello_asso_join,
            text=link_text)
    )

@register.simple_tag
def bouton_don_lg(link_text):
    return mark_safe(
        """<a href="{url}" class="btn btn-primary btn-lg" role="button" target="_blank">{text}</a>""".format(
            url=hello_asso_don,
            text=link_text)
    )

@register.simple_tag
def lien_don(link_text):
    return mark_safe(
        """<a href="{url}" target="_blank">{text}</a></p>""".format(
            url=hello_asso_don,
            text=link_text)
    )

@register.simple_tag
def url_don():
    return mark_safe(hello_asso_don)