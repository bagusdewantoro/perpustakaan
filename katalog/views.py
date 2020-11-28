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

    konteks = {
        'jml_buku': jml_buku,
        'jml_copy': jml_copy,
        'jml_copy_ada': jml_copy_ada,
        'jml_penulis': jml_penulis,
    }

    # render template html index.html dengan data di dalam variabel context
    return render(request, 'index.html', context=konteks)


class BukuListView(generic.ListView):
    model = Buku
    context_object_name = 'koleksi_buku'   # default = buku_list   (context di dalam templatenya)
    template_name = 'katalog/daftar_buku.html'  # default = buku_list.html   (lokasi & nama file html)
    paginate_by = 5

class BukuDetailView(generic.DetailView):
    model = Buku
    # context_object_name  by default = buku_detail
