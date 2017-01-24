{% assign posts_all=site.documents | where:"lang", page.lang | sort: "date" | reverse %}
{% assign  posts = "" | split:"|"  %}
{% for post in posts_all %}
{% if post.no_publish == true %}
{% else %}
{% assign posts = posts | push: post %}
{% endif %}
{% endfor %}

{% for post in posts limit:3 %} | <br/>[{{post.title | truncate:30}}<br/>{% if post.img %}<img style="margin-top:10px;" src="{{ site.baseurl }}/assets/{{ post.assets }}post/{{ post.img }}"/>{% endif %}]{% if post.external %}({{post.external}})<br/><small>{% if post.type == "blerifa" %}{{site.data.trad['blerifa'][page.lang]}}{% elsif post.type == "old_slides" %}{{site.data.trad['slides'][page.lang]}}{% endif %}</small><br/>{% else %}{% if post.type == "slides" %}({{post.url | prepend: site.baseurl }})<br/><small>{{site.data.trad['slides'][page.lang]}}</small><br/>{% else %}({{post.url | prepend: site.baseurl }})<br/><small>{{site.data.trad['post'][page.lang]}}</small><br/>{% endif %}{% endif %} {%endfor%} |
{: class="resptable resp3 card1_dark card2_dark card3_dark"}
