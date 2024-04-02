/* 1*/
select * from transaksi where tanggal_transaksi between '2023-10-10' and '2023-10-20'

/*2*/
SELECT transaksi_minuman.tm_transaksi_id, SUM(menu_minuman.harga_minuman * transaksi_minuman.jumlah_minuman) AS TOTAL_HARGA
FROM transaksi_minuman, menu_minuman
WHERE transaksi_minuman.tm_menu_minuman_id = menu_minuman.id_minuman
GROUP BY tm_transaksi_id

/*3*/
select customer.nama_customer, customer.id_customer, SUM(menu_minuman.harga_minuman * transaksi_minuman.jumlah_minuman) as Total_Belanja
from customer, transaksi, transaksi_minuman, menu_minuman
where transaksi_minuman.tm_transaksi_id = transaksi.id_transaksi and customer.id_customer = transaksi.customer_id_customer 
and transaksi_minuman.tm_menu_minuman_id = menu_minuman.id_minuman
group by customer.id_customer
order by customer.nama_customer

/*4*/
select pegawai.nik, pegawai.nama_pegawai, pegawai.jenis_kelamin, pegawai.email, pegawai.umur, pegawai.telepon from pegawai
join transaksi on transaksi.pegawai_nik = pegawai.nik
join customer on customer.id_customer = transaksi.customer_id_customer
where customer.nama_customer in ('Davi Liam', 'Sisil Triana', 'Hendra Asto')

/*5*/
select month(transaksi.tanggal_transaksi) as bulan, year(transaksi.tanggal_transaksi) as tahun, sum(transaksi_minuman.jumlah_minuman)
from transaksi, transaksi_minuman
where transaksi.id_transaksi = transaksi_minuman.tm_transaksi_id
group by month(transaksi.tanggal_transaksi), year(transaksi.tanggal_transaksi)
order by tahun, bulan

/*6*/
SELECT AVG(SUM(menu_minuman.harga_minuman * transaksi_minuman.jumlah_minuman))
FROM transaksi_minuman, menu_minuman
WHERE transaksi_minuman.tm_menu_minuman_id = menu_minuman.id_minuman
group by transaksi_minuman.tm_transaksi_id

select SUM(menu_minuman.harga_minuman * transaksi_minuman.jumlah_minuman)
  from menu_minuman, transaksi_minuman
  where transaksi_minuman.tm_menu_minuman_id = menu_minuman.id_minuman
  group by transaksi_minuman.tm_transaksi_id

select SUM(menu_minuman.harga_minuman * transaksi_minuman.jumlah_minuman)/count(transaksi_minuman.tm_transaksi_id)
from menu_minuman, transaksi_minuman
where transaksi_minuman.tm_menu_minuman_id = menu_minuman.id_minuman