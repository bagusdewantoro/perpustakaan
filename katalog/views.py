from django.shortcuts import render
from katalog.models import Buku, Penulis, Jenis, InstanceBuku

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
