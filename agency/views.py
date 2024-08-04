from django.shortcuts import render
from agency.models import GeneralInfo, Blog
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def home(request):
    general_info = GeneralInfo.objects.first()
    recent_blog = Blog.objects.all().order_by("-created_at")[:3]
    context = {
        "agency_name": general_info.agency_name,
        "location": general_info.location,
        "email": general_info.email,
        "phone": general_info.phone,
        "twitter": general_info.twitter_url,
        "open_hours": general_info.open_hours,
        "recent_blog": recent_blog,
    }
    return render(request, "home.html", context)


def blog(request):
    all_blogs = Blog.objects.all().order_by("-created_at")
    blog_per_page = 3
    paginator = Paginator(all_blogs, blog_per_page)
    page = request.GET.get("page")
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context = {
        "blogs": blogs,
    }

    return render(request, "blog.html", context)


# ckeditor


def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    recent_blog = Blog.objects.all().exclude(id=blog_id).order_by("-created_at")[:2]
    context = {
        "blog": blog,
        "recent_blog": recent_blog,
    }
    return render(request, "blog_detail.html", context)
