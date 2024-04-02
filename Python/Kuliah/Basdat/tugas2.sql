/*7*/
select customer.id_customer, customer.nama_customer, 

/*8*/
select * from customer
where id_customer not in (select m_id_customer from membership)

/*9*/
select sum(transaksi.t_id_customer)
from transaksi
join transaksi_minuman on transaksi.id_transaksi = transaksi_minuman.tm_transaksi_id
join menu_minuman on transaksi_minuman.tm_menu_minuman_id = menu_minuman.id_minuman
where menu_minuman.nama_minuman = 'Latte'

/*10*/
