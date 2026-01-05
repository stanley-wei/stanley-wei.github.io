---
layout: default
sitemap: false
permalink: /life-list
---
<div class="row container-fluid" markdown="0">
    <h2>Life List</h2>
    {% for item in site.data.life_list %}
        <div class="col col-lg-4">
            <div class="image-hover-wrapper">
                <img class="image-hover-img" src="{{site.base_url}}{{item.thumbnail}}"/>
                <div class="image-hover-desc d-sm-none d-md-flex">
                    <p class="image-hover-text">
                        <b>{{item.name}}</b> <br /> {{item.location}} <br /> {{item.date}}
                    </p>
                </div>
                <div class="d-md-none">
                    </br>
                </div>
            </div>
        </div>
    {% endfor %}
</div>