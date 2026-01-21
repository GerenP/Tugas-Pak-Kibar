<?php

function cek_data($data){
  if(isset($_GET[$data]) == true){
    if($_GET[$data] == null){
      return 0;
    }else{
      return $_GET[$data];
    }
  }else{
    return 0;
  }
}

function hasil($a, $b){
  $angka1 = cek_data($a);
  $angka2 = cek_data($b);

  if(isset($_GET['tambah'])){
    return $angka1 + $angka2;
  }elseif(isset($_GET['kurang'])){
    return $angka1 - $angka2;
  }elseif(isset($_GET['kali'])){
    return $angka1 * $angka2;
  }elseif(isset($_GET['bagi'])){
    if($angka2 == 0){
      return "Tidak bisa dibagi 0";
    }
    return $angka1 / $angka2;
  }

  return 0;
}

?>

<!DOCTYPE html>
<html>
  <head>
    <title>Kalkulator using Function</title>
  </head>
  <body>

    <h2>Angka Pertama = <?= cek_data('angka1') ?></h2>
    <h2>Angka Kedua = <?= cek_data('angka2') ?></h2>
    <h2>Hasil = <?= hasil('angka1', 'angka2') ?></h2>

    <hr>

    <form method="GET">
      <label>Angka Pertama</label><br>
      <input type="number" name="angka1"><br><br>

      <label>Angka Kedua</label><br>
      <input type="number" name="angka2"><br><br>

      <input type="submit" name="tambah" value="Tambah">
      <input type="submit" name="kurang" value="Kurang">
      <input type="submit" name="kali" value="Kali">
      <input type="submit" name="bagi" value="Bagi">
    </form>

  </body>
</html>
