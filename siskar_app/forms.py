from django import forms

CHOICES = [(1,'Ya'),(0,'Tidak')]

class FormName(forms.Form):
    attrib_1 = forms.CharField(label='1. Gangguan pernapasan', widget=forms.RadioSelect(choices=CHOICES))
    attrib_2 = forms.CharField(label='2. Demam', widget=forms.RadioSelect(choices=CHOICES))
    attrib_3 = forms.CharField(label='3. Batuk Kering', widget=forms.RadioSelect(choices=CHOICES))
    attrib_4 = forms.CharField(label='4. Sakit tenggorokan', widget=forms.RadioSelect(choices=CHOICES))
    attrib_5 = forms.CharField(label='5. Hidung berlendir', widget=forms.RadioSelect(choices=CHOICES))
    attrib_6 = forms.CharField(label='6. Pengidap Asthma', widget=forms.RadioSelect(choices=CHOICES))
    attrib_7 = forms.CharField(label='7. Memiliki riwayat penyakit paru kronis', widget=forms.RadioSelect(choices=CHOICES))
    attrib_8 = forms.CharField(label='8. Sakit kepala', widget=forms.RadioSelect(choices=CHOICES))
    attrib_9 = forms.CharField(label='9. Memiliki riwayat sakit jantung', widget=forms.RadioSelect(choices=CHOICES))
    attrib_10 = forms.CharField(label='10. Memiliki riwayat Diabetes', widget=forms.RadioSelect(choices=CHOICES))
    attrib_11 = forms.CharField(label='11. Memiliki riwayat Hipertensi', widget=forms.RadioSelect(choices=CHOICES))
    attrib_12 = forms.CharField(label='12. Mengalami kelelahan', widget=forms.RadioSelect(choices=CHOICES))
    attrib_13 = forms.CharField(label='13. Memiliki sakit Lambung', widget=forms.RadioSelect(choices=CHOICES))
    attrib_14 = forms.CharField(label='14. Sedang dalam perjalanan ke luar kota/negeri', widget=forms.RadioSelect(choices=CHOICES))
    attrib_15 = forms.CharField(label='15. Pernah melakukan kontak dengan pasien COVID', widget=forms.RadioSelect(choices=CHOICES))
    attrib_16 = forms.CharField(label='16. Pernah berkumpul di acara besar?', widget=forms.RadioSelect(choices=CHOICES))
    attrib_17 = forms.CharField(label='17. Melakukan kegiatan di tempat umum', widget=forms.RadioSelect(choices=CHOICES))
    attrib_18 = forms.CharField(label='18. Ada anggota keluarga yang Melakukan kegiatan di tempat umum?', widget=forms.RadioSelect(choices=CHOICES))
    attrib_19 = forms.CharField(label='19. Menggunakan Masker', widget=forms.RadioSelect(choices=CHOICES))
    attrib_20 = forms.CharField(label='20. Rajin menggunakan hand sanitizer?', widget=forms.RadioSelect(choices=CHOICES))

