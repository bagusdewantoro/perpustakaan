from django.shortcuts import render
from katalog.models import Buku, Penulis, Jenis, InstanceBuku
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin   # membuat VIEWS ini restricted : Harus login dulu untuk bisa mengakses
from django.contrib.auth.mixins import PermissionRequiredMixin  # membuat VIEWS ini hanya bisa diakses oleh user dengan PERMISSION

# form perbarui buku:
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from katalog.forms import PerbaruiBukuForm

# form modifikasi PENULIS & BUKU
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from katalog.models import Penulis, Buku


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


# =========================================================================
# views FORM untuk pustakawan memperbarui tanggal pengembalian pinjaman buku
@login_required
@permission_required('katalog.bisa_tandai_kembali', raise_exception=True)
def perbarui_buku_pustakawan(request, pk):
    buku_instance = get_object_or_404(InstanceBuku, pk=pk)

    # jika ini adalah POST request, maka lakukan proses data Form
    if request.method == 'POST':
        # membuat instance form dan populate form tsb dengan data dari requst (binding)
        form = PerbaruiBukuForm(request.POST)
        # cek jika form sudah valid:
        if form.is_valid():
            # memproses data di form.cleaned_data
            buku_instance.kembali = form.cleaned_data['perbarui_tanggal']
            buku_instance.save()
            # redirect ke url:
            return HttpResponseRedirect(reverse('seluruh-pinjaman'))

    # jika ini adalah GET (atau metode lain), buatlah default form.
    else:
        usulan_perbarui_tanggal = datetime.date.today() + datetime.timedelta(weeks=3)
        form = PerbaruiBukuForm(initial={'perbarui_tanggal' : usulan_perbarui_tanggal})

    context = {
        'form' : form,
        'buku_instance' : buku_instance,
    }

    return render(request, 'katalog/buku_perbarui_pustakawan.html', context)


# =========================================================================
# FORM untuk modifikasi PENULIS
class PenulisCreate(CreateView):
    model = Penulis
    fields = ['nama_depan', 'nama_belakang', 'tanggal_lahir', 'tanggal_wafat']
    initial = {'tanggal_lahir': '11/06/1970'}
    permission_required = 'katalog.bisa_tandai_kembali'

class PenulisUpdate(UpdateView):
    model = Penulis
    fields = '__all__' # NOT Recommended. Security issue jika fields baru ditambahkan
    permission_required = 'katalog.bisa_tandai_kembali'

# By Default, nama templatenya harus: namaclassdimodel_form.html --> contoh penulis_form.html
# Untuk ganti suffix selain 'form', bisa tambah field template_name_suffix = 'othersuffix'

class PenulisDelete(DeleteView):
    model = Penulis
    success_url = reverse_lazy('penulis')
    permission_required = 'katalog.bisa_tandai_kembali'
# By Default, nama templatenya harus: namaclassdimodel_confirm_delete.html --> contoh penulis_confirm_delete.html


# =========================================================================
# FORM untuk modifikasi BUKU
class BukuCreate(CreateView):
    model = Buku
    fields = ['judul', 'figure', 'penulis', 'resensi', 'isbn', 'jenis', 'bahasa']
    permission_required = 'katalog.bisa_tandai_kembali'

class BukuUpdate(UpdateView):
    model = Buku
    fields = '__all__' # NOT Recommended. Security issue jika fields baru ditambahkan
    permission_required = 'katalog.bisa_tandai_kembali'

# By Default, nama templatenya harus: namaclassdimodel_form.html --> contoh buku_form.html
# Untuk ganti suffix selain 'form', bisa tambah field template_name_suffix = 'othersuffix'

class BukuDelete(DeleteView):
    model = Buku
    success_url = reverse_lazy('penulis')
    permission_required = 'katalog.bisa_tandai_kembali'
# By Default, nama templatenya harus: namaclassdimodel_confirm_delete.html --> contoh buku_confirm_delete.html
