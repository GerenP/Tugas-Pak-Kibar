# nested = bersarang
# di dalam if / elif / else ada conditional

print("once upon a time at XII PPLG 1")
print("malam itu kelas sudah kosong, hanya ada kamu dan satu gitar di sudut ruangan.")
print("1. Mainkan gitar")
print("2. Tinggalkan gitar")
choice = int(input("= "))

if choice == 1:
    print("jreng... jreng... jreng...")
    print("tiba-tiba ada sosok hitam tinggi dari belakang!")
    print("1. Lari keluar kelas")
    print("2. Tatap sosok itu dan bertanya siapa dia")
    sub = int(input("= "))

    if sub == 1:
        print("kamu lari ke koridor, tapi sekolah gelap banget.")
        print("kamu lihat dua tempat terbuka.")
        print("1. Ke aula")
        print("2. Ke tangga")
        arah = int(input("= "))

        if arah == 1:
            print("kamu masuk aula. gitar yang tadi tiba-tiba udah ada di tengah ruangan.")
            print("kamu sentuh gitar itu dan bayangan tadi langsung hilang.")
            print("GOOD ENDING: kamu bebas dari gangguannya.")
        else:
            print("kamu turun tangga, tapi langkahmu diikuti suara gitar.")
            print("suara itu makin dekat... sampai akhirnya berhenti pas di belakangmu.")
            print("BAD ENDING: kamu ga pernah keluar dari sana.")

    else:
        print("kamu nanya pelan, 'lu siapa?'")
        print("bayangan itu bilang kalau dia cuma mau lagunya dimainkan sampai selesai.")
        print("1. Mainkan lagi gitarnya")
        print("2. Pergi ninggalin kelas")
        pilihan = int(input("= "))

        if pilihan == 1:
            print("kamu lanjutin mainnya sampai nada terakhir.")
            print("bayangan itu redup dan hilang pelan-pelan.")
            print("GOOD ENDING: roh itu akhirnya tenang.")
        else:
            print("kamu pergi, tapi gitar itu berbunyi sendiri tepat setelah kamu keluar.")
            print("BAD ENDING: lagunya belum selesai dan dia masih ngikutin.")

elif choice == 2:
    print("kamu mau pergi dari kelas.")
    print("tapi ada sosok putih kecil berdiri di depan pintu.")
    print("1. Mundur lagi ke dalam kelas")
    print("2. Deketin sosok itu")
    sub = int(input("= "))

    if sub == 1:
        print("kamu mundur dan gitar di pojokan bunyi sendiri.")
        print("suara itu ngikut sampai kamu ngerasa kelas makin dingin.")
        print("BAD ENDING: kamu terkunci bersama suara itu.")
    else:
        print("pas kamu deketin, ternyata itu cuma kain jemuran.")
        print("kamu ketawa, keluar kelas, dan pulang dengan aman.")
        print("SAFE ENDING: cuma halu karena capek belajar.")

else:
    print("kamu diem aja.")
    print("gitar itu tiba-tiba bunyi sendiri, nadanya kayak manggil kamu.")
    print("SECRET ENDING: kamu jadi bagian dari lagu itu.")