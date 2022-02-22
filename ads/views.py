import json

from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Category, Ad, User


def root(request):
    return JsonResponse({
        "status": "ok"
    })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(ListView):
    model = Category


    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()

        search_text = request.GET.get("name", None)
        if search_text:
            categories = categories.filter(name=search_text)

        categories = categories.order_by("name")

        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,
            })

        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)

        category = Category.objects.create(
            name=category_data["name"],
        )
        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        category_data = json.loads(request.body)
        self.object.name = category_data["name"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({
            "status": "ok"
        }, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        search_text = request.GET.get("price",None)
        if search_text:
            self.object_list = self.object_list.filter(price= search_text)

        self.object_list = self.object_list.order_by("-price")

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        ads_list = []
        for ad in page_obj:
            ads_list.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
            })
        response = {
            "items": ads_list,
            "total": page_obj.paginator.count,
            "num_pages": page_obj.paginator.num_pages
        }
        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ["name", "author", "price", "description", "address", "is_published"]

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        ad = Ad.objects.create(
            name=ad_data["name"],
            author=ad_data["author"],
            price=ad_data["price"],
            description=ad_data["description"],
            address=ad_data["address"],
            is_published=ad_data["is_published"],
        )

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        }, status=status.HTTP_201_CREATED)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        })

@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ["name", "author", "price", "description", "address", "is_published"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ad_data = json.loads(request.body)
        self.object.name = ad_data["name"]
        self.object.author = ad_data["author"]
        self.object.price = ad_data["price"]
        self.object.description = ad_data["description"]
        self.object.address = ad_data["address"]
        self.object.is_published = ad_data["is_published"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author,
            "price": self.object.price,
            "description": self.object.description,
            "address": self.object.address,
            "is_published": self.object.is_published
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({
            "status": "ok"
        }, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = ["name", "author", "price", "description", "address", "is_published", "logo"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.logo = request.FILES["logo"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author,
            "price": self.object.price,
            "description": self.object.description,
            "address": self.object.address,
            "is_published": self.object.is_published,
            "logo" : self.object.logo.url
        })

@method_decorator(csrf_exempt, name='dispatch')
class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        users = User.objects.all()

        search_text = request.GET.get("username",None)
        if search_text:
            users = users.filter(username= search_text)

        users = users.order_by("username")

        response = []
        for user in users:
            response.append({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "password": user.password,
                "role": user.role,
                "age": user.age,
                "location": user.location,
            })

        return JsonResponse(response, safe=False)



@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ["first_name", "last_name", "username", "password", "role", "age", "location"]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        user = User.objects.create(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            username=user_data["username"],
            password=user_data["password"],
            role=user_data["role"],
            age=user_data["age"],
            location=user_data["location"],
        )

        return JsonResponse({
            "id": user.id,
            "first_name": user.name,
            "last_name": user.author,
            "username": user.price,
            "password": user.description,
            "role": user.address,
            "age": user.is_published,
            "location": user.location,
        }, status=status.HTTP_201_CREATED)

class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()

        return JsonResponse({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "password": user.password,
            "role": user.role,
            "age": user.role,
            "location": user.location,
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ["first_name", "last_name", "username", "password", "role", "age", "location" ]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)
        self.object.username = user_data["username"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "username":  self.object.username,
            "password":  self.object.password,
            "role":  self.object.role,
            "age":  self.object.age,
            "location": self.object.location,
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({
            "status": "ok"
        }, status=200)


class UserAdsView(View):
    def get(self, request):
        user_qs =Ad.objects.annotate(total_ads=Count("is_published"))

        paginator = Paginator(user_qs, settings.TOTAL_ON_PAGE)
        page_number =request.GET.get("page")
        page_obj =paginator.get_page(page_number)

        users = []
        for user in page_obj:
            users.append({
                "id": user.id,
                # "username": user.username,
                # "first_name": user.first_name,
                # "last_name": user.last_name,
                # "role": user.role,
                # "age": user.age,
                # "location": user.location.name,
                "total_ads": user.total_ads,
            })

        response = {
            "items": users,
            "total": page_obj.paginator.count,
            "num_pages": page_obj.paginator.num_pages
        }

        return JsonResponse(response)


