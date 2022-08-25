
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

# Create your views here.
from lajkacorp.forms import AddUserForm, AddAlbumForm, AddIncomeForm, AddStoreroomForm, AddDistroForm, \
    AddIncomeSpliterForm
from lajkacorp.models import User, MusicAlbum, Storeroom, Distribution, Message, Income, ArtistIncomeSpliter


class ArtistAlbumsListView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = []

    def get(self, request):
        albums = MusicAlbum.objects.all().order_by('author')
        return render(request, 'artist_card_view.html', {'artists': albums})


class AddArtistView(LoginRequiredMixin, View):
    permission_required = []

    def get(self, request):
        form = AddUserForm()
        return render(request, 'add_new.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('artist_list'))
        return render(request, 'add_new.html', {'form': form})


class ArtistUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = []
    model = User
    fields = '__all__'
    template_name = 'user_update_form.html'


class ArtistDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = []
    model = User
    success_url = reverse_lazy('settings')
    template_name = 'user_confirm_delete.html'


class AddAlbumView(PermissionRequiredMixin, View):
    permission_required = []

    def get(self, request):
        form = AddAlbumForm()
        return render(request, 'add_new.html', {'form': form})

    def post(self, request):
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('artist_list'))
        return render(request, 'add_new.html', {'form': form})


class DeleteAlbumView(PermissionRequiredMixin, DeleteView):
    permission_required = []
    model = MusicAlbum
    success_url = reverse_lazy('settings')


class AddIncomeView(PermissionRequiredMixin, View):
    permission_required = []

    def get(self, request):
        form = AddIncomeForm()
        return render(request, 'add_new.html', {'form': form})

    def post(self, request):
        form = AddIncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('income_list'))
        return render(request, 'add_new.html', {'form': form})


class IncomeListView(PermissionRequiredMixin, View):
    permission_required = []

    def get(self, request):
        user = request.user
        albums = MusicAlbum.objects.filter(author=user)
        incomes = Income.objects.filter(album__in=albums)
        incomes_total = sum(incomes.values_list('income', flat=True))

        return render(request, 'artist_income_view.html',
                      {'incomes': incomes, 'total_inc': incomes_total})


class IncomeListViewAll(LoginRequiredMixin,PermissionRequiredMixin, View):
    permission_required = []

    def get(self, request):
        incomes = Income.objects.all().order_by('month2')
        incomes_total = sum(incomes.values_list('income', flat=True))
        return render(request, 'income_all.html',
                      {'incomes': incomes, 'total_inc': incomes_total})


class IncomeUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = []
    model = Income
    fields = '__all__'
    success_url = reverse_lazy('income_all')
    template_name = 'income_update_form.html'


class IncomeDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = []
    model = Income
    success_url = reverse_lazy('index')
    template_name = 'income_confirm_delete.html'


class AddStoreRoomView(View):

    def get(self, request):
        form = AddStoreroomForm()
        return render(request, 'add_new.html', {'form': form})

    def post(self, request):
        form = AddStoreroomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('settings'))
        return render(request, 'add_new.html', {'form': form})


class UpdateStoreRoomView(UpdateView):
    model = Storeroom
    fields = '__all__'
    template_name_suffix = '_update_form'


class DeleteStoreRoomView(PermissionRequiredMixin, DeleteView):
    permission_required = []
    model = Storeroom
    success_url = reverse_lazy('settings')
    template_name = 'storeroom_confirm_delete.html'


class AddDistroView(View):

    def get(self, request):
        form = AddDistroForm()
        return render(request, 'add_new.html', {'form': form})

    def post(self, request):
        form = AddDistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        return render(request, 'add_new.html', {'form': form})


class MessageDetailView(View):
    pass


class AddIncomeSpliter(View):

    def get(self, request):
        form = AddIncomeSpliterForm()
        return render(request, 'add_new.html', {'form': form})

    def post(self, request):
        form = AddIncomeSpliterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        return render(request, 'add_new.html', {'form': form})


class SettingsView(PermissionRequiredMixin, View):
    permission_required = []

    def get(self, request):
        return render(request, 'settings.html')


class StoreRoomView(PermissionRequiredMixin, View):
    permission_required = []

    def get(self, request):
        storeroom = Storeroom.objects.all()
        return render(request, 'storeroom_view.html', {'storeroom': storeroom})


class StoreroomUserView(View):

    def get(self, request):
        user = request.user
        albums = MusicAlbum.objects.filter(author=user)
        storeroom_all = Storeroom.objects.filter(album__in=albums)
        return render(request, 'storeroom_artist_view.html',
                      {'storeroom': storeroom_all})


# permision = ['lajkacorp.view_artistincomespliter','lajkacorp.delete_artistincomespliter','lajkacorp.change_artistincomespliter','lajkacorp.add_artistincomespliter','lajkacorp.view_income','lajkacorp.delete_income',
#                            'lajkacorp.change_income','lajkacorp.add_income','lajkacorp.view_message','lajkacorp.delete_message','lajkacorp.change_message','lajkacorp.add_message',
#                            'lajkacorp.view_storeroom','lajkacorp.delete_storeroom','lajkacorp.change_storeroom','lajkacorp.add_storeroom','lajkacorp.view_musicalbum','lajkacorp.delete_distribution',
#                            'lajkacorp.delete_musicalbum','lajkacorp.change_musicalbum','lajkacorp.add_musicalbum','lajkacorp.view_distribution','lajkacorp.','lajkacorp.',
#                            'lajkacorp.change_distribution','lajkacorp.add_distribution','lajkacorp.view_session','lajkacorp.delete_session','lajkacorp.change_session','lajkacorp.add_session','lajkacorp.view_contenttype','lajkacorp.delete_contenttype','lajkacorp.change_contenttype','lajkacorp.add_contenttype','lajkacorp.view_user','lajkacorp.delete_user','lajkacorp.change_user','lajkacorp.add_user','lajkacorp.view_group',
#                            'lajkacorp.delete_group','lajkacorp.change_group','lajkacorp.add_group','lajkacorp.view_permission','lajkacorp.delete_permission','lajkacorp.change_permission','lajkacorp.add_permission','lajkacorp.view_logentry','lajkacorp.delete_logentry','lajkacorp.change_logentry','lajkacorp.add_logentry',]