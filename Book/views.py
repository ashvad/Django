from django.shortcuts import render, redirect

# Create your views here.

from Book.forms import BookForm, OrderEditForm
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, TemplateView
from Book.models import Books
from customer.models import Orders
from django.core.mail import send_mail


class BookView(CreateView):
    model = Books
    form_class = BookForm
    template_name = "book_add.html"
    success_url = reverse_lazy("allbooks")

    # def get(self, request):
    #     form = BookForm()
    #     return render(request, "book_add.html", {"form": form})
    #
    # def post(self, request):
    #     form = BookForm(request.POST, files=request.FILES)
    #     if form.is_valid():
    #         # print(form.cleaned_data)
    #         # print(form.cleaned_data.get("book_name"))
    #         # print(form.cleaned_data.get("author"))
    #         # print(form.cleaned_data.get("amount"))
    #         # print(form.cleaned_data.get("copies"))
    #         #
    #         # qs=Books(book_name=form.cleaned_data.get("book_name"),
    #         #          author=form.cleaned_data.get("author"),
    #         #          amount=form.cleaned_data.get("amount"),
    #         #          copies=form.cleaned_data.get("copies"))
    #         # qs.save()
    #         form.save()
    #
    #         # return render(request, "book_add.html", {"msg": "book created"})
    #         return redirect("allbooks")
    #     else:
    #         return render(request, "book_add.html", {"form": form})


class BookList(ListView):
    model = Books
    template_name = "book_list.html"
    context_object_name = "books"
    # def get(self, request):
    #     print("here")
    #     qs = Books.objects.all()
    #     return render(request, 'book_list.html', {'books': qs})


class Bookdetails(DetailView):
    model = Books
    template_name = "book_detail.html"
    context_object_name = "book"

    pk_url_kwarg = "id"

    # def get(self, request, *args, **kwargs):
    #     # pass
    #     # kwargs
    #     qs = Books.objects.get(id=kwargs.get("id"))
    #     return render(request, 'book_detail.html', {'book': qs})


class BookdeleteView(View):
    def get(self, request, *args, **kwargs):
        qs = Books.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("allbooks")


class ChangeBook(UpdateView):
    model = Books
    template_name = "book_change.html"
    form_class = BookForm
    success_url = reverse_lazy("allbooks")
    pk_url_kwarg = "id"
    # def get(self, request, *args, **kwargs):
    #     qs = Books.objects.get(id=kwargs.get("id"))
    #     form = BookForm(instance=qs)
    #     return render(request, "book_change.html", {"form": form})
    #
    # def post(self, request, *args, **kwargs):
    #     qs = Books.objects.get(id=kwargs.get("id"))
    #     form = BookForm(request.POST, instance=qs, files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("allbooks")


class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        new_orders = Orders.objects.filter(status="order_placed")
        return render(request, self.template_name, {"new_orders": new_orders})


class OrderdetailView(DetailView):
    model = Orders
    template_name = "order_detail.html"
    context_object_name = "order"
    pk_url_kwarg = "id"


class OrderUpdateView(UpdateView):
    model = Orders
    template_name = "order_update.html"
    form_class = OrderEditForm
    pk_url_kwarg = "id"

    def get(self, request, *args, **kwargs):
        order = Orders.objects.get(id=kwargs["id"])
        return render(request, self.template_name, {"order": order, "form": self.form_class})

    def post(self, request, *args, **kwargs):
        order = Orders.objects.get(id=kwargs["id"])
        form = OrderEditForm(request.POST, instance=order)
        if form.is_valid():
            delivery_date = str(form.cleaned_data.get("expected_delivery_date"))
            form.save()
            send_mail(
                'Order Notification',
                'Your order will be delivered on' + delivery_date,
                'ashvadshajan@gmail.com',
                ['advaithahariharans@gmail.com'],
                fail_silently=False,
            )

            return redirect("dashboard")
