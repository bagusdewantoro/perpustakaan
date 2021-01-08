from django.shortcuts import render
from katalog.models import Buku, Penulis, Jenis, InstanceBuku
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin   # membuat VIEWS ini restricted : Harus login dulu untuk bisa mengakses
from django.contrib.auth.mixins import PermissionRequiredMixin  # membuat VIEWS ini hanya bisa diakses oleh user dengan PERMISSION

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

# membuat VIEWS ini restricted : Harus login dulu untuk bisa mengakses
class PenulisDetailView(LoginRequiredMixin, generic.DetailView): # masukkan 'LoginRequiredMixin' sebagai argumen pertama sebelum views
    model = Penulis
    login_url = '/accounts/login/' # tambahkan object ini supaya bisa restricted hanya Users

# Untuk user: mengecek buku yang dipinjam user tersebut
class BukuDisewaUserListView(LoginRequiredMixin, generic.ListView):
    model = InstanceBuku
    template_name = 'katalog/buku_pinjaman_saya.html'
    paginate_by = 10

    def get_queryset(self):
        return InstanceBuku.objects.filter(peminjam=self.request.user).filter(status__exact='s').order_by('kembali')

# Untuk staff (pustakawan): mengecek buku yang dipinjam oleh seluruh user
class SeluruhBukuDipinjamListView(PermissionRequiredMixin, generic.ListView):
    """Only visible to users with can_mark_returned permission."""
    model = InstanceBuku
    permission_required = 'katalog.bisa_tandai_kembali'
    template_name = 'katalog/buku_pinjaman_seluruh_user.html'
    paginate_by = 10

    def get_queryset(self):
        return InstanceBuku.objects.filter(status__exact='s').order_by('kembali')
