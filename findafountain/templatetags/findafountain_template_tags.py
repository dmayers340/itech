from django import template
from findafountain.models import Category

register = template.Library()
@register.inclusion_tag('findafountain/cats.html') 
def get_category_list():
	return {'cats': Category.objects.all()}
<ul> 
	{% if cats %}
		{% for c in cats %}
			<li><a href="{% url 'show_category' c.slug %}">{{ c.name }}</a></li>
		{% endfor %} 
	{% else %}
		<li><strong>There are no categories present.</strong></li> 
		{% endif %}
</ul>
