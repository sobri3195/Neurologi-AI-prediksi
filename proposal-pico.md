# Neurologi — AI Prediksi *Time-to-Deterioration* Stroke

## Pertanyaan Klinis (PICO)

### **P — Population**
Pasien **stroke iskemik akut** yang datang ke rumah sakit dengan keterbatasan ahli neuroradiologi 24/7.

### **I — Intervention**
Sistem AI yang menggabungkan:
- Interpretasi **CT non-kontras/CTA awal** untuk deteksi tanda iskemia luas, edema dini, dan oklusi pembuluh besar.
- **Model prediksi risiko** untuk memperkirakan:
  - risiko edema serebri berat / *malignant MCA syndrome*,
  - kebutuhan rujukan cepat ke pusat stroke tersier,
  - potensi kebutuhan **hemikraniektomi dekompresif**.

### **C — Comparator**
Alur standar saat ini:
- Interpretasi radiologi konvensional,
- Penilaian klinis dan skor klinis rutin (mis. NIHSS, GCS, parameter hemodinamik/lab sesuai protokol lokal).

### **O — Outcomes**
**Outcome primer:**
- Waktu dari CT awal ke keputusan rujukan (*time-to-referral decision*),
- Waktu dari CT awal ke tiba di pusat rujukan (*time-to-transfer*),
- Akurasi prediksi waktu perburukan neurologis (*time-to-deterioration*).

**Outcome sekunder:**
- Proporsi hemikraniektomi yang dilakukan tepat waktu,
- Mortalitas intrarumah sakit dan/atau 30–90 hari,
- Luaran fungsional **mRS hari ke-90**,
- Lama rawat ICU/rawat inap,
- Kesesuaian keputusan klinis (AI-assisted vs standar).

## Definisi Operasional yang Disarankan

- **Time-to-deterioration**: waktu dari CT awal ke kejadian perburukan neurologis terdefinisi (mis. penurunan GCS ≥2 poin, anisokor baru, atau kebutuhan ventilasi/intubasi karena edema serebri).
- **Malignant MCA**: kombinasi kriteria klinis + imaging (mis. area infark luas teritori MCA, midline shift progresif, edema masif) sesuai konsensus lokal.
- **Hemikraniektomi tepat waktu**: tindakan dilakukan dalam jendela waktu yang direkomendasikan setelah indikasi terpenuhi.

## Desain Studi yang Cocok

- **Tahap pengembangan model**: kohort retrospektif multicenter (data CT/CTA + klinis serial).
- **Tahap validasi**: validasi eksternal temporal/geografis.
- **Tahap implementasi klinis**: studi prospektif pragmatik (mis. *stepped-wedge* atau *before-after*) untuk menilai dampak pada waktu rujukan dan luaran pasien.

## Catatan Implementasi Klinis

- Integrasikan AI sebagai **decision support**, bukan pengganti klinisi.
- Sediakan output yang dapat ditindaklanjuti:
  - skor risiko,
  - estimasi waktu perburukan,
  - rekomendasi level urgensi rujukan.
- Tetapkan protokol eskalasi saat skor risiko tinggi agar dampak terhadap waktu rujukan nyata.

## Ringkasan Satu Kalimat

Pada pasien stroke iskemik akut di RS dengan keterbatasan neuroradiologi, apakah AI interpretasi CT/CTA + model risiko klinis, dibanding interpretasi standar + skor klinis rutin, dapat mempercepat rujukan/keputusan hemikraniektomi dan memperbaiki mortalitas serta mRS 90 hari?
