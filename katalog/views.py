from django.shortcuts import render
from katalog.models import Buku, Penulis, Jenis, InstanceBuku
from django.views import generic

def index(request):
    """Fungsi view untuk home page"""

    # generate jumlah dari beberapa object utama
    jml_buku = Buku.objects.all().count()
    jml_copy = InstanceBuku.objects.all().count()

    # buku yang ada/tersedia
    jml_copy_ada = InstanceBuku.objects.filter(status__exact='a').count()

    # all() sudah tersirat by default
    jml_penulis = Penulis.objects.count()

    # menghitung jumlah visit di views ini, terhitung dari variabel SESSION
    jml_visits = request.session.get('jml_visits', 1)
    request.session['jml_visits'] = jml_visits + 1

    konteks = {
        'jml_buku': jml_buku,
        'jml_copy': jml_copy,
        'jml_copy_ada': jml_copy_ada,
        'jml_penulis': jml_penulis,
        'jml_visits' : jml_visits,   # konteks jumlah visit
    }

    # render template html index.html dengan data di dalam variabel context
    return render(request, 'index.html', context=konteks)


class BukuListView(generic.ListView):    # nama class boleh diganti, asal sama kaya di urls.py
    model = Buku
    context_object_name = 'koleksi_buku'   # default = buku_list   (context di dalam templatenya)
    template_name = 'katalog/daftar_buku.html'  # default = buku_list.html   (lokasi & nama file html)
    paginate_by = 7

class BukuDetailView(generic.DetailView):   # nama class boleh diganti, asal sama kaya di urls.py
    model = Buku
    # context_object_name  by default = buku_detail

class PenulisListView(generic.ListView):
    model = Penulis

from django.contrib.auth.mixins import LoginRequiredMixin   # membuat VIEWS ini restricted : Harus login dulu untuk bisa mengakses
class PenulisDetailView(LoginRequiredMixin, generic.DetailView): # masukkan 'LoginRequiredMixin' sebagai argumen pertama sebelum views
    model = Penulis
    login_url = '/akun/login/' # tambahkan object ini supaya bisa restricted hanya Users
