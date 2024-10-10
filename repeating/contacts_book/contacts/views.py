from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from .models import Contact
from .forms import ContactForm, ContactSearchForm
from django.contrib.auth.mixins import LoginRequiredMixin
import os
from django.http import FileResponse, JsonResponse
from django.conf import settings
from .mixins import LoggingMixin


def search_contact(request):
    if request.method == 'POST':
        form = ContactSearchForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            results = Contact.objects.filter(name__icontains=contact_name)
            return render(request, 'search_results.html', {'form': form, 'results': results})
    else:
        form = ContactSearchForm()

    results = Contact.objects.all()
    return render(request, 'search_results.html', {'form': form, 'results': results})



def my_json_view(request):
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return JsonResponse(data)

def my_file_view(request):
    #file_path = os.path.join('path', 'to', 'your', 'file.pdf')
    file_path = os.path.join(settings.MEDIA_ROOT, 'files', "ukol.txt")
    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename='downloaded_file.txt')
    return response

def my_image_view(request):
    filename = "img.png"
    file_path = os.path.join(settings.MEDIA_ROOT, 'images', filename)
    response = FileResponse(open(file_path, 'rb'), as_attachment=False, filename='downloaded.png')
    return response



class ContactListView(ListView, LoggingMixin):
    model = Contact
    template_name = 'contacts_list.html'
    context_object_name = 'page_obj'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.log_action('View')
        return super().get(request, *args, **kwargs)


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = reverse_lazy('contacts_list')


class ContactUpdateView(LoginRequiredMixin, UpdateView, LoggingMixin):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = reverse_lazy('contacts_list')

    def form_valid(self, form):
        self.log_action('Update')
        return super().form_valid(form)

class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'contact_confirm_delete.html'
    success_url = reverse_lazy('contacts_list')

