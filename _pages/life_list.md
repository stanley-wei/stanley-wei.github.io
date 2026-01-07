---
layout: default
sitemap: false
permalink: /life-list
---
<div class="row container-fluid" markdown="0">
    <h2>Life List (incomplete)</h2>
    {% for item in site.data.life_list %}
        <div class="col col-12 col-lg-4 mb-3" style="max-height:400px">
            <div class="image-hover-wrapper">
                <img class="image-hover-img" src="{{site.base_url}}{{item.thumbnail}}" loading="lazy"/>
                <div class="image-hover-caption">
                    {{item.name}}
                </div>
                <div class="image-hover-desc">
                    <p class="image-hover-text">
                        <b>{{item.name}}</b> <br /> {{item.location}} <br /> {{item.date}}
                    </p>
                </div>
            </div>
        </div>
    {% endfor %}
</div>